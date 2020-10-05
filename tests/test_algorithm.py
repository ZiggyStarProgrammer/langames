from src.algorithm import conclusion, find_gamers
import json
from pathlib import Path
import os
print(os.getcwd())


def test_find_conclusion_no_one_owns_game_means_red():
    assert conclusion(['not owned', 'not owned']) == 'RED'



def test_find_conclusion_no_one_installed_game_means_yellow():
    assert conclusion(['not installed', 'not installed']) == 'YELLOW'


def test_find_conclusion_all_installed_game_means_green():
    assert conclusion(['installed', 'installed']) == 'GREEN'


def test_find_all_gamers():
    data = json.loads(Path('../../langames/data/gamers.json').read_text(encoding='utf8'))
    expected = {"Agneta", "Anni-Frid", "Björn", "Benny"}
    got = find_gamers(data)
    assert expected == got


def test_dummy_gamers():
    data = {"gamers": [{"name": "Larry"}, {"name": "Hasse"}]}
    got = find_gamers(data)
    expected = {"Larry", "Hasse"}
    assert expected == got
