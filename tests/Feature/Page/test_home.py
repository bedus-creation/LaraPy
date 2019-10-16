from tests.TestCase import TestCase
import pytest


@pytest.mark.network
class TestHome(TestCase):
    def test_home_page_is_working(self):
        self.get('http://localhost:8080').assertStatus(200)
