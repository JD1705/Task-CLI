import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/..")

from app.services import delete_task
import pytest

def test_if_return_true_when_find_file(mocker):
    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
        
    tasks = [{"id": "1", "task": "test 1"}, {"id": "2", "task": "test 2"}]
    mock_read_file.return_value = tasks
        
    result = delete_task("/path/data.json", "1")
        
    assert result == True
    mock_write_file.assert_called_once_with("/path/data.json", [{"id": "2", "task": "test 2"}])

def test_delete_unexistent_task(mocker):
    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
        
    tasks = [{"id": "1", "task": "test 1"}]
    mock_read_file.return_value = tasks
    
    result = delete_task("/ruta/archivo.json", "999")
        
    assert result == False
    mock_write_file.assert_not_called()

def test_empty_file(mocker):
    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
        
    mock_read_file.return_value = []
        
    resultado = delete_task("/ruta/archivo.json", "1")
        
    assert resultado == False
    mock_write_file.assert_not_called()
