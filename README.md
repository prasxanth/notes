# Personal Knowledge Apps

> A collection of personal single-file web apps — metabolic tracking, Vedic sādhana, Yoga study, and a reading library — each designed to live on an iPhone home screen.

---

## Overview

This repository contains a suite of personal knowledge tools. Each app is a single self-contained HTML file: no server, no build step, no dependencies to install. Open any file directly in a browser, or — on iOS — use Safari's **Add to Home Screen** to install it as a standalone app with its own icon, title, and full-screen launch. All apps work fully offline.

The four main apps cover: a metabolic health protocol system driven by blood lab data (**Agni**), a Vedic astrology daily spiritual practice (**Jyotish Sādhana**), a Yoga Sūtra learning course (**Yoga Sudhakara**), and a personal reading library with thematic browsing and stats (**Marginalia**). The books app is backed by a CSV database that can be updated via a small Python script.

---

## Apps

### Agni

**File:** `agni.html`

A lab-directed metabolic protocol system built on the principle: *each lab result activates a protocol.* Agni tracks blood panel results from Function Health / Quest Diagnostics, maps failing biomarker gates to the appropriate intervention protocol, and provides the full daily plan for that protocol.

**Key sections:**

- **Timeline (Home):** Chronological lab entries showing panel date, source, key cardiometabolic markers (ApoB, TG, LDL-P, Ferritin, HDL, hs-CRP), pass/fail gate summary, and a direct link to the activated protocol. Future planned retests appear as pending entries.
- **Labs:** Full detail view for a result set — all gate statuses with current value, target, and delta needed. Shows which protocol was activated and why (e.g., "5 of 8 gates failing → decongestive force protocol").
- **Protocol — SEP Reset · Phase 1:** The active Signal-Explicit Partitioning (SEP) Reset is an 8–16 week cardiometabolic decongestive protocol targeting hepatic VLDL overproduction, insulin resistance, iron deficiency, and lipid export failure. Six protocol tabs:
  - **Schedule** — day-by-day (Mon–Sun) plan
  - **Supps** — 25 supplements with dose, timing, and supply chain notes
  - **Gates** — 8 transition gates (ApoB ≤90, LDL-P ≤1400, TG ≤180, Ferritin ≥30, hs-CRP ≤1.5, HDL ≥35, HbA1c ≤5.6, AST/ALT normal) with current status and delta needed
  - **Caveats** — protocol-specific cautions
  - **Situations** — conditional adjustments for edge-case scenarios
  - **SEP-L** — the next phase; side-by-side comparison of SEP Phase 1 vs. SEP-L (Reversal Phase), which activates only after all 8 gates pass

The December 3, 2025 Function Health panel (Quest Diagnostics, fasting, 40+ markers) is the current active entry. Follow-up panel planned for March–April 2026.

**How to use:** Open `agni.html` in any browser. On iPhone: Safari → Share → Add to Home Screen → launches as **Agni**.

---

### Jyotish Sādhana

**File:** `jyotish_sadhana.html`

A Jyotish (Vedic astrology) daily spiritual practice companion. The app is organized around the principle of witness-awareness (*sākṣi*) as the primary driver of efficacy, with all rituals — mantra, prāṇāyāma, deity worship — understood as vehicles for recognizing the witness rather than ends in themselves.

**Key sections (six screens via bottom navigation):**

- **Home:** Dashboard with a time-aware greeting, a banner for the currently active session (Morning / Midday / Evening / Night), a grid of four modules, and a daily rhythm strip for quick session navigation.
- **Witnessing:** Core philosophical module. Begins with the Mahāsūtra (*Whatever is seen is not you; the one who sees is you*). Six sub-tabs: Nature, Practice, Experience, Scenarios, Self-check, and Non-dual. Each card is expandable with Sanskrit verses, IAST transliteration, English translation, and calibrated insight notes.
- **Daily Practice:** Four session tabs (Morning, Midday, Evening, Night) with structured step sequences. The Morning sequence (Brahma Muhūrta): Nāḍī Śodhana (3–10 min) → Kena Upaniṣad 1.1–1.2 (×3–5) → Gāyatrī Mantra (×108) → Meditation → Witnessing. Each step is an expandable card with full Sanskrit verse, word-by-word breakdown, and rep count pills.
- **Devatā System:** Personal deity (iṣṭadevatā) system. Iṣṭadevatā is Dakṣiṇāmūrti — Śiva as the silent teacher and witness — with primary mantra (ॐ नमो भगवते दक्षिणामूर्तये), full word-by-word table, and the operational rule: 70% awareness quality dominates 30% ritual correctness.
- **Chart Sutras:** Chart-aligned verse recitation system by session. Anchored in Kena Upaniṣad 1.2, Gāyatrī Mantra, and Bhagavad Gītā 2.48. Includes a five-step daily inner sequence (Awareness → Clarity → Equanimity → Detachment → Stillness) with efficacy percentages.
- **Spiritual Canon:** Age-phased reading curriculum (ages 44–62+) in eight stages: Pātañjala Yoga Sūtrāṇi → Bhagavad Gītā → Kena Upaniṣad → Ātmabodha → Vivekacūḍāmaṇi + Kaṭha Upaniṣad → Aṣṭāvakra Gītā → Māṇḍūkya Upaniṣad → Dakṣiṇāmūrti Stotra + Upadeśa Sāhasrī. Each text has an expandable card with rationale, key sūtras, and an alignment probability bar.
- **Life Field** (from home overflow): Interactive SVG node-map of the spiritual arc across life phases (causal perception 0–30 → timing awareness 30–40 → samyama matures 40–55 → continuous witnessing 55+).

