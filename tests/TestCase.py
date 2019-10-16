import requests


class TestCase:

    def get(self, url):
        self.response = requests.get(url)
        return self

    def assertStatus(self, status):
        assert self.response.status_code == status
