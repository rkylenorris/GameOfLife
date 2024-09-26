# Author: R. Kyle Norris
# capstone project for https://learn.365datascience.com/ Python Bootcamp course
# found at https://learn.365datascience.com/projects/building-conway-s-game-of-life-in-python/
# code provided is in skeleton_code folder

#imports
from game_of_life import GameOfLife


def main():
    game: GameOfLife = GameOfLife(6, 5)
    coords = [(1, 0), (4, 5), [3, 2], [4, 1], [0, 3], [1,3], [0,4], [1,2]]
    game.populate_grid(coords)
    game.make_n_steps(5)


if __name__ == '__main__':
    main()
