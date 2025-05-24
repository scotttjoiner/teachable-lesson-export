import tempfile
import os
from harmony_tools import html2doc
from harmony_tools.config import config


def test_process_file_creates_output(monkeypatch):
    # Setup temp input and output dirs
    with tempfile.TemporaryDirectory() as tmp_input:

        # Create input and output directories
        config.load(tmp_input, force=True)

        # Write a dummy HTML file
        filename = "test.html"
        html_path = config.input_folder / filename
        html_path.write_text(
            "<html><body><div class='course-mainbar lecture-content'>"
            "<div class='lecture-attachment'><p>Hello World</p></div></div></body></html>"
        )

        # Run function
        html2doc.process_file(filename)

        # Verify output file was created
        # Expected behavior is a folder is created based on the name of the html doc
        expected_doc = str(config.output_folder / "test" / "test.docx")
        assert os.path.isfile(expected_doc)
