#tests/test_fixture_scope.py

import pytest

@pytest.fixture(scope="class")
def sample_data():
    print("\n data load")
    data = {"id":1,"name":"henry"}
    return data

class TestUser:
    def test_id(self,sample_data):
        assert sample_data["id"] == 1
    def test_name(self,sample_data):
        assert sample_data["name"] == "henry"

class TestGuest:
    def test_id(self,sample_data):
        assert sample_data["id"] == 1
    def test_name(self,sample_data):
        assert sample_data["name"] == "henry"
