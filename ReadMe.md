## Rock-Paper-Scissors Game

This is a Rock-Paper-Scissors game implemented using Python and Tkinter. The game features different difficulty levels for the computer opponent and includes a graphical user interface (GUI) to enhance the user experience.

### Features

- **Difficulty Levels:** 
  - **Easy:** The computer makes random choices.
  - **Medium:** The computer sometimes makes strategic choices based on the player's previous choice.
  - **Hard:** The computer uses more sophisticated strategies to predict the player's choice.
  - **Impossible:** The computer always wins based on the player's previous choice.

- **Score Tracking:** Tracks the scores for both the player and the computer.

- **Sound Effects:** Includes sound effects for different game actions and outcomes.

- **GUI Elements:** 
  - Difficulty selection buttons
  - Labels for displaying choices and scores
  - Reset button to start a new game

### Installation

To run this game, ensure you have Python installed on your machine. This game uses the Tkinter library for the GUI, which is included with Python by default. You may need additional sound files if not included.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/cansuyildiriim/rock-paper-scissors.git
    ```
2. **Navigate to the Game Directory:**

   ```bash
    cd rock-paper-scissors
    ```

3. **Run the Game:**

   ```bash
   python rock_paper_scissors.py
    ```
### Usage

- **Select Difficulty Level:** Choose a difficulty level for the computer opponent by clicking one of the difficulty buttons.
- **Make Your Choice:** Click on one of the options (Rock, Paper, Scissors) to make your choice.
- **View Results:** The game will display the result of each round, update scores, and show the computer's choice.
- **Reset Game:** Click the "Reset" button to start a new game.
- **Play Again:** After the game ends, you can choose to play again or exit.

### Code Overview

- **`get_computer_choice()`:** Determines the computer's choice based on the selected difficulty level.
- **`set_difficulty(level)`:** Sets the game's difficulty level and updates the UI.
- **`ask_play_again()`:** Asks the player if they want to play another game and handles the response.
- **`reset_game()`:** Resets the game state for a new game.
- **GUI Elements:** Configured using Tkinter, including labels, buttons, and sound effects.

### Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

### Acknowledgements

- Tkinter documentation for GUI components.
- Python documentation for language features.
- Various online resources for sound effects and game design principles.
