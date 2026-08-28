# ❧ Leafnote — a quiet notebook for the books you love

Leafnote is a calm, one-tap reading journal. Open it, write what a book made you feel, tap **Save note** — and when a note deserves to travel, turn it into an **elegant one-page letter PDF** and send it to anyone. No clutter, no noise: just you, your books, and a beautifully simple place to keep your thoughts.

A real example of a generated letter is included in this repository: open **`sample-letter.pdf`**.

---

## ✨ What it does

### ✍️ One-tap note taking
- The app opens straight onto the writing page. Two fields are required — **the book** and **your thoughts**. That's it.
- Author, 5★ rating, reference number, finished date and character notes are optional and tucked behind **“More details”**, so the page always looks like a simple, reliable notebook.
- `Ctrl/Cmd + S` saves instantly. Everything is kept locally *and* synced to Firebase in real time.

### ✉️ Send any note as an elegant letter (new)
- Tap **✉️ Letter** on any note (or **Send as Letter** while writing, or **Backup → Elegant Letter PDF**).
- Say who it's for and who it's from, watch the live paper preview, then tap **Make PDF & send**.
- The letter is typeset like fine stationery — leaf letterhead, double rule, dated salutation, your review beside a quiet gold rule, hand-drawn star rating, a “characters worth meeting” cast list, and your signature with a gold flourish.
- One tap hands the PDF to your phone's share sheet (WhatsApp, Gmail, Drive, AirDrop…). On desktop it downloads, with one-click follow-ups for **WhatsApp** and **Email**.
- Sender and recipient names are remembered, so the next letter is two taps.

### 📚 My Shelf
- A clean, searchable list of everything you've recorded. Each card shows the book, your stars and a snippet, with **Letter**, **Edit** and delete right on the card.

### 🔖 Want to Read
- A quiet wishlist for upcoming books, with a one-tap **“✍️ Review this”** that moves a book straight into the writer.

### 🎨 Studio & 🗂 Backup (tucked one level down)
- Instagram 1080×1080 cards (three themes) and WhatsApp shares, still one tab away.
- JSON / CSV backups, printable sheets, and file import — under **Backup**.

### 🔒 Private by design
- PIN passcode gate (default **1234**, change it under **PIN** in the top bar).
- Live cloud-sync badge in the header; your notes survive offline via local backup.

---

## 🚀 Quick start

1. Open `index.html` in any modern browser (no build step needed).
2. Enter the default PIN **1234**.
3. Write a note, tap **Save note**.
4. Tap **✉️ Letter** on the note, enter a recipient, tap **Make PDF & send** — done.

---

## ⚙️ Firebase setup

Leafnote is pre-configured with Firebase Realtime Database. To use your own project:

1. Create a project in the [Firebase Console](https://console.firebase.google.com/) and enable **Realtime Database**.
2. Set read/write rules for development:
   ```json
   {
     "rules": {
       ".read": true,
       ".write": true
     }
   }
   ```
3. Replace the `firebaseConfig` object in `index.html` with your project credentials.

---

## 🛠️ Technology

- Pure vanilla HTML/CSS/JS in a single file — no build step.
- Firebase Realtime Database (modular SDK, CDN) for live sync; `localStorage` as an offline safety net.
- **jsPDF** (CDN) draws the letter entirely in vector type — leaf ornament, stars and signature included — so every PDF is crisp, tiny and selectable-text.
- HTML5 Canvas renders the Instagram cards.

Crafted for readers who like their software the way they like their paper: quiet, warm, and dependable.
