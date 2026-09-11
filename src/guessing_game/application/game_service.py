"""Orchestrates a single guessing game: owns the secret number and
evaluates guesses against it via the pure domain rule.
"""

import random

from guessing_game.domain.game import (
    SECRET_RANGE_MAX,
    SECRET_RANGE_MIN,
    Outcome,
    judge,
)


class GameService:
    def __init__(self, secret: int | None = None) -> None:
        self._secret = (
            secret
            if secret is not None
            else random.randint(SECRET_RANGE_MIN, SECRET_RANGE_MAX)
        )

    def guess(self, value: int) -> Outcome:
        return judge(value, self._secret)
