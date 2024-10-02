from shapely.geometry import Polygon, Point
from shapely.affinity import translate, rotate
import matplotlib.pyplot as plt
import random

class BinPacking2D:
    def __init__(self, bin_polygon):
        self.bin = bin_polygon
        self.placed_polygons = []

    def can_place_polygon(self, poly, position):
        """ Check if a polygon can be placed at a certain position without overlapping other polygons """
        # Translate the polygon to the new position
        translated_poly = translate(poly, xoff=position[0], yoff=position[1])

        # Check if the translated polygon is within the bin
        if not self.bin.contains(translated_poly):
            return False

        # Check for overlap with already placed polygons
        for placed_poly in self.placed_polygons:
            if translated_poly.intersects(placed_poly):
                return False

        return True

    def place_polygon(self, poly, position):
        """ Place a polygon at the given position if possible """
        if self.can_place_polygon(poly, position):
            translated_poly = translate(poly, xoff=position[0], yoff=position[1])
            self.placed_polygons.append(translated_poly)
            return True
        return False

    def pack_polygon(self, poly, max_attempts=1000):
        """ Try to pack a polygon within the bin by randomly selecting positions """
        min_x, min_y, max_x, max_y = self.bin.bounds

        for _ in range(max_attempts):
            # Generate a random position within the bounding box of the bin
            x_pos = random.uniform(min_x, max_x)
            y_pos = random.uniform(min_y, max_y)

            if self.place_polygon(poly, (x_pos, y_pos)):
                return True
        return False

    def visualize(self):
        """ Visualize the bin and placed polygons using Matplotlib """
        fig, ax = plt.subplots()
        
        # Plot the bin
        bin_patch = plt.Polygon(list(self.bin.exterior.coords), fill=None, edgecolor='black')
        ax.add_patch(bin_patch)
        
        # Plot each placed polygon
        for poly in self.placed_polygons:
            patch = plt.Polygon(list(poly.exterior.coords), fill=True, edgecolor='blue', alpha=0.5)
            ax.add_patch(patch)
        
        ax.set_xlim(self.bin.bounds[0], self.bin.bounds[2])
        ax.set_ylim(self.bin.bounds[1], self.bin.bounds[3])
        ax.set_aspect('equal')
        plt.show()

# Example irregular bin (hexagonal shape)
irregular_bin = Polygon([(0, 0), (5, 0), (10, 3), (12, 20), (3, 5), (0, 3)])

# Example irregular polygons
polygons = []  # List to store the polygons
materials = 20
random_integer = random.randint(1, 10)

for i in range(materials):
    polygon = Polygon([(0, 0), (random.randint(1, 10), random.randint(1, 10)), (random.randint(1, 10),random.randint(1, 10)), (2, 1)])  # Create the same polygon
    polygons.append(polygon)  # Add the polygon to the list
  # L-shaped #HOW TO MAKE MULTIPLE POLYGONS EASILY

#polygon2 = Polygon([(0, 0), (3, 0), (3, 1), (0, 1)])  # Rectangle


# Initialize the bin with an irregular shape
bin_packer = BinPacking2D(irregular_bin)

# Try to pack the polygons
for i in range(materials):
    bin_packer.pack_polygon(polygons[i])


#bin_packer.pack_polygon(polygon1)


# Visualize the result
bin_packer.visualize()
