import re
import sys

with open('/home/user/uploads/Reading Hub.html', 'r') as f:
    content = f.read()

# 1. CSS changes
css_addition = """
.char-entry {
  background: #fcfdfa;
  border: 1px solid #e2e5dc;
  border-radius: 10px;
  padding: 12px;
  margin-bottom: 10px;
  position: relative;
}
.char-entry input, .char-entry textarea {
  margin-bottom: 8px;
  width: 100%;
}
.char-entry textarea {
  min-height: 60px;
  margin-bottom: 0;
}
.char-entry .remove-char {
  position: absolute;
  top: 12px;
  right: 12px;
  background: none;
  border: none;
  color: #a8b4a8;
  font-weight: 800;
  cursor: pointer;
  font-size: 18px;
  padding: 0;
  line-height: 1;
}
.char-entry .remove-char:hover {
  color: var(--coral);
}
"""
content = content.replace('</style>', css_addition + '</style>')

# 2. HTML additions
# Editor section
html_editor = """<div class="full"><label>Your review</label><textarea id="text" placeholder="What stayed with you after the final page?" oninput="updatePreview()"></textarea></div>
<div class="full">
  <label>Characters (Meet the Cast)</label>
  <div id="characterList"></div>
  <button type="button" class="outline" style="padding: 6px 12px; font-size: 12px; margin-top: 5px; border-style: dashed;" onclick="addCharacterField()">+ Add Character</button>
</div>"""
content = content.replace('<div class="full"><label>Your review</label><textarea id="text" placeholder="What stayed with you after the final page?" oninput="updatePreview()"></textarea></div>', html_editor)

# Preview section
html_preview = """<p class="prev-text" id="pText">A thoughtful review deserves a beautiful little home.</p>
<div id="pChars" style="display:none; margin-top: 15px; font-size: 13px; color: #52615b; border-top: 1px dashed #cbd0c7; padding-top: 10px; position:relative; z-index:1"></div>"""
content = content.replace('<p class="prev-text" id="pText">A thoughtful review deserves a beautiful little home.</p>', html_preview)

# 3. JS Additions
# current function
js_current = """function current(){
  let chars = Array.from(document.querySelectorAll('.char-entry')).map(el => ({
    name: el.querySelector('.char-name').value.trim(),
    role: el.querySelector('.char-role').value.trim(),
    notes: el.querySelector('.char-notes').value.trim()
  })).filter(c => c.name);
  return {id:editing||Date.now().toString(),book:value('book'),author:value('author'),ref:value('ref')||'BK-'+String(reviews.length+1).padStart(3,'0'),date:value('date'),rating,text:value('text'),characters:chars,updated:new Date().toISOString()}
}"""
content = re.sub(r"function current\(\)\{return \{id:editing[^}]+\}\}", js_current, content)

# updatePreview function
js_updatePreview = """function updatePreview(){
  let r=current();
  $('pBook').textContent=r.book||'Your next great read';
  $('pAuthor').textContent='by '+(r.author||'an author you admire');
  $('pRef').textContent=r.ref;
  $('pText').textContent=r.text||'A thoughtful review deserves a beautiful little home.';
  
  let pChars = $('pChars');
  if(pChars){
    if(r.characters && r.characters.length > 0) {
      pChars.style.display = 'block';
      pChars.innerHTML = '<strong>Meet the Characters:</strong><ul style="margin:6px 0 0; padding-left:20px; line-height:1.4;">' + 
        r.characters.map(c => `<li><b>${esc(c.name)}</b> ${c.role?`<span style="color:#778580">(${esc(c.role)})</span>`:''} — ${esc(c.notes)}</li>`).join('') +
        '</ul>';
    } else {
      pChars.style.display = 'none';
      pChars.innerHTML = '';
    }
  }
}"""
content = re.sub(r"function updatePreview\(\)\{[^}]+\}", js_updatePreview, content)

# clearForm function
js_clearForm = """function clearForm(){
  editing=null;rating=0;['book','author','ref','text'].forEach(id=>$(id).value='');
  $('date').value=new Date().toISOString().slice(0,10);
  $('characterList').innerHTML='';
  $('formTitle').textContent='Write a book review';
  $('editPill').textContent='NEW REVIEW';
  renderStars();updatePreview()
}"""
content = re.sub(r"function clearForm\(\)\{[^\}]+renderStars\(\);updatePreview\(\)\}", js_clearForm, content)

# editReview function
js_editReview = """function editReview(id){
  let r=reviews.find(x=>x.id===id);if(!r)return;
  editing=id;
  ['book','author','ref','date','text'].forEach(k=>$(k).value=r[k]||'');
  $('characterList').innerHTML='';
  (r.characters||[]).forEach(c => addCharacterField(c));
  rating=r.rating||0;
  $('formTitle').textContent='Edit your review';
  $('editPill').textContent='EDITING';
  renderStars();renderList();updatePreview();window.scrollTo({top:0,behavior:'smooth'})
}"""
content = re.sub(r"function editReview\(id\)\{let r=reviews\.find\(x=>x\.id===id\);if\(!r\)return;editing=id;\['book','author','ref','date','text'\]\.forEach\(k=>\$\(k\)\.value=r\[k\]\|\|''\);rating=r\.rating\|\|0;\$\('formTitle'\)\.textContent='Edit your review';\$\('editPill'\)\.textContent='EDITING';renderStars\(\);renderList\(\);updatePreview\(\);window\.scrollTo\(\{top:0,behavior:'smooth'\}\)\}", js_editReview, content)

