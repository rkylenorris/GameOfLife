# Author: R. Kyle Norris
# capstone project for https://learn.365datascience.com/ Python Bootcamp course
# found at https://learn.365datascience.com/projects/building-conway-s-game-of-life-in-python/
# code provided is in skeleton_code folder

#imports
from game_of_life import GameOfLife


def main():
    game: GameOfLife = GameOfLife(30, 30)
    coords = [(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
(16, 14), (16, 15), (16, 17), (16, 18),
(18, 14), (18, 15), (18, 17), (18, 18),
(14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)]
    # coords = [(y, x) for (x, y) in coords]
    game.populate_grid(coords)
    # game.draw_grid(0)
    game.make_n_steps(6)


if __name__ == '__main__':
    main()
