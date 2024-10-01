# # # # import matplotlib.pyplot as plt
# # # # from shapely.geometry import Polygon
# # # # from shapely.affinity import translate
# # # # import cv2

# # # # def read_polygon_from_image(path):
# # # #     # Read the image
# # # #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# # # #     # Detect the edges
# # # #     contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # # #     # Extract the largest contour
# # # #     contour = max(contours, key=cv2.contourArea)
# # # #     # Convert to a Shapely polygon
# # # #     poly = Polygon(contour.squeeze())
# # # #     return poly

# # # # def generate_nfp(poly1, poly2):
# # # #     # Calculate the no-fit polygon by moving poly2 around poly1
# # # #     nfp = []
# # # #     for x, y in poly2.exterior.coords:
# # # #         translated = translate(poly1, xoff=x, yoff=y)
# # # #         nfp.append(translated)
# # # #     return nfp

# # # # def find_optimal_position(poly1, poly2):
# # # #     # This is a simple placeholder for finding the optimal position
# # # #     # You can replace it with more complex algorithms like genetic algorithms
# # # #     nfp = generate_nfp(poly1, poly2)
# # # #     min_distance = float('inf')
# # # #     optimal_position = None
    
# # # #     for candidate in nfp:
# # # #         distance = poly1.distance(candidate)
# # # #         if distance < min_distance:
# # # #             min_distance = distance
# # # #             optimal_position = candidate
    
# # # #     return optimal_position

# # # # def plot_polygons(poly1, poly2, output_path):
# # # #     fig, ax = plt.subplots()
# # # # #     x1, y1 = poly1.exterior.xy
# # # # #     ax.plot(x1, y1, color='blue')

# # # # #     x2, y2 = poly2.exterior.xy
# # # # #     ax.plot(x2, y2, color='red')

# # # # #     plt.savefig(output_path)

# # # # # def main():
# # # # #     # Define the paths of the images for polygons
# # # # #     poly1_path = input("Enter the path for the first polygon image: ")
# # # # #     poly2_path = input("Enter the path for the second polygon image: ")
# # # # #     output_path = input("Enter the path for the output image: ")

# # # # #     poly1 = read_polygon_from_image(poly1_path)
# # # # #     poly2 = read_polygon_from_image(poly2_path)
# # # # #     optimal_poly2 = find_optimal_position(poly1, poly2)
# # # # #     plot_polygons(poly1, optimal_poly2, output_path)

# # # # # if __name__ == "__main__":
# # # # #     main()


# # # # import matplotlib.pyplot as plt
# # # # from shapely.geometry import Polygon
# # # # from shapely.affinity import translate
# # # # import cv2

# # # # def read_polygon_from_image(path):
# # # #     # Read the image
# # # #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# # # #     # Detect the edges
# # # #     contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # # #     # Extract the largest contour
# # # #     contour = max(contours, key=cv2.contourArea)
# # # #     # Convert to a Shapely polygon
# # # #     poly = Polygon(contour.squeeze())
# # # #     return poly

# # # # def generate_nfp(poly1, poly2):
# # # #     # Calculate the no-fit polygon by moving poly2 around poly1
# # # #     nfp = []
# # # #     for x, y in poly2.exterior.coords:
# # # #         translated = translate(poly1, xoff=x, yoff=y)
# # # #         nfp.append(translated)
# # # #     return nfp

# # # # def find_optimal_position(poly1, poly2):
# # # #     # This is a simple placeholder for finding the optimal position
# # # #     # You can replace it with more complex algorithms like genetic algorithms
# # # #     nfp = generate_nfp(poly1, poly2)
# # # #     min_distance = float('inf')
# # # #     optimal_position = None
    
# # # #     for candidate in nfp:
# # # #         distance = poly1.distance(candidate)
# # # #         if distance < min_distance:
# # # #             min_distance = distance
# # # #             optimal_position = candidate
    
# # # #     return optimal_position

# # # # def arrange_polygons(polygons):
# # # #     positioned_polygons = [polygons[0]]
    
# # # #     for poly in polygons[1:]:
# # # #         last_poly = positioned_polygons[-1]
# # # #         optimal_poly = find_optimal_position(last_poly, poly)
# # # #         positioned_polygons.append(optimal_poly)
    
# # # #     return positioned_polygons

# # # # def plot_polygons(polygons, output_path):
# # # #     fig, ax = plt.subplots()
    
