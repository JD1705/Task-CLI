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

def test_create_multiple_tasks(mocker):
    """Test añadiendo múltiples tasks"""
    mock_read_file = mocker.patch("app.services.read_file")
    mock_write_file = mocker.patch("app.services.write_file")
    mock_exists = mocker.patch("app.services.os.path.exists")
        
    mock_exists.return_value = True
    mock_read_file.return_value = []  # Archivo vacío
        
    path = "/ruta/archivo.json"
        
    # Añadir primera task
    task1 = {"id": "id1", "task": "task 1"}
    result1 = create_new_task(path, task1)
        
    # Añadir segunda task
    task2 = {"id": "id2", "task": "task 2"}
    result2 = create_new_task(path, task2)
        
    assert result1 == "id1"
    assert result2 == "id2"
        
    # Verificar que write_file fue llamado con las tasks acumuladas
    assert mock_write_file.call_count == 2
    assert mock_write_file.call_args_list[1][0][1] == [task1, task2]