# createPost function
js_createPost = """function createPost(type){
  let r=selected()||current();if(!r.book){toast('Save or write a review first.');return}
  let charText = '';
  if(r.characters && r.characters.length > 0) {
    charText = '\\n\\n✨ Meet the Characters:\\n' + r.characters.map(c => `• ${c.name} ${c.role?`(${c.role})`:''}: ${c.notes}`).join('\\n');
  }
  let text=`📚 ${r.book} — ${r.author}\\n\\n${r.text}${charText}\\n\\n${'★'.repeat(r.rating||0)} ${r.ref?`\\n#BookReview #CurrentlyReading`:''}`; 
  if(type==='whatsapp'){
    window.open('https://wa.me/?text='+encodeURIComponent(text),'_blank');toast('Opening WhatsApp share…')
  }else{
    if(navigator.clipboard) navigator.clipboard.writeText(text).catch(e=>{});
    downloadPost(r);toast('Image saved & caption copied to clipboard!')
  }
}"""
content = re.sub(r"function createPost\(type\)\{[^\}]+toast\('Your post image is ready to share on Instagram\.'\)\}\}", js_createPost, content)

# exportCSV function
js_exportCSV = """function exportCSV(){
  let head=['Book Title','Author','Reference No','Finished On','Rating','Review','Characters'];
  let rows=reviews.map(r=>{
    let chars = (r.characters||[]).map(c=>`${c.name} (${c.role}): ${c.notes}`).join(' | ');
    return [r.book,r.author,r.ref,r.date,r.rating,r.text,chars];
  });
  let csv=[head,...rows].map(a=>a.map(v=>'"'+String(v??'').replaceAll('"','""')+'"').join(',')).join('\\n');
  download('leafnote-reviews.csv',csv,'text/csv');toast('CSV exported.')
}"""
content = re.sub(r"function exportCSV\(\)\{[^\}]+toast\('CSV exported\.'\)\}", js_exportCSV, content)

# exportPDF function
js_exportPDF = """function exportPDF(){
  let r=selected();if(!r){toast('Save a review first.');return}
  let charHtml = '';
  if(r.characters && r.characters.length > 0) {
    charHtml = '<h3>Meet the Characters</h3><ul>' + r.characters.map(c => `<li><b>${esc(c.name)}</b> ${c.role?`(${esc(c.role)})`:''} — ${esc(c.notes)}</li>`).join('') + '</ul>';
  }
  let win=window.open('','_blank');
  win.document.write(`<title>${esc(r.book)} — Leafnote</title><style>body{font-family:Georgia,serif;max-width:700px;margin:70px auto;color:#183d39;padding:30px}.tag{font:700 12px Arial;letter-spacing:2px;color:#687}.title{font-size:42px;margin:20px 0 5px}.author{font:20px Arial;color:#687}.line{height:6px;background:#d8ee75;margin:35px 0}.rating{color:#d6991e;font:25px Arial}p{font-size:19px;line-height:1.7;color:#293634} h3{margin-top:30px; font-size:22px; color:#183d39;} ul{font-size:18px; line-height:1.6;}</style><div class=tag>LEAFNOTE BOOK REVIEW · ${esc(r.ref)}</div><h1 class=title>${esc(r.book)}</h1><div class=author>by ${esc(r.author)} · Finished ${esc(r.date||'')}</div><div class=line></div><div class=rating>${'★'.repeat(r.rating||0)}${'☆'.repeat(5-(r.rating||0))}</div><p>${esc(r.text).replaceAll('\\n','<br>')}</p>${charHtml}<script>window.onload=()=>window.print()<\/script>`);
  win.document.close();toast('Print dialog opened — choose “Save as PDF”.')
}"""
content = re.sub(r"function exportPDF\(\)\{[^\}]+toast\('Print dialog opened — choose “Save as PDF”\.'\)\}", js_exportPDF, content)

# Insert addCharacterField
js_addCharacter = """function addCharacterField(c = {}) {
  let list = $('characterList');
  let div = document.createElement('div');
  div.className = 'char-entry';
  div.innerHTML = `
    <button type="button" class="remove-char" onclick="this.parentElement.remove(); updatePreview()" title="Remove character">×</button>
    <input type="text" class="char-name" placeholder="Character Name" value="${esc(c.name||'')}" oninput="updatePreview()">
    <input type="text" class="char-role" placeholder="Who they are (e.g. The Protagonist)" value="${esc(c.role||'')}" oninput="updatePreview()">
    <textarea class="char-notes" placeholder="Interesting traits or what you felt about them" oninput="updatePreview()">${esc(c.notes||'')}</textarea>
  `;
  list.appendChild(div);
}
"""
content = content.replace('function renderStars(){', js_addCharacter + 'function renderStars(){')

with open('/home/user/uploads/Reading Hub_updated.html', 'w') as f:
    f.write(content)
