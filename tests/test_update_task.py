import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/..")

from app.services import update_task
import pytest
import datetime as dt

def test_if_return_true(mocker):

    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
    mock_datetime = mocker.patch("app.services.dt.datetime")
    mock_read_file.return_value = [{
        "id":"1",
        "desc":"test 1",
        "updatedAt":"2023-01-01"
        },
        {
        "id":"2",
        "desc":"test 2",
        "updatedAt":"2023-02-02"
        }]

    mock_now = mocker.patch("app.services.dt.datetime.now")
    mock_now.return_value = "2024-01-01 12:00:00"
    mock_datetime.now.return_value = mock_now()
    
    result = update_task("/path/data.json", "1", "test updated")

    assert result == True
    mock_write_file.assert_called_once()

    updated_tasks = mock_write_file.call_args[0][1]
    assert updated_tasks[0]["desc"] == "test updated"
    assert updated_tasks[0]["updatedAt"] == "2024-01-01 12:00:00"

def test_if_id_is_not_found(mocker):

    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")

    mock_read_file.return_value = [{"id":"1","desc":"test","updatedAt":"2023-01-01"}]

    result = update_task("/path/data.json","999","test updated")

    assert result == False
    mock_write_file.assert_not_called()

def test_if_file_is_empty(mocker):

    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
    mock_read_file.return_value = []

    result = update_task("/path/data.json", "1", "test updated")

    assert result == False
    mock_write_file.assert_not_called()
