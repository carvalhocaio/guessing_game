"""Composition root: creates the GameService and hands control to the
CLI session.
"""

from guessing_game.application.game_service import GameService
from guessing_game.infrastructure.cli.session import Session


def main() -> None:
    service = GameService()
    session = Session(service)
    session.run()


if __name__ == "__main__":
    main()
