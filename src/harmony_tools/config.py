import os
import json
from pathlib import Path

import click

CONFIG_FILE = Path.home() / ".harmony-tools" / "config.json"
DEFAULT_WORKDIR = Path.home() / "harmony-tools"
SCOPES = [
    "https://www.googleapis.com/auth/drive.file"
]


class Config:

    @property
    def workdir(self):
        self._ensure_loaded()
        return self._workdir

    @property
    def input_folder(self):
        self._ensure_loaded()
        return self._input_folder

    @property
    def output_folder(self):
        self._ensure_loaded()
        return self._output_folder

    @property
    def processed_folder(self):
        self._ensure_loaded()
        return self._processed_folder

    def __init__(self):
        self._loaded = False
        self._workdir = None
        self._input_folder = None
        self._output_folder = None
        self._processed_folder = None

    def load(self, cli_arg=None, force=False):
        
        if self._loaded and not force:
            return self

        # Fallback order
        workdir = (
            Path(cli_arg)
            if cli_arg
            else (
                Path(os.environ.get("HARMONY_WORKDIR"))
                if os.environ.get("HARMONY_WORKDIR")
                else self._load_from_file() or DEFAULT_WORKDIR
            )
        )

        self._workdir = workdir.expanduser().resolve()
        self._input_folder = self._workdir / "saved_html_lessons"
        self._output_folder = self._workdir / "converted_docs"
        self._processed_folder = self._workdir / "processed_html"

        # Ensure folders exist
        for folder in [
            self._input_folder,
            self._output_folder,
            self._processed_folder,
        ]:
            folder.mkdir(parents=True, exist_ok=True)

        self._loaded = True
        return self

    def save(self):
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with CONFIG_FILE.open("w") as f:
            json.dump({"workdir": str(self.workdir)}, f)

    def _load_from_file(self):
        try:
            if CONFIG_FILE.exists():
                with CONFIG_FILE.open() as f:
                    data = json.load(f)
                    return Path(data.get("workdir")).expanduser().resolve()
        except Exception:
            pass
        return None

    def _ensure_loaded(self):
        if not self._loaded:
            raise RuntimeError(
                "Configuration not initialized. Call `harmony-init` to get started."
            )


# Global singleton instance
config = Config()

@click.command(help="Initialize the harmony-tools working directory.")
@click.option("--workdir", default=None, type=click.Path(file_okay=False), help="Override working directory")
def main(workdir=None):
    config.load(workdir).save()

