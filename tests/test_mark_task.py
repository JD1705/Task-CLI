import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/..")

from app.services import mark_tasks
import pytest

def test_if_return_true(mocker):

    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
    mock_read_file.return_value = [{
        "id":"1",
        "desc":"test 1",
        "status":"to-do",
        "updatedAt":"2023-01-01"
        }]

    mock_datetime = mocker.patch("app.services.dt.datetime")
    mock_now = mocker.patch("app.services.dt.datetime.now")
    mock_now.return_value = "2024-02-02 12:00:00"
    mock_datetime.return_value = mock_now()

    state = "done"
    result = mark_tasks("/path/data.json", "1", state)

    assert result == True
    mock_write_file.assert_called_once()

    marked_tasks = mock_write_file.call_args[0][1]
    assert marked_tasks[0]["status"] == "done"
    assert marked_tasks[0]["updatedAt"] == "2024-02-02 12:00:00"

def test_if_id_is_not_found(mocker):

    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")

    mock_read_file.return_value = [{"id":"1","desc":"test", "status":"to-do","updatedAt":"2023-01-01"}]

    result = mark_tasks("/path/data.json","999", "done")

    assert result == False
    mock_write_file.assert_not_called()

def test_reading_error(mocker):

    mock_read_file = mocker.patch("app.services.read_file")
    mock_read_file.side_effect = IOError("Read Error")

    with pytest.raises(IOError, match="Read Error"):
        mark_tasks("/path/data.json", "1", "done")

def test_writing_error(mocker):

    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
    mock_read_file.return_value = [{
        "id":"1",
        "desc":"test 1",
        "status":"to-do",
        "updatedAt":"2023-01-01"
        }]
    mock_write_file.side_effect = IOError("Write Error")

    with pytest.raises(IOError, match="Write Error"):
        mark_tasks("/path/data.json", "1", "done")
