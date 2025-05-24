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

---

### 🧪 Alternate (without Poetry)
You can also use this project with standard `pip`, without needing to install Poetry.

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install in editable mode**
   ```bash
   pip install -e .
   ```

3. **Run tools**
   ```bash
   harmony-init --help
   html2doc --help
   upload2drive --help
   ```

---

### 3. Authenticate with Google
To upload files to Google Docs, you'll need a `credentials.json` file from the Google Cloud Console:

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a project and enable the **Google Drive API**.
3. Create **OAuth 2.0 Client ID** credentials for a **Desktop Application**.
4. Download the `credentials.json` file.

Place this file in the working directory (default: `~/harmony-tools/`).  
The first time you run `upload2drive`, it will prompt you to log in. Your access token will be saved to `token.pickle` in the same folder for future runs.

## 📂 Working Directory
By default, the following folders are created under your home directory (`~/harmony-tools/`):

- `saved_html_lessons` – where you put raw Teachable HTML files
- `converted_docs` – where the generated `.docx` files are saved
- `processed_html` – where processed HTML files are moved after conversion

> These directories are automatically created if they don't exist.

To change the location of the working directory, use the `--workdir` option:
```bash
html2doc --workdir /custom/path
upload2drive --workdir /custom/path
```

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