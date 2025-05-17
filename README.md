# Harmony Tools

This project provides command-line utilities to assist in converting and uploading lesson content exported from Teachable.

## Features

- Convert saved HTML lessons (e.g., from Teachable) to clean DOCX format
- Upload DOCX lessons to Google Drive, converting to Google Docs format
- Configurable working directory (default: `~/harmony-tools`)

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management and CLI support.

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   Or refer to [Poetry installation docs](https://python-poetry.org/docs/#installation).

2. **Clone the repository and install dependencies:**
   ```bash
   git clone <your-repo-url>
   cd harmony-tools
   poetry install
   ```

3. **Activate the virtual environment (optional):**
   ```bash
   poetry shell
   ```

## CLI Usage

The project includes two main tools:

### 1. `html2doc`
Convert a folder of exported HTML lessons into DOCX format.

```bash
poetry run html2doc [--workdir <path>]
```

- `--workdir` (optional): Override the default working directory (`~/harmony-tools`).

This will:
- Read from `~/harmony-tools/saved_html_lessons`
- Create `.docx` files in `~/harmony-tools/converted_docs`
- Move processed HTML to `~/harmony-tools/processed_html`

### 2. `upload2drive`
Merge and upload DOCX files to Google Drive (converted to Google Docs).

```bash
poetry run upload2drive [FOLDER_PATH] [--merged-name <filename>] [--sort <name|ctime>] [--workdir <path>]
```

- `FOLDER_PATH`: Path to a folder of `.docx` files (recursively searched)
- `--merged-name`: Optional output filename (default: folder name)
- `--sort`: Sort files by `name` or `ctime` (default: `name`)
- `--workdir`: Override working directory used for token/cache storage

The first time you run this, you will be prompted to authenticate with Google and a `token.pickle` will be saved.

## Configuration

You can define a `.env` file in the project root to override `WORKDIR` or other settings. For example:

```dotenv
WORKDIR=/Users/yourname/Documents/lesson-processing
```

## Folder Structure

```
~/harmony-tools
├── saved_html_lessons     # Input folder for html2doc
├── converted_docs         # Output folder for generated DOCX files
├── processed_html         # Moved HTML files after processing
├── token.pickle           # Stored Google auth token (upload2drive)
```

## License

MIT License

---
This project was built by Scott Joiner to support custom content pipelines for education and coaching applications.
