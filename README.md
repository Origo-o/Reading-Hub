# ❧ Leafnote — Book Review & Reading Studio

A serene, feature-rich web application for book lovers and reviewers. Capture your reading thoughts instantly with **Plain Writing Mode**, organize your shelf with **Deep Character Cast Tracking**, sync in real-time with **Firebase Realtime Database**, protect your notes with a **PIN Passcode Gate**, and generate **1080×1080 Instagram Post Cards** and **WhatsApp statuses** complete with character details.

---

## ✨ Features at a Glance

### 1. ✍️ Plain Writing & Structured Review Modes
- **Instant Plain Writing on Entry:** When you open the application, you can start typing your raw thoughts, quotes, and reading reflections freely without mandatory forms.
- **Structured Review Mode:** Toggle with one click to log full review metadata — *Book Title, Author, Reference Number (e.g. BK-042), Finished Date, 5-Star Rating*, and **Character Cast**.
- **Keyboard Shortcuts:** Press `Ctrl + S` (or `Cmd + S` on Mac) to save your entry instantly.

### 2. 🎭 Meet the Cast (Character Tracking)
- Add unlimited characters to any book with **Name**, **Role / Trait** (e.g., *Protagonist, Antagonist, Mentor*), and **Character Notes**.
- Character chips are displayed in your personal shelf and dynamically rendered in PDF exports.
- **Full Social Integration:** Characters are automatically drawn onto your **Instagram cards** and formatted in **WhatsApp shares**.

### 3. 📸 Instagram Share Studio & WhatsApp Status
- **Dynamic 1080×1080 Post Generator:** Renders high-resolution social cards ready for Instagram feeds or square stories using HTML5 Canvas.
- **Includes Character Cast:** If characters are added to the review, a dedicated *"Meet the Cast"* section is dynamically measured and drawn on the card.
- **3 Designer Themes:**
  - 🌿 **Leaf Emerald:** Deep forest green (`#123d39`) with lime gold accents.
  - 📜 **Warm Parchment:** Editorial cream parchment (`#fbf8ef`) with espresso typography.
  - 🌌 **Midnight Obsidian:** Slate dark mode with gradient neon highlights.
- **WhatsApp Share:** Generates a clean, formatted message with star ratings, quotes, and bulleted character summaries.

### 4. ⚡ Real-Time Cloud Sync (Firebase Realtime Database)
- Built with **Firebase Modular SDK v12**.
- **Two-Way Live Sync:** Any review, character change, or wishlist update syncs across all open devices and tabs instantly.
- **Live Cloud Status Indicator:** A pulsing badge in the header shows connection health (`● Cloud Synced` / `Local Mode`).
- **Offline Resilience:** Local cache backup (`localStorage`) guarantees zero data loss even if your internet connection fluctuates.

### 5. 🔒 PIN Passcode Authentication
- **Default Login PIN:** `1234`
- **Interactive Numeric Keypad:** Enter your PIN using the on-screen keypad or physical keyboard numbers (`0-9`, `Backspace`, `Escape`).
- **Session Protection:** Remembers your session while the tab is active; lock anytime with the **"🔒 Lock"** button.
- **Customizable PIN:** Change your PIN anytime via **"⚙ PIN Settings"** in the top navigation.

### 6. 📱 Fully Adaptive & Responsive Design
- **Mobile Devices (320px – 600px):** Single-column layout with 48px touch targets, mobile-optimized keypad, and horizontal scrolling tab bar.
- **Tablets (600px – 1024px):** Fluid two-column grids for side-by-side editing and studio previewing.
- **Desktop & Ultrawide (1200px+):** Generous margins, crisp typography, and instant one-click tab switching.

### 7. 💾 Complete Data Portability & Exports
- **JSON Backup:** Full raw archive with timestamps, ratings, and character lists.
- **CSV Spreadsheet:** Formatted for Google Sheets, Microsoft Excel, or Notion databases.
- **Printable PDF:** Clean, single-page print layout formatted with book quotes and character rosters.
- **File Importer:** Import existing reading logs from `.json`, `.csv`, `.pdf`, or `.txt` files.

---

## 🚀 Quick Start & Usage

### 1. Opening the App
1. Launch `index.html` in any modern web browser.
2. Enter the default PIN: **`1234`** on the lock screen.
3. You will immediately enter the **✍️ Write Note** tab.

### 2. Writing Your First Note
- Type the **Book Title**, **Author**, and your **Thoughts**.
- Click **"+ Add Character"** to record memorable characters from the story.
- Click **"💾 Save Entry"** or press `Ctrl + S` to save to your cloud shelf.

### 3. One-Click Navigation
All tools are organized under the top navigation bar:
- ✍️ **Write Note:** Distraction-free editor (Plain & Structured).
- 📚 **My Shelf:** Browse, search by title/author/character, edit, or delete saved reviews.
- 🎨 **Share Studio:** Preview and export Instagram cards and WhatsApp posts.
- 🔖 **Want to Read:** Quick wishlist for upcoming books with a one-click *"✍️ Review this"* mover.
- 💾 **Export & Import:** Export to JSON, CSV, PDF, or upload backup files.

---

## ⚙️ Firebase Setup & Configuration

Leafnote is pre-configured with Firebase Realtime Database. If you wish to connect your own Firebase project:

1. Go to the [Firebase Console](https://console.firebase.google.com/) and create a project.
2. Enable **Realtime Database** under *Build > Realtime Database*.
3. In **Database Rules**, set read and write permissions:
   ```json
   {
     "rules": {
       ".read": true,
       ".write": true
     }
   }
   ```
4. Open `index.html` and replace the `firebaseConfig` object with your project credentials:
   ```javascript
   const firebaseConfig = {
     apiKey: "YOUR_API_KEY",
     authDomain: "YOUR_PROJECT.firebaseapp.com",
     databaseURL: "https://YOUR_PROJECT-default-rtdb.firebaseio.com",
     projectId: "YOUR_PROJECT",
     storageBucket: "YOUR_PROJECT.firebasestorage.app",
     messagingSenderId: "YOUR_SENDER_ID",
     appId: "YOUR_APP_ID",
     measurementId: "YOUR_MEASUREMENT_ID"
   };
   ```

---

## 🔒 PIN Security Guide

| Feature | Details |
| :--- | :--- |
| **Default PIN** | `1234` |
| **How to Change PIN** | Click **"⚙ PIN Settings"** in the top navigation, enter current PIN (`1234`), then choose and confirm your new 4-digit PIN. |
| **Quick Lock** | Click the **"🔒 Lock"** button in the header at any time to instantly secure your shelf. |
| **Keyboard Input** | Type digits `0` to `9` on your keyboard, `Backspace` to delete, or `Escape` to clear. |

---

## 🛠️ Technology Stack

- **Frontend:** Pure Vanilla HTML5, CSS3, ES Modules (Zero npm build step required).
- **Backend / Realtime Sync:** Firebase Realtime Database (Modular SDK v12 CDN).
- **Social Graphics Engine:** HTML5 Canvas 2D Rendering Context with dynamic word-wrapping and character badge computation.
- **Offline Storage:** Browser `localStorage` + `sessionStorage`.

---

## 📄 License & Attribution

Crafted for readers and book reviewers who appreciate calm, elegant software. Free to use and customize.