# # # #     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
# # # #     for i, poly in enumerate(polygons):
# # # #         x, y = poly.exterior.xy
# # # #         ax.plot(x, y, color=colors[i % len(colors)])

# # # #     plt.savefig(output_path)

# # # # def main():
# # # #     num_polygons = int(input("Enter the number of polygon images: "))
# # # #     polygon_paths = [input(f"Enter the path for polygon image {i+1}: ") for i in range(num_polygons)]
# # # #     output_path = input("Enter the path for the output image: ")

# # # #     polygons = [read_polygon_from_image(path) for path in polygon_paths]
# # # #     positioned_polygons = arrange_polygons(polygons)
# # # #     plot_polygons(positioned_polygons, output_path)

# # # # if __name__ == "__main__":
# # # #     main()


# # # import matplotlib.pyplot as plt
# # # from shapely.geometry import Polygon
# # # from shapely.affinity import translate
# # # import cv2

# # # def read_polygon_from_image(path):
# # #     # Read the image
# # #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# # #     if img is None:
# # #         raise ValueError(f"Image at path {path} could not be read.")
    
# # #     # Detect the edges
# # #     contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# # #     # Extract the largest contour that has at least 4 points
# # #     contour = max(contours, key=cv2.contourArea, default=None)
# # #     if contour is None or len(contour) < 4:
# # #         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
# # #     # Convert to a Shapely polygon
# # #     poly = Polygon(contour.squeeze())
# # #     if not poly.is_valid:
# # #         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
# # #     return poly

# # # def generate_nfp(poly1, poly2):
# # #     # Calculate the no-fit polygon by moving poly2 around poly1
# # #     nfp = []
# # #     for x, y in poly2.exterior.coords:
# # #         translated = translate(poly1, xoff=x, yoff=y)
# # #         nfp.append(translated)
# # #     return nfp

# # # def find_optimal_position(poly1, poly2):
# # #     # This is a simple placeholder for finding the optimal position
# # #     # You can replace it with more complex algorithms like genetic algorithms
# # #     nfp = generate_nfp(poly1, poly2)
# # #     min_distance = float('inf')
# # #     optimal_position = None
    
# # #     for candidate in nfp:
# # #         distance = poly1.distance(candidate)
# # #         if distance < min_distance:
# # #             min_distance = distance
# # #             optimal_position = candidate
    
# # #     return optimal_position

# # # def arrange_polygons(polygons):
# # #     positioned_polygons = [polygons[0]]
    
# # #     for poly in polygons[1:]:
# # #         last_poly = positioned_polygons[-1]
# # #         optimal_poly = find_optimal_position(last_poly, poly)
# # #         positioned_polygons.append(optimal_poly)
    
# # #     return positioned_polygons

# # # def plot_polygons(polygons, output_path):
# # #     fig, ax = plt.subplots()
    
# # #     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
# # #     for i, poly in enumerate(polygons):
# # #         x, y = poly.exterior.xy
# # #         ax.plot(x, y, color=colors[i % len(colors)])

# # #     plt.savefig(output_path)

# # # def main():
# # #     num_polygons = int(input("Enter the number of polygon images: "))
# # #     polygon_paths = [input(f"Enter the path for polygon image {i+1}: ") for i in range(num_polygons)]
# # #     output_path = input("Enter the path for the output image: ")

# # #     polygons = [read_polygon_from_image(path) for path in polygon_paths]
# # #     positioned_polygons = arrange_polygons(polygons)
# # #     plot_polygons(positioned_polygons, output_path)

# # # if __name__ == "__main__":
# # #     main()

# # import matplotlib.pyplot as plt
# # from shapely.geometry import Polygon
# # from shapely.affinity import translate
# # import cv2
# # import numpy as np

# # def read_polygon_from_image(path):
# #     # Read the image
# #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# #     if img is None:
# #         raise ValueError(f"Image at path {path} could not be read.")
    
# #     # Invert the image so the black areas become white
# #     img_inverted = cv2.bitwise_not(img)
    
# #     # Detect the edges
# #     contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# #     # Extract the largest contour that has at least 4 points
# #     contour = max(contours, key=cv2.contourArea, default=None)
# #     if contour is None or len(contour) < 4:
# #         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
# #     # Convert to a Shapely polygon
# #     poly = Polygon(contour.squeeze())
# #     if not poly.is_valid:
# #         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
# #     return poly

# # def generate_nfp(poly1, poly2):
# #     # Calculate the no-fit polygon by moving poly2 around poly1
# #     nfp = []
# #     for x, y in poly2.exterior.coords:
# #         translated = translate(poly1, xoff=x, yoff=y)
# #         nfp.append(translated)
# #     return nfp

