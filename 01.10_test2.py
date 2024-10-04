
# import matplotlib.pyplot as plt
# from shapely.geometry import Polygon
# from shapely.affinity import translate
# import cv2
# import numpy as np

# def read_polygon_from_image(path):
#     # Read the image
#     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#     if img is None:
#         raise ValueError(f"Image at path {path} could not be read.")
    
#     # Invert the image so the black areas become white
#     img_inverted = cv2.bitwise_not(img)
    
#     # Detect the edges
#     contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Extract the largest contour that has at least 4 points
#     contour = max(contours, key=cv2.contourArea, default=None)
#     if contour is None or len(contour) < 4:
#         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
#     # Convert to a Shapely polygon
#     poly = Polygon(contour.squeeze())
#     if not poly.is_valid:
#         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
#     return poly

# def check_collision(poly, other_polys):
#     for other in other_polys:
#         if poly.intersects(other):
#             return True
#     return False
# # image_folder = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\shapes"
# def arrange_polygons_without_collision(polygons):
#     positioned_polygons = [polygons[0]]
#     grid_spacing = 10  # Define the grid spacing for the placement attempts

#     for poly in polygons[1:]:
#         position_found = False
#         x_offset, y_offset = 0, 0
#         max_range = 100  # Initial max range for search

#         while not position_found:
#             # Try to place the polygon in a grid pattern within the max range
#             for dx in range(-max_range, max_range + 1, grid_spacing):
#                 for dy in range(-max_range, max_range + 1, grid_spacing):
#                     translated_poly = translate(poly, xoff=dx, yoff=dy)
#                     if not check_collision(translated_poly, positioned_polygons):
#                         positioned_polygons.append(translated_poly)
#                         position_found = True
#                         break
#                 if position_found:
#                     break
#             # If no position found within max range, expand the search range
#             if not position_found:
#                 max_range += 100

#     return positioned_polygons

# def plot_polygons(polygons, output_path):
#     fig, ax = plt.subplots()
    
#     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
#     for i, poly in enumerate(polygons):
#         x, y = poly.exterior.xy
#         ax.plot(x, y, color=colors[i % len(colors)])

#     plt.savefig(output_path)

# def main():
#     num_polygons = int(input("Enter the number of polygon images: "))
#     polygon_paths = [input(f"Enter the path for polygon image {i+1}: ") for i in range(num_polygons)]
#     output_path = input("Enter the path for the output image: ")

#     polygons = [read_polygon_from_image(path) for path in polygon_paths]
#     positioned_polygons = arrange_polygons_without_collision(polygons)
#     plot_polygons(positioned_polygons, output_path)

# if __name__ == "__main__":
#     main()
    

import os
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.affinity import translate
import cv2
import numpy as np

# Hardcoded paths
FOLDER_PATH = r"C:\Users\Armand\OneDrive - Delft University of Technology\Uni\Masters\CORE\02.10 shapes"
OUTPUT_PATH = r"C:\Users\Armand\OneDrive - Delft University of Technology\Uni\Masters\CORE\OUTPUT"

def read_polygon_from_image(path):
    # Read the image
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image at path {path} could not be read.")
    
    # Invert the image so the black areas become white
    img_inverted = cv2.bitwise_not(img)
    
    # Detect the edges
    contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Extract the largest contour that has at least 4 points
    contour = max(contours, key=cv2.contourArea, default=None)
    if contour is None or len(contour) < 4:
        raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
    # Convert to a Shapely polygon
    poly = Polygon(contour.squeeze())
    if not poly.is_valid:
        raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
    return poly

def check_collision(poly, other_polys):
    for other in other_polys:
        if poly.intersects(other):
            return True
    return False

def arrange_polygons_without_collision(polygons):
    positioned_polygons = [polygons[0]]
    grid_spacing = 10  # Define the grid spacing for the placement attempts

    for poly in polygons[1:]:
        position_found = False
        x_offset, y_offset = 0, 0
        max_range = 100  # Initial max range for search

        while not position_found:
            # Try to place the polygon in a grid pattern within the max range
            for dx in range(-max_range, max_range + 1, grid_spacing):
                for dy in range(-max_range, max_range + 1, grid_spacing):
                    translated_poly = translate(poly, xoff=dx, yoff=dy)
                    if not check_collision(translated_poly, positioned_polygons):
                        positioned_polygons.append(translated_poly)
                        position_found = True
                        break
                if position_found:
                    break
            # If no position found within max range, expand the search range
            if not position_found:
                max_range += 100

    return positioned_polygons

def plot_polygons(polygons, output_path):
    fig, ax = plt.subplots()
    
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
    for i, poly in enumerate(polygons):
        x, y = poly.exterior.xy
        ax.plot(x, y, color=colors[i % len(colors)])

    plt.savefig(output_path)

def main():
    # List all files in the folder
    valid_extensions = ['.png', '.jpg', '.jpeg']
    polygon_paths = [
        os.path.join(FOLDER_PATH, filename)
        for filename in os.listdir(FOLDER_PATH)
        if os.path.splitext(filename)[1].lower() in valid_extensions
    ]

    print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

    polygons = [read_polygon_from_image(path) for path in polygon_paths]
    positioned_polygons = arrange_polygons_without_collision(polygons)
    plot_polygons(positioned_polygons, OUTPUT_PATH)
    print(f"Output image saved to '{OUTPUT_PATH}'")

if __name__ == "__main__":
    main()