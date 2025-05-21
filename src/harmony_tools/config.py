# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Scott Joiner

import os

from dotenv import load_dotenv

load_dotenv()


# Default values — will be overwritten by `init()`
INPUT_FOLDER = "saved_html_lessons"
PROCESSED_FOLDER = "processed_html"
OUTPUT_FOLDER = "converted_docs"
WORKDIR = None

SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def init(base_dir=None):
    """
    Initializes config constants. Should be called once at startup.
    """
    global INPUT_FOLDER, PROCESSED_FOLDER, OUTPUT_FOLDER, WORKDIR

    WORKDIR = (
        os.path.abspath(base_dir) if base_dir else os.path.expanduser("~/harmony-tools")
    )
    INPUT_FOLDER = os.path.join(WORKDIR, "saved_html_lessons")  # noqa: F841
    PROCESSED_FOLDER = os.path.join(WORKDIR, "processed_html")  # noqa: F841
    OUTPUT_FOLDER = os.path.join(WORKDIR, "converted_docs")  # noqa: F841

    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
