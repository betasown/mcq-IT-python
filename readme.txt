Here's a README file for your project:

```markdown
# AES - Minor Setback: A Quiz Game

AES - Minor Setback is a multiple-choice quiz game developed as part of a school project at CESI. This interactive game tests your knowledge of foundational IT concepts through a series of engaging questions. Built using Python and Tkinter, the game features rounds of varying difficulty to challenge players and enhance learning.

## Features

- **Multiple Rounds**: The game consists of three standard rounds and a final round.
- **Interactive Gameplay**: Players select answers via intuitive buttons with real-time feedback.
- **Dynamic Scoring**: Scores update after each question, displayed at the bottom of the screen.
- **Engaging Visuals**: A colorful UI using Tkinter with easy navigation between screens.
- **Informative Topics**:
  - Basics of programming (OOP, data structures)
  - Networking (IP, MAC address, protocols)
  - Security (password practices)
  - Methodologies (Agile, primary keys in databases)

## Rules

1. The game includes three rounds and a final round.
2. Each round has several questions.
3. Choose the correct answer from four options.
4. Correct answers are highlighted in green, incorrect ones in red.
5. Scores are displayed at the end of each round.
6. Aim for the highest score!

## Installation and Usage

### Prerequisites

- Python 3.x installed on your system
- Tkinter library (included by default in Python standard library)

### Steps to Run

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd aes-minor-setback
   ```
3. Run the game:
   ```bash
   python game.py
   ```

### Game Navigation

1. On launch, the main menu offers options to start rounds, view rules, or view credits.
2. Choose a round to begin answering questions.
3. Follow on-screen instructions and select your answers.
4. At the end of a round, your score will be displayed.
5. Return to the main menu to explore other rounds or review game rules.

## Code Structure

- **`QuizGame` class**: Handles game logic, UI components, and navigation.
- **Questions**: Organized into dictionaries by round (e.g., `round1`, `round2`).
- **Methods**:
  - `create_main_menu`: Displays the main menu.
  - `show_question`: Displays a question and options for the current round.
  - `check_answer`: Evaluates selected answers and updates the score.
  - `show_results`: Displays the final score at the end of a round.
  - `show_rules`/`show_credits`: Displays rules and credits screens, respectively.

## Learning Outcomes

This project reinforces:
- Basic Python programming
- GUI development with Tkinter
- Structuring code for readability and functionality
- IT foundational knowledge (e.g., programming, networking, security)

## Credits

- **Developer**: Beta
- **Year**: 2024
- Created as part of a CESI assignment.

## License

This project is distributed for educational purposes. Modify and use it as a reference for learning Python and Tkinter.
