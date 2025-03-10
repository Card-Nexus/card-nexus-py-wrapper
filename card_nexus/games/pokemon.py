import requests


class PokemonTcgClient:
    def __init__(self):
        self.base_url = 'http://localhost:3000/v1/pokemon'

    def get_all_eras(self):
        """Fetches all Pokemon TCG eras"""
        try:
            response = requests.get(f"{self.base_url}/eras")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching eras: {e}")
            return {"error": "Failed to fetch all eras"}

    def get_era_by_identifier(self, identifier):
        """Fetches a specific era by its identifier (either id or slug)"""
        try:
            response = requests.get(f"{self.base_url}/eras/{identifier}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching era by identifier: {e}")
            return {"error": "Failed to fetch era by identifier"}

    def get_all_sets(self, era=None, name=None, sort=None, order=None):
        """
        Fetches all sets, with optional filtering by era and name, and optional sorting by release date.
        """
        params = {}
        if era:
            params['era'] = era
        if name:
            params['name'] = name
        if sort:
            params['sort'] = sort
        if order:
            params['order'] = order

        response = requests.get(f"{self.base_url}/sets", params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_set_by_identifier(self, identifier):
        """Fetches a specific set by its identifier (either id or slug)"""
        try:
            response = requests.get(f"{self.base_url}/sets/{identifier}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching set by identifier: {e}")
            return {"error": "Failed to fetch set by identifier"}

    def get_all_cards(self, limit=20, offset=0, filters=None):
        """
        Fetches all cards, with optional filters and pagination (limit/offset).
        Filters are expected in a dictionary with keys as fields and values as the search term or range.
        """
        params = {
            'limit': limit,
            'offset': offset
        }

        if filters:
            for key, value in filters.items():
                params[key] = value

        try:
            response = requests.get(f"{self.base_url}/cards", params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching cards: {e}")
            return {"error": "Failed to fetch cards"}

    def get_card_by_identifier(self, identifier):
        """Fetches a specific card by its identifier (either id or slug)"""
        try:
            response = requests.get(f"{self.base_url}/cards/{identifier}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching card by identifier: {e}")
            return {"error": "Failed to fetch card by identifier"}
