Memory Card Game

Description

The Memory Card Game is a simple console-based Python application where players test their memory by matching pairs of hidden cards. At the beginning of the game, the cards are shuffled randomly and displayed as numbered positions. The player selects two card indices in each turn. If the selected cards match, they remain revealed; otherwise, they stay hidden. The game continues until all matching pairs are found.

Features

- Randomly shuffles the cards at the start of each game.
- Displays a numbered game board.
- Allows users to select two cards by entering their indices.
- Checks whether the selected cards match.
- Validates invalid inputs and duplicate selections.
- Announces a congratulatory message when all pairs are matched.

Technologies Used

- Python 3
- Random module

Project Structure

- main.py – Controls the game flow and user interaction.
- memory_module.py – Contains functions for card creation, board display, input handling, match checking, game completion, and result display.

How to Run

1. Make sure Python 3 is installed.
2. Keep "main.py" and "memory_module.py" in the same folder.
3. Open a terminal in the project directory.
4. Run the following command:
   python main.py
5. Follow the on-screen instructions to play the game.

Future Enhancements

- Add score tracking.
- Include a timer to measure performance.
- Provide multiple difficulty levels.
- Develop a graphical user interface (GUI) using Tkinter or Pygame.
- Add multiplayer support and a leaderboard.
