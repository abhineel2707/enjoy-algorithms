import pytest
from rps_game import RockPaperScissors


@pytest.fixture
def game():
    return RockPaperScissors()


def test_choices(game):
    assert game.choices == ["rock", "paper", "scissors"]


def test_validate_choice(game):
    assert game.validate_choice("rock")
    assert not game.validate_choice("invalid")


def test_get_computer_choice(game):
    assert game.get_computer_choice() in game.choices


def test_determine_winner_tie(game):
    assert game.determine_winner("rock", "rock") == "tie"
    assert game.determine_winner("paper", "paper") == "tie"
    assert game.determine_winner("scissors", "scissors") == "tie"


def test_determine_winner_player_wins(game):
    game.player_score = 0
    game.computer_score = 0
    assert game.determine_winner("rock", "scissors") == "player"
    assert game.player_score == 1
    assert game.computer_score == 0


def test_determine_winner_computer_wins(game):
    game.player_score = 0
    game.computer_score = 0
    assert game.determine_winner("rock", "paper") == "computer"
    assert game.player_score == 0
    assert game.computer_score == 1


def test_check_winner_no_winner_yet(game):
    game.player_score = 2
    game.computer_score = 2
    assert game.check_winner() is None


def test_check_winner_player_wins(game):
    game.player_score = 3
    game.computer_score = 1
    assert game.check_winner() == "player"


def test_check_winner_computer_wins(game):
    game.player_score = 1
    game.computer_score = 3
    assert game.check_winner() == "computer"
