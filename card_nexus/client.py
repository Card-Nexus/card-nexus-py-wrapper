import requests
from .games.pokemon import PokemonTcgClient


class CardNexusClient:

    def __init__(self, game):
        self.not_implemented = "This method is not supported for the selected game."
        if game == 'pokemon':
            self.client = PokemonTcgClient()

    def fetch_all_eras(self):
        """Fetches all eras for the selected game."""
        if hasattr(self.client, 'get_all_eras'):
            return self.client.get_all_eras()
        else:
            raise NotImplementedError(
                self.not_implemented)

    def fetch_era_by_identifier(self, identifier):
        """Fetches a specific era by its identifier for the selected game."""
        if hasattr(self.client, 'get_era_by_identifier'):
            return self.client.get_era_by_identifier(identifier)
        else:
            raise NotImplementedError(
                self.not_implemented)

    def fetch_sets(self):
        if hasattr(self.client, 'get_all_sets'):
            return self.client.get_all_sets()
        else:
            raise NotImplementedError(
                self.not_implemented)

    def fetch_set_by_identifier(self, identifier):
        """Fetches a specific set by its identifier for the selected game."""
        if hasattr(self.client, 'get_set_by_identifier'):
            return self.client.get_set_by_identifier(identifier)
        else:
            raise NotImplementedError(self.not_implemented)

    def fetch_all_cards(self, limit=20, offset=0, filters=None):
        """Fetches all cards for the selected game, with optional filters and pagination."""
        if hasattr(self.client, 'get_all_cards'):
            return self.client.get_all_cards(limit=limit, offset=offset, filters=filters)
        else:
            raise NotImplementedError(
                self.not_implemented)

    def fetch_card_by_identifier(self, identifier):
        """Fetches a specific card by its identifier for the selected game."""
        if hasattr(self.client, 'get_card_by_identifier'):
            return self.client.get_card_by_identifier(identifier)
        else:
            raise NotImplementedError(
                self.not_implemented)


client = CardNexusClient(game='pokemon')
sets = client.fetch_sets()
print(sets)
