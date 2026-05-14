# Rust Guessing Game

This is a beginner Rust project built while studying the language.

## What this project does

This is a simple terminal game where:

- The program generates a random number between `1` and `100`
- You type guesses in the terminal
- The game tells you if your guess is too low or too high
- The loop continues until you guess correctly

## Install Rust

The recommended way to install Rust is with `rustup`.

### Linux / macOS

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

After installation, reload your shell and verify:

```bash
rustc --version
cargo --version
```

### Windows

Download and run `rustup-init.exe` from:

https://www.rust-lang.org/tools/install

Then open a new terminal and verify:

```bash
rustc --version
cargo --version
```

## Run the project

From the project root (`guessing_game`), run:

```bash
cargo run
```

Cargo will compile the project and start the game in your terminal.

## Notes

- Invalid input (like text) is ignored, and the game asks again
- The random number changes every time you run the game