# # def find_optimal_position(poly1, poly2):
# #     # This is a simple placeholder for finding the optimal position
# #     # You can replace it with more complex algorithms like genetic algorithms
# #     nfp = generate_nfp(poly1, poly2)
# #     min_distance = float('inf')
# #     optimal_position = None
    
# #     for candidate in nfp:
# #         distance = poly1.distance(candidate)
# #         if distance < min_distance:
# #             min_distance = distance
# #             optimal_position = candidate
    
# #     return optimal_position

# # def arrange_polygons(polygons):
# #     positioned_polygons = [polygons[0]]
    
# #     for poly in polygons[1:]:
# #         last_poly = positioned_polygons[-1]
# #         optimal_poly = find_optimal_position(last_poly, poly)
# #         positioned_polygons.append(optimal_poly)
    
# #     return positioned_polygons

# # def plot_polygons(polygons, output_path):
# #     fig, ax = plt.subplots()
    
# #     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
# #     for i, poly in enumerate(polygons):
# #         x, y = poly.exterior.xy
# #         ax.plot(x, y, color=colors[i % len(colors)])

# #     plt.savefig(output_path)

# # def main():
# #     num_polygons = int(input("Enter the number of polygon images: "))
# #     polygon_paths = [input(f"Enter the path for polygon image {i+1}: ") for i in range(num_polygons)]
# #     output_path = input("Enter the path for the output image: ")

# #     polygons = [read_polygon_from_image(path) for path in polygon_paths]
# #     positioned_polygons = arrange_polygons(polygons)
# #     plot_polygons(positioned_polygons, output_path)

# # if __name__ == "__main__":
# #     main()


# import matplotlib.pyplot as plt
# from shapely.geometry import Polygon
# from shapely.affinity import translate
# import cv2
# import numpy as np
# import random

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

# def generate_nfp(poly1, poly2):
#     # Calculate the no-fit polygon by moving poly2 around poly1
#     nfp = []
#     for x, y in poly2.exterior.coords:
#         translated = translate(poly1, xoff=x, yoff=y)
#         nfp.append(translated)
#     return nfp

# def find_optimal_position(poly1, poly2):
#     # This is a simple placeholder for finding the optimal position
#     # You can replace it with more complex algorithms like genetic algorithms
#     nfp = generate_nfp(poly1, poly2)
#     min_distance = float('inf')
#     optimal_position = None
    
#     for candidate in nfp:
#         distance = poly1.distance(candidate)
#         if distance < min_distance:
#             min_distance = distance
#             optimal_position = candidate
    
#     return optimal_position

# def arrange_polygons(polygons):
#     positioned_polygons = [polygons[0]]
    
#     for poly in polygons[1:]:
#         last_poly = positioned_polygons[-1]
#         optimal_poly = find_optimal_position(last_poly, poly)
#         positioned_polygons.append(optimal_poly)
    
#     return positioned_polygons

# def check_collision(poly, other_polys):
#     for other in other_polys:
#         if poly.intersects(other):
#             return True
#     return False

# def arrange_polygons_without_collision(polygons):
#     positioned_polygons = [polygons[0]]
    
#     for poly in polygons[1:]:
#         position_found = False
#         attempts = 0
#         max_attempts = 1000
#         while not position_found and attempts < max_attempts:
#             attempts += 1
#             # Generate a random translation
#             xoff = random.uniform(-100, 100)
#             yoff = random.uniform(-100, 100)
#             translated_poly = translate(poly, xoff=xoff, yoff=yoff)
#             if not check_collision(translated_poly, positioned_polygons):
#                 positioned_polygons.append(translated_poly)
#                 position_found = True
        
#         if not position_found:
#             raise RuntimeError("Could not find a valid position for the polygon without collision.")
    
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


import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.affinity import translate
import cv2
import numpy as np

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
# image_folder = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\shapes"
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
    num_polygons = int(input("Enter the number of polygon images: "))
    polygon_paths = [input(f"Enter the path for polygon image {i+1}: ") for i in range(num_polygons)]
    output_path = input("Enter the path for the output image: ")

    polygons = [read_polygon_from_image(path) for path in polygon_paths]
    positioned_polygons = arrange_polygons_without_collision(polygons)
    plot_polygons(positioned_polygons, output_path)

if __name__ == "__main__":
    main()

#fuck you

