from unittest.mock import patch, MagicMock
from harmony_tools import upload2drive, config


@patch("harmony_tools.upload2drive.os.path.exists", return_value=True)
@patch("harmony_tools.upload2drive.pickle.load", return_value=MagicMock(valid=True))
@patch("harmony_tools.upload2drive.build")
@patch("harmony_tools.upload2drive.MediaFileUpload")
def test_upload_to_google_drive(
    mock_media, mock_build, mock_pickle, mock_exists, monkeypatch, tmp_path
):

    #monkeypatch.setattr(upload2drive.config, "WORKDIR", tmp_path)
    config.init(tmp_path)

    # Setup dummy doc
    test_doc = tmp_path / "dummy.docx"
    test_doc.write_bytes(b"test")

    # Ensure dummy token.pickle exists
    token_path = tmp_path / "token.pickle"
    token_path.write_bytes(b"fake-token-data")
    
    # Configure mocks
    mock_service = MagicMock()
    mock_service.files.return_value.create.return_value.execute.return_value = {
        "id": "fake-id"
    }
    mock_build.return_value = mock_service

    result = upload2drive.upload_to_google_drive(str(test_doc))

    print(mock_media.call_args_list)
    print(mock_media)
    mock_media.assert_called_once_with(
        str(test_doc),
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    mock_service.files.assert_called_once()
    #assert "fake-id" in result
