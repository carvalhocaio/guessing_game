"""Pure comparison rule for a guess against the secret number -- no I/O."""

from enum import Enum, auto

SECRET_RANGE_MIN = 1
SECRET_RANGE_MAX = 100


class Outcome(Enum):
    TOO_LOW = auto()
    TOO_HIGH = auto()
    CORRECT = auto()


def judge(guess: int, secret: int) -> Outcome:
    if guess < secret:
        return Outcome.TOO_LOW
    if guess > secret:
        return Outcome.TOO_HIGH
    return Outcome.CORRECT
