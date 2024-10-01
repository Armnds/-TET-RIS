from shapely.geometry import Polygon, Point
from shapely.affinity import translate, rotate
import matplotlib.pyplot as plt
import random

class BinPacking2D:
    def __init__(self, bin_width, bin_height):
        self.bin_width = bin_width
        self.bin_height = bin_height
        self.bin = Polygon([(0, 0), (bin_width, 0), (bin_width, bin_height), (0, bin_height)])
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
        for _ in range(max_attempts):
            # Generate a random position within the bin bounds
            x_pos = random.uniform(0, self.bin_width)
            y_pos = random.uniform(0, self.bin_height)

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
        
        ax.set_xlim(0, self.bin_width)
        ax.set_ylim(0, self.bin_height)
        ax.set_aspect('equal')
        plt.show()

# Example shapes (irregular polygons)
polygon1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 1)])  # L-shaped
polygon2 = Polygon([(0, 0), (3, 0), (3, 1), (0, 1)])  # Rectangle
polygon3 = Polygon([(0, 0), (1, 0), (1, 3), (0, 2)])

polygon4 = Polygon([(0, 0), (3, 0), (3, 1), (0, 1)])
polygon5 = Polygon([(0, 0), (3, 0), (3, 1), (0, 1)])  # Vertical Rectangle
polygon6 = Polygon([(0, 0), (3, 0), (3, 1), (0, 1)])

# Initialize the bin (10x10)
bin_packer = BinPacking2D(10, 3)

# Try to pack the polygons

bin_packer.pack_polygon(polygon1)
bin_packer.pack_polygon(polygon2)
bin_packer.pack_polygon(polygon3)
bin_packer.pack_polygon(polygon4)
bin_packer.pack_polygon(polygon5)
bin_packer.pack_polygon(polygon6)


# Visualize the result
bin_packer.visualize()
