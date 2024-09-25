# Author: R. Kyle Norris
# capstone project for https://learn.365datascience.com/ Python Bootcamp course
# found at https://learn.365datascience.com/projects/building-conway-s-game-of-life-in-python/
# code provided is in skeleton_code folder

#imports
from game_of_life import GameOfLife


def main():
    game: GameOfLife = GameOfLife(6, 5)
    coords = [(1, 0), (5, 4)]
    game.populate_grid(coords)
    game.print_grid()
    print(game.get_neighbors([0,0]))


if __name__ == '__main__':
    main()