**Sanskrit verses with full word-by-word breakdowns:**
- Kena Upaniṣad 1.1, 1.2, 2.4
- Bhagavad Gītā 2.47, 2.48, 18.61
- Gāyatrī Mantra

**How to use:** Open `jyotish_sadhana.html` in any browser. On iPhone: Safari → Share → Add to Home Screen → launches as **Jyotish Sādhana** with a deep amber ॐ icon.

---

### Yoga Sudhakara

**File:** `yoga_sudhakara.html`

A structured learning app for Patañjali's Yoga Sūtras (196 sūtras, 4 chapters) following the *Yoga Sudhākara* commentary by Sadasiva Brahmendra (17th-century Advaita saint), as taught by Swami Paramahamsananda Sarasvatī in the living oral tradition of Parampara Rishividya. The Advaita reading treats Kaivalya as non-different from Brahman-realization rather than the dualistic Puruṣa-isolation of classical Sāṃkhya-Yoga.

**Key sections (four nav items + chapter screens):**

- **Home:** Course dashboard with an "In Progress" banner (Samādhi Pāda — Class 1 active), grid of the four chapters, and quick-access cards for Course Overview and Sūtra Index.
- **Course Overview:** Teacher biography (Swami Paramahamsananda Sarasvatī and the Yoga Sudhākara lineage through Sadasiva Brahmendra), course stats (196 sūtras, 4 chapters, 45 classes), the root text (YS 1.2: *योगश्चित्तवृत्तिनिरोधः*), and a card on what makes the Yoga Sudhākara commentary distinctive.
- **Four chapter screens:**
  - **Samādhi Pāda (Ch. I · 51 sūtras):** Absorption — the gateway sūtras (1.1–1.4), five states of citta, samprajñāta and asamprajñāta samādhi, obstacles, and the path to stillness.
  - **Sādhana Pāda (Ch. II · 55 sūtras):** Practice methods — kleśas, kriyā yoga, aṣṭāṅga yoga (eight limbs), and vivekakhyāti.
  - **Vibhūti Pāda (Ch. III · 56 sūtras):** Saṃyama, dhāraṇā, dhyāna, samādhi, and siddhis arising from concentrated practice.
  - **Kaivalya Pāda (Ch. IV · 34 sūtras):** Liberation — dissolution of the mind, puruṣa, and the nature of Kaivalya.
- **Sūtra Index:** All 196 sūtras browsable by chapter. Each row is expandable for Sanskrit, transliteration, and meaning.

Each sūtra entry has Sanskrit, IAST transliteration, word-by-word table, English translation, and Yoga Sudhākara commentary note.

**How to use:** Open `yoga_sudhakara.html` in any browser. On iPhone: Safari → Share → Add to Home Screen → launches as **Yoga Sudhakara**.

---

### Marginalia

**File:** `books/marginalia.html`

A personal reading library browser (~108 books). Book data is embedded as JSON directly in the HTML and rendered entirely client-side. Named for the notes written in the margins of books — reflecting the app's emphasis on personal impact, notes, and re-read intentions rather than mere cataloguing.

**Key sections (two screens via bottom navigation):**

