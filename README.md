# Alien Invaders by Python and Pygame

Alien Invaders is a 2D arcade game developed in Python using the Pygame library. In this game, you control a spaceship to defend Earth from waves of alien invaders.

## Game Description

- **Objective**: Destroy all the aliens before they reach the bottom of the screen or collide with your spaceship.
- **Controls**:
  - Move Left: `Left Arrow Key`
  - Move Right: `Right Arrow Key`
  - Shoot: `Spacebar`
- **Gameplay**:
  - Aliens move horizontally and descend gradually.
  - Eliminate all aliens to progress to the next level, where the game speed increases.
  - The game ends if an alien collides with your ship or reaches the bottom of the screen.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jubaer-bhuiyan/Alien-Invaders-by-Python-pygame.git
   cd Alien-Invaders-by-Python-pygame
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3.x installed.
   - Install Pygame:
     ```bash
     pip install pygame
     ```

3. **Run the Game**:
   ```bash
   python alien_invasion.py
   ```

## Project Structure

- `alien_invasion.py`: Main module to start the game.
- `settings.py`: Contains game settings like screen size and speed.
- `game_stats.py`: Tracks game statistics such as score and lives.
- `ship.py`: Defines the player's spaceship behavior.
- `alien.py`: Defines alien behavior.
- `bullet.py`: Manages bullet behavior fired by the spaceship.
- `button.py`: Handles the start game's button functionality.
- `scoreboard.py`: Manages the display of scores and levels.

## Resources

- **Pygame Documentation**: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)
- **Python Crash Course by Eric Matthes**: This project is inspired by the "Alien Invasion" project in the book.

## Contributing

Contributions are welcome! Feel free to fork this repository, make enhancements, and submit a pull request.
