import requests

class TcgClient:
    def __init__(self):
        self.base_url = 'http://localhost:3000/v1/tcg'

    def get_all_tcg(self):
        """Fetches all TCG games in API"""
        try:
            response = requests.get(f"{self.base_url}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching cards: {e}")
            return {"error": "Failed to fetch cards"}
        
    def get_tcg_by_identifier(self, identifier):
        """Fetches a specific TCG game by its identifier"""
        try:
            response = requests.get(f"{self.base_url}/{identifier}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching card by identifier: {e}")
            return {"error": "Failed to fetch card by identifier"}