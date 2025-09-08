import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + "/..")

from app import id_generator
import pytest

def test_id_lenght(mocker):
    
    mock_randint = mocker.patch("app.services.randint", return_value=10)

    result = id_generator()

    assert len(result) == 5
    assert mock_randint.call_count == 5

def test_id_type_is_string(mocker):
    
    mock_randint = mocker.patch("app.services.randint", return_value=10)

    result = id_generator()

    assert isinstance(result, str)

def test_verify_mock(mocker):

    mock_randint = mocker.patch("app.services.randint")
    mock_randint.side_effect = [0,1,2,3,4]

    result = id_generator()

    letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    letters_result = letters[0] + letters[1] + letters[2] + letters[3] + letters[4]

    assert result == letters_result
