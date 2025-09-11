import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/..")

from app.services import lists_task
import pytest

def test_if_function_returns_a_list(mocker):
    mock_read_file = mocker.patch("app.services.read_file")
    expected_content = [{"id": "1", "task": "tarea 1"}, {"id": "2", "task": "tarea 2"}]
    mock_read_file.return_value = expected_content
        
    result = lists_task("/ruta/archivo.json")
        
    assert result == expected_content
    mock_read_file.assert_called_once_with("/ruta/archivo.json")

def test_if_return_empty_list(mocker):
    mock_read_file = mocker.patch("app.services.read_file")
    empty_list = []
    mock_read_file.return_value = empty_list

    result = lists_task("/path/data.json")

    assert result == empty_list
    assert isinstance(result, list)
    mock_read_file.assert_called_once_with("/path/data.json")

def test_file_not_found(mocker):
    """Test que maneja error cuando el archivo no existe"""
    mock_read_file = mocker.patch("app.services.read_file")
    mock_read_file.side_effect = FileNotFoundError("Archivo no encontrado")
        
    with pytest.raises(FileNotFoundError, match="Archivo no encontrado"):
        lists_task("/ruta/inexistente.json")
