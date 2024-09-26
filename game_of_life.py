import matplotlib.pyplot as plt
import numpy as np

class GameOfLife(object):
    """
    Class representing the game of life
    """

    def __init__(self, x_dim: int, y_dim: int):
        """
        Initializer takes and x and y dimension
        generates game grid from these values

        :param x_dim: int
        :param y_dim: int
        """
        self.grid = [[0] * x_dim for _ in range(y_dim)]

    def get_grid(self) -> list:
        """
        method to return the game grid

        :return: list
        """
        return self.grid

    def print_grid(self) -> None:
        """
        method that prints grid to console in readable format

        :return: None
        """

        for i, row in enumerate(self.grid):
            row_print = " | ".join(map(str, row))
            border = "-" * len(row_print)
            if i == 0:
                print(border)
            print(row_print)
            print(border)

    def populate_grid(self, coord: list[tuple[int, int]]) -> None:
        """
        method to populate grid with given coordinates
        :param coord: list[tuple[int, int]]
        :return: None
        """

        for co in coord:
            try:
                self.grid[co[0]][co[1]] = 1
            except IndexError:
                raise IndexError(f"Coordinate ({co[0]}, {co[1]}) out of range")

    def make_step(self) -> None:
        """
        method to make the next step in Conway's Game of Life

        :return: None
        """
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                neighbors = self.get_neighbors([i, j])
                if cell == 0:
                    self.dead_change((i, j), neighbors)
                elif cell == 1:
                    self.live_change((i, j), neighbors)

    def get_neighbors(self, coord: list[int]) -> list[int]:
        """
        method to get all cell values of existing neighbor cells
        :param coord: list[int]
        :return: list[int]
        """

        # array of possible directions from a cell
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        # array for holding cell values of neighbor cells
        neighbors = []
        rows = len(self.grid)
        cols = len(self.grid[0])

        for x, y in directions:
            nx, ny = coord[0] + x, coord[1] + y
            # check that cell exists before getting value and appending
            # to neighbors array
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append(self.grid[nx][ny])

        return neighbors

    def dead_change(self, cell_coord: tuple[int, int], neighbor_vals: list[int]) -> None:
        """
        method for checking if dead cell should be live
        if it has 3 live neighbors it gets set to live

        :param cell_coord: tuple[int, int]
        :param neighbor_vals: list[int]
        :return: None
        """
        if sum(neighbor_vals) == 3:
            self.grid[cell_coord[0]][cell_coord[1]] = 1

    def live_change(self, cell_coord: tuple[int, int], neighbor_vals: list[int]) -> None:
        """
        method for checking if live cell should be live or dead
        if 1 or fewer live neighbors it gets set to dead
        if 4 or more live neighbors it gets set to dead
        if 2 or 3 live neighbors it gets set to live

        :param cell_coord: tuple[int, int]
        :param neighbor_vals: list[int]
        :return: None
        """

        live_or_dead: int = 0

        # if live cell has less than or equal to 1 neighbor it dies
        if sum(neighbor_vals) <= 1:
            live_or_dead = 0
        # if live cell has more than or equal to 4 neighbor it dies
        elif sum(neighbor_vals) >= 4:
            live_or_dead = 0
        # if live cell has 2 or 3 live neighbors it survives
        elif sum(neighbor_vals) in range(2, 4):
            live_or_dead = 1

        # assign new value to cell coordinates
        self.grid[cell_coord[0]][cell_coord[1]] = live_or_dead

    def make_n_steps(self, n) -> None:
        """
        method to call method make_step n times
        draws grid for original state and each successive state

        :param n: int number of steps
        :return: None
        """
        self.draw_grid(0)
        for i in range(1, n + 1):
            self.make_step()
            self.draw_grid(step_num=i)

    def draw_grid(self, step_num: int) -> None:
        """
        method to draw the grid using matplotlib

        :param step_num: int number of step in game
        :return: None
        """

        # get coords of all live cells
        live_coords = self.get_live()
        # get coords of all dead cells
        dead_coords = self.get_dead()
        # create x and y values to plot live cells
        y = np.array(live_coords[0])
        x = np.array(live_coords[1])
        live_scatter = plt.scatter(x, y, color='red', s=200)
        # create x and y values to plot dead cells
        y = np.array(dead_coords[0])
        x = np.array(dead_coords[1])
        dead_scatter = plt.scatter(x, y, color='black', s=50)
        # invert axis so it's the same direction as print_grid
        plt.subplot().invert_yaxis()
        # change y tick marks
        plt.yticks(np.arange(y.min(), y.max() + 1, 1))
        plt.title(f'Game of Life -  Step {step_num}')
        plt.subplots_adjust(right=0.7)
        plt.legend((live_scatter, dead_scatter),
                   ('Live Cells', 'Dead Cells'),
                   loc='lower left',
                   bbox_to_anchor=(1.05, 1))
        # show plot
        plt.show()

    def get_live(self) -> list[list[int]]:
        """
        method to get all live cells

        :return: list[list[int]] list of live cell coordinates
        """
        live_cells_x = []
        live_cells_y = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    live_cells_x.append(i)
                    live_cells_y.append(j)

        return [live_cells_x, live_cells_y]

    def get_dead(self) -> list[list[int]]:
        """
        method to get all dead cells

        :return: list[list[int]] list of dead cell coordinates
        """
        dead_cells_x = []
        dead_cells_y = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    dead_cells_x.append(i)
                    dead_cells_y.append(j)

        return [dead_cells_x, dead_cells_y]