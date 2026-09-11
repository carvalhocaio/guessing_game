"""Tests for the pure judge() rule."""

import pytest

from guessing_game.domain.game import Outcome, judge


class TestJudge:
    @pytest.mark.parametrize(
        ("guess", "secret", "expected"),
        [
            (1, 50, Outcome.TOO_LOW),
            (49, 50, Outcome.TOO_LOW),
            (51, 50, Outcome.TOO_HIGH),
            (100, 50, Outcome.TOO_HIGH),
            (50, 50, Outcome.CORRECT),
            (1, 1, Outcome.CORRECT),
            (100, 100, Outcome.CORRECT),
        ],
    )
    def test_returns_the_expected_outcome(self, guess, secret, expected):
        assert judge(guess, secret) is expected
