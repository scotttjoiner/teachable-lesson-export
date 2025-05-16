import os

# Default values — will be overwritten by `init()`
INPUT_FOLDER = "saved_html_lessons"
PROCESSED_FOLDER = "processed_html"
OUTPUT_FOLDER = "converted_docs"
WORKDIR = None

SCOPES = ['https://www.googleapis.com/auth/drive.file']


def init(base_dir=None):
    """
    Initializes config constants. Should be called once at startup.
    """
    global SAVED_LESSONS, PROCESSED_HTML, CONVERTED_DOCS, WORKDIR

    WORKDIR = os.path.abspath(base_dir) if base_dir else os.path.expanduser("~/html2doc")
    SAVED_INPUT_FOLDERLESSONS = os.path.join(WORKDIR, "saved_html_lessons")  # noqa: F841
    PROCESSED_FOLDER = os.path.join(WORKDIR, "processed_html")  # noqa: F841
    OUTPUT_FOLDER = os.path.join(WORKDIR, "converted_docs")  # noqa: F841

    os.makedirs(SAVED_LESSONS, exist_ok=True)
    os.makedirs(PROCESSED_HTML, exist_ok=True)
    os.makedirs(CONVERTED_DOCS, exist_ok=True)