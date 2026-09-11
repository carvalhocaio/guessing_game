"""Tests for GameService, exercised with an injected secret so results
are deterministic.
"""

from guessing_game.application.game_service import GameService
from guessing_game.domain.game import SECRET_RANGE_MAX, SECRET_RANGE_MIN, Outcome


class TestGuess:
    def test_too_low(self):
        service = GameService(secret=50)

        assert service.guess(10) is Outcome.TOO_LOW

    def test_too_high(self):
        service = GameService(secret=50)

        assert service.guess(90) is Outcome.TOO_HIGH

    def test_correct(self):
        service = GameService(secret=50)

        assert service.guess(50) is Outcome.CORRECT


class TestDefaultSecret:
    def test_picks_a_secret_within_range_when_omitted(self):
        service = GameService()

        assert service.guess(SECRET_RANGE_MIN - 1) is Outcome.TOO_LOW
        assert service.guess(SECRET_RANGE_MAX + 1) is Outcome.TOO_HIGH
