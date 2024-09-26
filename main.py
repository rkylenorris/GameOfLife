# Author: R. Kyle Norris
# capstone project for https://learn.365datascience.com/ Python Bootcamp course
# found at https://learn.365datascience.com/projects/building-conway-s-game-of-life-in-python/
# code provided is in skeleton_code folder

#imports
from game_of_life import GameOfLife


def main():
    game: GameOfLife = GameOfLife(30, 30)
    coords = [(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)]
    game.populate_grid(coords)
    # game.draw_grid(0)
    game.make_n_steps(15)


if __name__ == '__main__':
    main()
