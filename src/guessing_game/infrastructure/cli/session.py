"""Drives one game session: reads guesses from stdin in a loop, evaluates
them via GameService, and prints results. The only layer that touches the
console.
"""

from rich.console import Console

from guessing_game.application.game_service import GameService
from guessing_game.domain.game import Outcome
from guessing_game.infrastructure.cli import output


class Session:
    def __init__(self, service: GameService, console: Console | None = None) -> None:
        self._service = service
        self._console = console if console is not None else Console()

    def run(self) -> None:
        output.print_greeting(self._console)
        while True:
            output.print_prompt(self._console)
            guess = self._read_guess()
            if guess is None:
                output.print_invalid_input(self._console)
                continue

            output.print_guess(self._console, guess)
            outcome = self._service.guess(guess)
            if outcome is Outcome.TOO_LOW:
                output.print_too_low(self._console)
            elif outcome is Outcome.TOO_HIGH:
                output.print_too_high(self._console)
            else:
                output.print_win(self._console)
                break

    def _read_guess(self) -> int | None:
        try:
            value = int(input().strip())
        except ValueError:
            return None
        return value if value >= 0 else None
