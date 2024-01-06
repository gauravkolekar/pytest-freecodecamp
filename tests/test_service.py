import pytest
import src.service as service
import unittest.mock as mock

@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    username = service.get_user_from_db(1)
    assert username == "Mocked Alice"