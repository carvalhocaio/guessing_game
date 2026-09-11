"""Tests for Session, driven by a scripted stdin and a recording console."""

import builtins

from guessing_game.application.game_service import GameService
from guessing_game.infrastructure.cli.session import Session


def _run_with_inputs(inputs, console):
    responses = iter(inputs)
    original_input = builtins.input
    builtins.input = lambda: next(responses)
    try:
        Session(GameService(secret=50), console).run()
    finally:
        builtins.input = original_input


class TestRun:
    def test_ends_on_a_correct_guess(self, recording_console):
        _run_with_inputs(["50"], recording_console)

        output = recording_console.export_text()
        assert "You guessed: 50" in output
        assert "You win!" in output

    def test_reports_too_low_and_too_high(self, recording_console):
        _run_with_inputs(["10", "90", "50"], recording_console)

        output = recording_console.export_text()
        assert "Too small!" in output
        assert "Too big!" in output

    def test_warns_on_non_numeric_input_and_keeps_looping(self, recording_console):
        _run_with_inputs(["not-a-number", "50"], recording_console)

        output = recording_console.export_text()
        assert "Please enter a valid number." in output
        assert "You win!" in output

    def test_warns_on_negative_input(self, recording_console):
        _run_with_inputs(["-5", "50"], recording_console)

        output = recording_console.export_text()
        assert "Please enter a valid number." in output
        assert "You win!" in output