- **Library:**
  - **Search** — full-text across title, author, notes, and themes
  - **Theme filter chips** — dynamically generated for all themes in the library (Human Cognition & Bias, Literature & Human Condition, Science & Epistemology, Business & Management, Speculative Futures & Myth, Power & Institutions, Systems & Complexity, Health & Longevity, Learning & Productivity, Mythology, Mythic Worlds, Humor & Satire, and more). Tapping a chip filters the list; tapping "All" resets.
  - **Sort** — toggle between alphabetical and impact rating (1–5)
  - **Book cards** — spine icon (initials, color-coded by theme), title, author, genre, impact rating. Expanding a card shows: completion date, audiobook status, re-read flag, Fiction/Nonfiction, recommendation status, personal notes, and all theme chips.
  - **Live count** — header and list meta update as filters change
- **Stats:** Total book count, audiobook %, recommend %, fiction vs. nonfiction split, impact rating distribution (bar chart), and book counts by theme (bar chart).

**CSV structure (`books/books_db.csv`):**

| Column | Notes |
|---|---|
| Title | Book title |
| Author | Author name(s) |
| Audiobook | Y / N |
| Completion Date | Free text (e.g., "January, 2020", "Graduate School") |
| Re-read? | Y / N |
| Genre | Free text (e.g., "Psychology / Behavior") |
| Fiction/Nonfiction | Fiction / Nonfiction |
| Impact (1–5) | Numeric rating |
| Would Recommend | Y / N |
| Notes | Personal notes (free text) |
| Themes | Semicolon-delimited (e.g., `Human Cognition & Bias; Learning & Productivity`) |

**How to use:** Open `books/marginalia.html` in any browser. On iPhone: Safari → Share → Add to Home Screen → launches as **Marginalia** with a deep blue gradient icon.

---

## Books Toolchain

The `books/` directory contains three files that work together:

| File | Role |
|---|---|
| `books_db.csv` | Source of truth — edit this to add, update, or remove books |
| `update_books_navigator_from_csv.py` | Python script that reads the CSV and injects JSON into the HTML |
| `marginalia.html` | The app — reads the embedded JSON at runtime, no server needed |

**Workflow:**

1. Edit `books_db.csv` in any spreadsheet app or text editor. Add a new row per book and use semicolons for multiple themes.
2. Run the updater from the `books/` directory:
   ```bash
   python update_books_navigator_from_csv.py books_db.csv marginalia.html
   ```
3. Open or refresh `marginalia.html` — the new data is live immediately.

**Dependencies:** Python 3, `pandas` (`pip install pandas`).

**Custom paths:** The script accepts optional command-line overrides for both the CSV and HTML paths:
```bash
python update_books_navigator_from_csv.py path/to/books.csv path/to/target.html
```

---

## iOS Home Screen Icons

All four apps are configured for iOS "Add to Home Screen" via Safari. Each HTML file includes:

```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="[App Name]">
<link rel="apple-touch-icon" sizes="180x180" href="data:image/svg+xml,...">
```

The `apple-touch-icon` is inlined as an SVG data URI — no separate image file needed. Once added to the home screen, each app launches full-screen with no browser chrome.

**To install on iPhone:** Open the file in Safari → tap **Share** → tap **Add to Home Screen** → confirm name → tap **Add**.

| App | Icon | Home Screen Name |
|---|---|---|
| Agni | Dark amber with Agni flame motif | Agni |
| Jyotish Sādhana | Deep amber radial gradient with white ॐ | Jyotish Sādhana |
| Yoga Sudhakara | Deep teal with white ॐ | Yoga Sudhakara |
| Marginalia | Navy-to-steel-blue gradient with ✏️ | Marginalia |

---

## Technical Notes

- **Pure HTML/CSS/JS — no framework, no build tooling.** Each file is entirely self-contained. All styles are inline `<style>` blocks, all logic is inline `<script>` blocks.
- **Offline capable.** No network requests at runtime — all apps work without an internet connection once the file is on the device.
- **No server required.** Open directly with `file://` in any desktop browser. On iOS Safari, serve from iCloud Drive or a minimal local server (`python -m http.server`) when installing to the home screen.
- **Data embedding pattern.** Marginalia uses a `<script type="application/json">` block for book data; the other apps embed data directly in JavaScript constants. Everything stays in one file while keeping data clearly separated from logic.
- **Dark theme throughout.** All apps use CSS custom properties for a consistent dark palette with status bar styling set to `black-translucent` for edge-to-edge appearance on iPhone.
- **Mobile-first layout.** Fixed bottom navigation bar, scrollable content area, and thumb-sized tap targets. Viewport set to `width=device-width, initial-scale=1, viewport-fit=cover` with `env(safe-area-inset-*)` padding for notch / Dynamic Island compatibility.
