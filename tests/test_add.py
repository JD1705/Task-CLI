import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/..")

import pytest
from app.services import create_new_task

def test_creation_of_task_in_already_existing_file(mocker):
    
    mock_read_file = mocker.patch('app.services.read_file')
    mock_write_file = mocker.patch('app.services.write_file')
    mock_exist = mocker.patch('app.services.os.path.exists')

    mock_exist.return_value = True
    mock_read_file.return_value = [{
        "id":"abcde",
        "desc":"test"
        }]

    path = "/ruta/test.json"
    new_task = {
            "id":"fghij",
            "desc":"new test"
            }

    result = create_new_task(path, new_task)

    assert result == "fghij"
    mock_exist.assert_called_once_with(path)
    mock_read_file.assert_called_once_with(path)
    mock_write_file.assert_called_once_with(path, [
            {"id": "abcde", "desc": "test"},
            {"id": "fghij", "desc": "new test"}
        ])

def test_create_task_in_a_new_file(mocker):
    
    mock_read_file = mocker.patch('app.services.read_file')
    mock_write_file = mocker.patch('app.services.write_file')
    mock_exist = mocker.patch('app.services.os.path.exists')

    mock_exist.return_value = False

    path = "/ruta/test.json"
    new_task = {
            "id":"fghij",
            "desc":"new test"
            }

    result = create_new_task(path, new_task)

    assert result == "fghij"
    mock_exist.assert_called_once_with(path)
    mock_read_file.assert_not_called()  # No se debería llamar
    mock_write_file.assert_called_once_with(path, [new_task])
