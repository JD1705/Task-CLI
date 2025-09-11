import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/..")

from app.services import list_tasks_done
import pytest

def test_if_return_correct_tasks(mocker):
    mock_read_file = mocker.patch("app.services.read_file")
        
    tasks = [
        {"id": "1", "task": "test 1", "status": "done"},
        {"id": "2", "task": "test 2", "status": "to-do"},
        {"id": "3", "task": "test 3", "status": "done"},
        {"id": "4", "task": "test 4", "status": "in progress"}
    ]
    mock_read_file.return_value = tasks
        
    result = list_tasks_done("/path/data.json")
        
    assert result == [
        {"id": "1", "task": "test 1", "status": "done"},
        {"id": "3", "task": "test 3", "status": "done"}
    ]
    mock_read_file.assert_called_once_with("/path/data.json")

def test_if_file_has_no_done_tasks(mocker):
    mock_read_file = mocker.patch("app.services.read_file")

    tasks = [
        {"id": "1", "task":"test 1", "status":"to-do"},
        {"id": "2", "task":"test 2", "status":"in-process"}
    ]

    mock_read_file.return_value = tasks

    result = list_tasks_done("/path/data.json")

    assert result == []
    assert isinstance(result, list)

def test_list_tasks_done_error_reading(mocker):
    mock_read_file = mocker.patch("app.services.read_file")
    mock_read_file.side_effect = IOError("Read Error")
        
    with pytest.raises(IOError, match="Read Error"):
        list_tasks_done("/path/data.json")
