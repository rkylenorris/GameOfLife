from typing import List


class GameOfLife(object):

    def __init__(self, x_dim: int, y_dim: int):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.grid = [[0] * x_dim for _ in range(y_dim)]

    def get_grid(self) -> list:
        # Implement a getter method for your grid.
        return self.grid

    def print_grid(self) -> None:
        # Implement a method to print out your grid in a human-readable format.
        for i, row in enumerate(self.grid):
            row_print = " | ".join(map(str, row))
            border = "-" * len(row_print)
            if i == 0:
                print(border)
            print(row_print)
            print(border)

    def populate_grid(self, coord: list[tuple[int, int]]) -> None:
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for co in coord:
            try:
                self.grid[co[0]][co[1]] = 1
            except IndexError as err:
                print(err)
                print(f'one of more coordinates is not valid for coordinate pair ({co[0]}, {co[1]})')

    def make_step(self) -> None:
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                neighbors = self.get_neighbors([i, j])
                if cell == 0:
                    self.dead_change((i, j), neighbors)
                elif cell == 1:
                    self.live_change((i, j), neighbors)

    def get_neighbors(self, coord: list[int]) -> list[int]:
        """
        gets all cell values of existing neighbor cells
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
        # if dead cell has 3 live neighbors it becomes alive
        if sum(neighbor_vals) == 3:
            self.grid[cell_coord[0]][cell_coord[1]] = 1

    def live_change(self, cell_coord: tuple[int, int], neighbor_vals: list[int]) -> None:
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
        # Implement a method that applies the make_step method n times.
        for _ in range(n):
            self.make_step()

    def draw_grid(self):
        # Draw the current state of the grid.
        pass

