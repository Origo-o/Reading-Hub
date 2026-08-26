import re

with open('/home/user/uploads/Reading Hub.html', 'r') as f:
    content = f.read()

# Replace inline style for wishlist inputs
content = content.replace(
    '<div style="display:flex;gap:8px;margin-bottom:12px">',
    '<div class="wishlist-inputs">'
)

# Build the new responsive CSS block
responsive_css = """
/* Responsive Design */
.wishlist-inputs {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

@media(max-width:850px){
  .app{padding:15px}
  .grid{grid-template-columns:1fr}
  .hero{padding:25px}
  .hero h1{font-size:28px; line-height:1.2; margin-bottom:12px;}
  .fields{grid-template-columns:1fr}
  .top-actions .outline{display:none}
  .hero:after{right:-120px; top:-100px; width:220px; height:220px; border-width:25px;}
}

@media(max-width:600px){
  .top{flex-direction:column; gap:15px; align-items:flex-start}
  .top-actions{width: 100%;}
  .top-actions .dark{width: 100%; text-align: center; padding: 12px;}
  .brand{font-size:20px}
  .mark{width: 32px; height: 32px; font-size: 18px; border-radius: 10px;}
  .hero{padding:20px}
  .hero h1{font-size:23px; margin-bottom: 10px;}
  .hero p{font-size:14px; line-height: 1.5;}
  .hero:before{bottom: 15px; right: 20px;}
  .editor, .library, .studio, .wishlist, .export{padding:18px}
  .share-row{grid-template-columns:1fr}
  .export-grid{grid-template-columns:1fr}
  .rating-row{flex-direction:column; align-items:flex-start; gap:8px}
  .wishlist-inputs { flex-direction: column; }
  .wishlist-inputs button { width: 100%; padding: 10px; }
  .actions{flex-direction: column-reverse; width: 100%; gap:15px;}
  .actions button{width: 100%; text-align: center;}
  
  .prev-title{font-size:21px; max-width: 90%;}
  .prev-text{font-size:13px; max-width: 90%;}
  .preview:after{font-size:120px; bottom:-30px; right:5px}
  .modalbox{padding: 20px;}
  .modalbox button { width: 100%; margin-top: 10px; float: none !important; }
}
"""

# Replace the old media query with the new responsive CSS
# The old one was: @media(max-width:850px){.app{padding:17px}.grid{grid-template-columns:1fr}.hero{padding:28px}.hero h1{font-size:29px}.fields{grid-template-columns:1fr}.top-actions .outline{display:none}.hero:after{right:-105px}.export-grid{grid-template-columns:repeat(3,1fr)}}
old_media = r"@media\(max-width:850px\)\{[^\}]+\}"
content = re.sub(old_media, responsive_css, content)

with open('/home/user/uploads/Reading Hub_responsive.html', 'w') as f:
    f.write(content)

