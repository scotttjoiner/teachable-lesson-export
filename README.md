# Harmony Tools

Tools to convert Teachable HTML lessons to DOCX and upload merged documents to Google Docs.

## ✨ Features
- Extracts lesson content from saved Teachable HTML files
- Converts each lesson into a DOCX document
- Optionally merges all `.docx` files into a single document
- Uploads the merged document to Google Docs via the Drive API
- Supports basic customization (e.g., sorting, merged filename)

## 🛠️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/harmony-tools.git
cd harmony-tools
```

### 2. Install dependencies using Poetry
```bash
poetry install
```

> ✅ This project uses [Poetry](https://python-poetry.org/) for dependency and virtual environment management.

### 3. Authenticate with Google
Place your `credentials.json` file (from Google Cloud Console) in the working directory. A token will be stored after the first run to avoid reauthenticating.

## 📂 Working Directory
By default, the following working directories are created in your home folder:

- `~/harmony-tools/saved_html_lessons`
- `~/harmony-tools/converted_docs`
- `~/harmony-tools/processed_html`

You can override this location using the `--workdir` option.

## ⚙️ Usage

### Convert lessons from HTML to DOCX
```bash
poetry run html2doc
```
- Parses all files in `~/harmony-tools/saved_html_lessons`
- Extracts lesson content
- Creates Word documents in `~/harmony-tools/converted_docs`

### Merge and upload to Google Docs
```bash
poetry run upload2drive
```
- Merges all `.docx` files in the output folder
- Uploads the merged result to Google Docs

### Optional arguments
```bash
poetry run upload2drive --help
```
```
Usage: upload2drive [OPTIONS]

  Merge and upload DOCX lessons to Google Drive

Options:
  --folder-path PATH  Path to folder with lesson .docx files (default: WORKDIR)
  --merged-name TEXT  Filename for merged output (default: foldername.docx)
  --sort [name|ctime] How to sort lessons: 'name' or 'ctime' (default: name)
```

## 📘 How It Works
This tool recursively finds all `.docx` files in the specified folder, merges them into a single document (optionally sorted by filename or creation time), and uploads the result to Google Docs.

- The default merged document name is based on the folder name (e.g., `my-lessons.docx`)
- The output is saved locally and uploaded as a Google Doc
- Only `.docx` files are processed; subfolders are not searched recursively

## 📄 License
MIT License