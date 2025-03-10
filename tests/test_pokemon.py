import pytest
from card_nexus.games.pokemon import PokemonTcgClient

client = PokemonTcgClient()

def test_get_all_eras():
    response = client.get_all_eras()
    assert "error" not in response, "Error message in response"
    assert isinstance(response, list), "Response should be a list of eras"

def test_get_era_by_identifier():
    identifier = "original-series"
    response = client.get_era_by_identifier(identifier)
    assert "error" not in response, "Error message in response"
    assert "name" in response, "Era response should contain 'name'"