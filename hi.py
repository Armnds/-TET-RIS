import random
import numpy as np

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shape_grid = np.ones((height, width))  # 1s represent the filled shape

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))  # 0s represent empty space

    def can_place_shape(self, shape, x, y):
        """ Check if the shape can be placed at position (x, y) without overlap. """
        if x + shape.width > self.width or y + shape.height > self.height:
            return False
        
        # Check if there is overlap
        for i in range(shape.height):
            for j in range(shape.width):
                if self.grid[y + i][x + j] != 0 and shape.shape_grid[i][j] != 0:
                    return False
        return True

    def place_shape(self, shape, x, y):
        """ Place the shape in the grid, allowing overlaps. """
        for i in range(shape.height):
            for j in range(shape.width):
                if shape.shape_grid[i][j] == 1:
                    self.grid[y + i][x + j] = 1  # Mark as occupied

    def calculate_filled_percentage(self):
        """ Calculate the percentage of the grid that is filled. """
        return np.sum(self.grid) / (self.width * self.height) * 100

    def print_grid(self):
        """ Print the grid for visualization. """
        for row in self.grid:
            print(' '.join(str(int(cell)) for cell in row))

# Example usage
larger_shape = Grid(10, 10)  # A 10x10 grid representing the larger shape

# Randomly generate smaller shapes
random_shapes = [Shape(random.randint(1, 4), random.randint(1, 4)) for _ in range(20)]

# Try to place the shapes into the larger grid
for shape in random_shapes:
    placed = False
    for y in range(larger_shape.height):
        for x in range(larger_shape.width):
            if larger_shape.can_place_shape(shape, x, y):
                larger_shape.place_shape(shape, x, y)
                placed = True
                break
        if placed:
            break

# Print the grid and show how much of the area is filled
larger_shape.print_grid()
print(f"Filled percentage: {larger_shape.calculate_filled_percentage():.2f}%")
