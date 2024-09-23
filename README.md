# Game of Life
### Author: R. Kyle Norris


A capstone project for https://learn.365datascience.com/ Python Bootcamp course,
found at 
https://learn.365datascience.com/projects/building-conway-s-game-of-life-in-python/

## Description from project page:

>In this Building Conway's Game of Life in Python project, you get to implement 
a simulation of the Game of Life, invented by mathematician John Horton Conway. 
It’s an excellent opportunity to apply your programming skills in 
Python while exploring fascinating concepts in cellular automata, 
emergence, and complexity theory.

>Conway’s Game of Life is a zero-player game requiring only an initial state 
and no further input. In its original setting, the game takes place on an 
infinite grid of square cells, each in one of two possible states: live or dead. 
Every cell interacts with its eight neighbors (horizontally, vertically, or 
diagonally adjacent cells). Starting at the initial state, the game evolves 
according to the following rules:

>Any live cell with two or three live neighbors survives. 
Otherwise, a cell dies due to loneliness (with no or only one neighbor) or 
overpopulation (with four or more neighbors).
Any dead cell with (exactly) three live neighbors becomes a live cell. 
A dead cell with any other number of neighbors remains dead.
In this project, we restrict the infinite grid to one with finite pre-defined 
dimensions.

>Despite its simplicity, the Game of Life has the power to create complex 
behaviors, which have implications for all fields—from physics and 
mathematics to philosophy and art.


## Code Provided to start:

Found in skeleton_code directory,it's the basic structure of a class
called GameOfLife:

    class GameOfLife(object):  
        
        def __init__(self, x_dim, y_dim):
            # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
            pass
        
        def get_grid(self):
            # Implement a getter method for your grid.
            pass
    
        def print_grid(self):
            # Implement a method to print out your grid in a human-readable format.
            pass
    
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