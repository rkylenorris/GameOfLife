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

    def populate_grid(self, coord: list[tuple]):
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
        pass

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        pass

    def draw_grid(self):
        # Draw the current state of the grid.
        pass

