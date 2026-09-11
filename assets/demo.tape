# VHS tape recording the Guessing Game demo.
# Install VHS (https://github.com/charmbracelet/vhs) and run:
#   vhs assets/demo.tape
# Requires vhs <= 0.11.0 -- v0.12.0 has a regression where the render step
# receives an already-cancelled context and silently produces no output
# (https://github.com/charmbracelet/vhs/compare/v0.11.0...v0.12.0).
Output assets/demo.gif

Set Shell "bash"
Set FontSize 16
Set Width 1000
Set Height 500
Set Theme "Dracula"
Set TypingSpeed 60ms

Type "uv run guessing-game"
Enter
Sleep 1s

Type "not-a-number"
Enter
Sleep 1500ms

Type "50"
Enter
Sleep 1s

Type "80"
Enter
Sleep 1s

Type "20"
Enter
Sleep 1500ms

Ctrl+C
