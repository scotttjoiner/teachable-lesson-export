import tempfile
import os
from harmony_tools import config, html2doc


def test_process_file_creates_output(monkeypatch):
    # Setup temp input and output dirs
    with tempfile.TemporaryDirectory() as tmp_input:

        # Create input and output directories
        config.init(tmp_input)

        # Write a dummy HTML file
        filename = "test.html"
        html_path = os.path.join(config.INPUT_FOLDER, filename)
        with open(html_path, "w") as f:
            f.write(
                "<html><body><div class='course-mainbar lecture-content'>"
                "<div class='lecture-attachment'><p>Hello World</p></div></div></body></html>"
            )

        # Run function
        html2doc.process_file(filename)

        # Verify output file was created
        # Expected behavior is a folder is created based on the name of the html doc
        expected_doc = os.path.join(config.OUTPUT_FOLDER, "test", "test.docx")
        assert os.path.isfile(expected_doc)
