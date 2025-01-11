import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data, headers=headers)
        return response

    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, headers=headers)
        return response
