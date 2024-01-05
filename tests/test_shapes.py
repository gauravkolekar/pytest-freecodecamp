import pytest
import src.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print("Setting up {method}")
    
    def teardown_method(self, method):
        print("Tearing down {method}")

    def test_area(self):
        assert True
    
    def test_area2(self):
        assert True