from typing import List


class GameOfLife(object):

    def __init__(self, x_dim: int, y_dim: int):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.grid = [[0] * x_dim for _ in range(y_dim)]

    def get_grid(self) -> list:
        # Implement a getter method for your grid.
        return self.grid

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        for i, row in enumerate(self.grid):
            row_print = " | ".join(map(str, row))
            border = "-" * len(row_print)
            if i == 0:
                print(border)
            print(row_print)
            print(border)

    def populate_grid(self, coord: list[tuple[int]]):
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for co in coord:
            try:
                self.grid[co[1]][co[0]] = 1
            except IndexError as err:
                print(err)
                print(f'one of more coordinates is not valid for coordinate pair ({co[0]}, {co[1]})')

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                neighbors = self.get_neighbors([i, j])
                if cell == 0:
                    self.dead_change((i, j), neighbors)
                elif cell == 1:
                    self.live_change((i, j), neighbors)

    def get_neighbors(self, coord: list[int]) -> list[int]:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        neighbors = []
        rows = len(self.grid)
        cols = len(self.grid[0])

        for x, y in directions:
            nx, ny = coord[0] + x, coord[1] + y
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append(self.grid[nx][ny])

        return neighbors

    def dead_change(self, cell_coord: tuple[int, int], neighbor_vals: list[int]):
        if sum(neighbor_vals) == 3:
            self.grid[cell_coord[1]][cell_coord[0]] = 1

    def live_change(self, cell_coord: tuple[int, int], neighbor_vals: list[int]):
        live_or_dead: int = 0
        if sum(neighbor_vals) <= 1:
            live_or_dead = 0
        elif sum(neighbor_vals) >= 4:
            live_or_dead = 0
        elif sum(neighbor_vals) in range(2, 4):
            live_or_dead = 1

        self.grid[cell_coord[1]][cell_coord[0]] = live_or_dead

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        for _ in range(n):
            self.make_step()

    def draw_grid(self):
        # Draw the current state of the grid.
        pass

