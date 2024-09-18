# Türkiye Cities Game

This Python project is an interactive game where users can guess and type cities of Turkey. The game then places the guessed city on the correct location on a map of Turkey. It’s built using Python’s Turtle Graphics and utilizes a CSV file to track Turkish city data.

## Features
- Interactive user interface: Users type the names of cities, and the cities are plotted on the map in their corresponding regions.
- A total of 81 cities to guess and place.
- **Exit** feature: Whenever the user wants to see all the cities on the map, they can type `Exit`, and all the cities will be displayed.

## Files
- **`main.py`**: The main script that runs the game. This handles user input and plots the cities on the map.
- **`city_file.py`**: A helper file that loads the CSV file and manages city data.
- **`cities.csv`**: Contains the list of Turkish cities along with their corresponding coordinates to be plotted on the map.
- **`turkiye_map.gif`**: A GIF file of Turkey's administrative map used for plotting the cities.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/turkiye_cities_game.git
    ```

2. Install dependencies:
    The game relies on Python’s built-in libraries such as `turtle` and `csv`, which should be available with standard Python installations.

3. Run the game:

    ```bash
    python main.py
    ```

## How to Play

1. When the game starts, a map of Turkey will be displayed.
2. Type the name of a Turkish city (in Turkish) into the prompt.
3. If the city is correctly typed, it will appear on the map in its respective region.
4. Type `Exit` at any time to display all the cities on the map.
5. The game will continue until all 81 cities are placed on the map.

## Screenshots

![Game Start Screenshot](./path-to-screenshot1.png)

*Screenshot of the blank map.*

![Game in Progress](./path-to-screenshot2.png)

*Screenshot of the game in progress with cities being guessed.*

## Acknowledgments
- Map image credit: [coğrafyaharitasi.com](https://cografyaharitasi.com)
- Python Turtle Graphics for providing the functionality to plot the map.
