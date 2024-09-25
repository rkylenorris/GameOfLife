class GameOfLife(object):

    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.grid = [[0] * x_dim for _ in range(y_dim)]

    def get_grid(self):
        # Implement a getter method for your grid.
        return self.grid

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        for row in self.grid:
            print(row)

    def populate_grid(self, coord):
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        pass

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        pass

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        pass

    def draw_grid(self):
        # Draw the current state of the grid.
        pass

