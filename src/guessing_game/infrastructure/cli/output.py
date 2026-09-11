"""Presentation-only formatting for the guessing game, using Rich for
semantic-colored terminal output. No business logic.
"""

from rich.console import Console


def print_greeting(console: Console) -> None:
    console.print("[bold cyan]Guess a number![/bold cyan]")


def print_prompt(console: Console) -> None:
    console.print("Please input your guess.")


def print_invalid_input(console: Console) -> None:
    console.print("[yellow]Please enter a valid number.[/yellow]")


def print_guess(console: Console, guess: int) -> None:
    console.print(f"You guessed: {guess}")


def print_too_low(console: Console) -> None:
    console.print("[red]Too small![/red]")


def print_too_high(console: Console) -> None:
    console.print("[red]Too big![/red]")


def print_win(console: Console) -> None:
    console.print("[bold green]You win![/bold green]")
