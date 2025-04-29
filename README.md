# Teachable Lesson Exporter & Google Drive Uploader

This toolchain automates the conversion of Teachable course content into clean, structured Google Docs for collaboration, editing, or archival.

---

## 🧩 Components

### 1. `html2doc.py` — Teachable HTML to DOCX Converter

Converts exported HTML lessons from Teachable into well-formatted `.docx` files.

- Extracts lesson content, preserving:
  - Paragraphs
  - Headings
  - Lists
  - Images (downloaded + embedded)
  - Hyperlinks and basic formatting (bold, italics)
- Outputs a folder structure like:

```
converted_docs/
  Lesson1/
    lesson.docx
  Lesson2/
    lesson.docx
  ...
```

---

### 2. `upload2drive.py` — Merge Lessons and Upload to Google Drive

Takes a folder of `.docx` files (like `converted_docs/`) and:

- Recursively finds all lesson files
- Sorts them by:
  - Filename (`--sort name`) *(default)*  
  - Creation time (`--sort ctime`)
- Merges into a single `.docx` with:
  - Embedded images
  - Table of contents
  - Optional page breaks between lessons
- Uploads as a Google Doc to your Drive
- Outputs a shareable link

---

## 📁 Project Layout

```
your-repo/
├── src/
│   ├── html2doc/
│   │   └── html2doc.py
│   └── upload2drive.py
├── requirements.txt
├── .gitignore
├── credentials.json            # OAuth file from Google (not included)
└── README.md
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Google API Setup (one-time)

- Enable the **Google Drive API** in your Google Cloud Console
- Download your OAuth `credentials.json`
- Place it in the project root

---

## 🔧 Usage

### ✍️ Convert HTML to DOCX

```bash
python src/html2doc/html2doc.py path/to/html_files/ --output_folder converted_docs/
```

- Each HTML file gets parsed and saved as `lesson.docx` in its own folder.
- Supports inline images, formatting, and layout fidelity.

---

### 📤 Merge + Upload to Google Drive

```bash
python src/upload2drive.py converted_docs/ --merged_name Week3_Lessons.docx --sort name --add_page_break
```

**Options**:
- `--merged_name`: name for the final merged `.docx` and uploaded file
- `--sort`: `name` or `ctime`
- `--add_page_break`: (flag) adds a page break between merged files

---

## 📎 Features

- ✅ Parses HTML from Teachable downloads
- ✅ Merges lessons into one document
- ✅ Preserves images, formatting, headings
- ✅ Uploads to Google Docs via OAuth
- ✅ Adds Table of Contents
- ✅ Clean structure, reusable for other platforms

---

## 🧪 Example Workflow

```bash
# Convert HTML files to DOCX
python src/html2doc/html2doc.py ./html_lessons/ --output_folder converted_docs/

# Merge DOCX files and upload
python src/upload2drive.py converted_docs/ --merged_name "Course Week 3" --sort ctime --add_page_break
```
