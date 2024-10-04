
# # # # # import matplotlib.pyplot as plt
# # # # # from shapely.geometry import Polygon
# # # # # from shapely.affinity import translate
# # # # # import cv2
# # # # # import numpy as np

# # # # # def read_polygon_from_image(path):
# # # # #     # Read the image
# # # # #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# # # # #     if img is None:
# # # # #         raise ValueError(f"Image at path {path} could not be read.")
    
# # # # #     # Invert the image so the black areas become white
# # # # #     img_inverted = cv2.bitwise_not(img)
    
# # # # #     # Detect the edges
# # # # #     contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# # # # #     # Extract the largest contour that has at least 4 points
# # # # #     contour = max(contours, key=cv2.contourArea, default=None)
# # # # #     if contour is None or len(contour) < 4:
# # # # #         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
# # # # #     # Convert to a Shapely polygon
# # # # #     poly = Polygon(contour.squeeze())
# # # # #     if not poly.is_valid:
# # # # #         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
# # # # #     return poly

# # # # # def check_collision(poly, other_polys):
# # # # #     for other in other_polys:
# # # # #         if poly.intersects(other):
# # # # #             return True
# # # # #     return False
# # # # # # image_folder = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\shapes"
# # # # # def arrange_polygons_without_collision(polygons):
# # # # #     positioned_polygons = [polygons[0]]
# # # # #     grid_spacing = 10  # Define the grid spacing for the placement attempts

# # # # #     for poly in polygons[1:]:
# # # # #         position_found = False
# # # # #         x_offset, y_offset = 0, 0
# # # # #         max_range = 100  # Initial max range for search

# # # # #         while not position_found:
# # # # #             # Try to place the polygon in a grid pattern within the max range
# # # # #             for dx in range(-max_range, max_range + 1, grid_spacing):
# # # # #                 for dy in range(-max_range, max_range + 1, grid_spacing):
# # # # #                     translated_poly = translate(poly, xoff=dx, yoff=dy)
# # # # #                     if not check_collision(translated_poly, positioned_polygons):
# # # # #                         positioned_polygons.append(translated_poly)
# # # # #                         position_found = True
# # # # #                         break
# # # # #                 if position_found:
# # # # #                     break
# # # # #             # If no position found within max range, expand the search range
# # # # #             if not position_found:
# # # # #                 max_range += 100

# # # # #     return positioned_polygons

# # # # # def plot_polygons(polygons, output_path):
# # # # #     fig, ax = plt.subplots()
    
# # # # #     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
# # # # #     for i, poly in enumerate(polygons):
# # # # #         x, y = poly.exterior.xy
# # # # #         ax.plot(x, y, color=colors[i % len(colors)])

# # # # #     plt.savefig(output_path)

# # # # # def main():
# # # # #     num_polygons = int(input("Enter the number of polygon images: "))
# # # # #     polygon_paths = [input(f"Enter the path for polygon image {i+1}: ") for i in range(num_polygons)]
# # # # #     output_path = input("Enter the path for the output image: ")

# # # # #     polygons = [read_polygon_from_image(path) for path in polygon_paths]
# # # # #     positioned_polygons = arrange_polygons_without_collision(polygons)
# # # # #     plot_polygons(positioned_polygons, output_path)

# # # # # if __name__ == "__main__":
# # # # #     main()
    

# # # # import os
# # # # import matplotlib.pyplot as plt
# # # # from shapely.geometry import Polygon
# # # # from shapely.affinity import translate
# # # # import cv2
# # # # import numpy as np

# # # # # Hardcoded paths
# # # # FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\irregular shapes 3"
# # # # OUTPUT_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons\outcome_vers11.png"

# # # # def read_polygon_from_image(path):
# # # #     # Read the image
# # # #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# # # #     if img is None:
# # # #         raise ValueError(f"Image at path {path} could not be read.")
    
# # # #     # Invert the image so the black areas become white
# # # #     img_inverted = cv2.bitwise_not(img)
    
# # # #     # Detect the edges
# # # #     contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# # # #     # Extract the largest contour that has at least 4 points
# # # #     contour = max(contours, key=cv2.contourArea, default=None)
# # # #     if contour is None or len(contour) < 4:
# # # #         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
# # # #     # Convert to a Shapely polygon
# # # #     poly = Polygon(contour.squeeze())
# # # #     if not poly.is_valid:
# # # #         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
# # # #     return poly

# # # # def check_collision(poly, other_polys):
# # # #     for other in other_polys:
# # # #         if poly.intersects(other):
# # # #             return True
# # # #     return False

# # # # def arrange_polygons_without_collision(polygons):
# # # #     positioned_polygons = [polygons[0]]
# # # #     grid_spacing = 10  # Define the grid spacing for the placement attempts

# # # #     for poly in polygons[1:]:
# # # #         position_found = False
# # # #         x_offset, y_offset = 0, 0
# # # #         max_range = 100  # Initial max range for search

# # # #         while not position_found:
# # # #             # Try to place the polygon in a grid pattern within the max range
# # # #             for dx in range(-max_range, max_range + 1, grid_spacing):
# # # #                 for dy in range(-max_range, max_range + 1, grid_spacing):
# # # #                     translated_poly = translate(poly, xoff=dx, yoff=dy)
# # # #                     if not check_collision(translated_poly, positioned_polygons):
# # # #                         positioned_polygons.append(translated_poly)
# # # #                         position_found = True
# # # #                         break
# # # #                 if position_found:
# # # #                     break
# # # #             # If no position found within max range, expand the search range
# # # #             if not position_found:
# # # #                 max_range += 100

# # # #     return positioned_polygons

# # # # def plot_polygons(polygons, output_path):
# # # #     fig, ax = plt.subplots()
    
# # # #     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
# # # #     for i, poly in enumerate(polygons):
# # # #         x, y = poly.exterior.xy
# # # #         ax.plot(x, y, color=colors[i % len(colors)])

# # # #     plt.savefig(output_path)

# # # # def main():
# # # #     # List all files in the folder
# # # #     valid_extensions = ['.png', '.jpg', '.jpeg']
# # # #     polygon_paths = [
# # # #         os.path.join(FOLDER_PATH, filename)
# # # #         for filename in os.listdir(FOLDER_PATH)
# # # #         if os.path.splitext(filename)[1].lower() in valid_extensions
# # # #     ]

# # # #     print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

# # # #     polygons = [read_polygon_from_image(path) for path in polygon_paths]
# # # #     positioned_polygons = arrange_polygons_without_collision(polygons)
# # # #     plot_polygons(positioned_polygons, OUTPUT_PATH)
# # # #     print(f"Output image saved to '{OUTPUT_PATH}'")

# # # # if __name__ == "__main__":
# # # #     main()

# # # import os
# # # import matplotlib.pyplot as plt
# # # from shapely.geometry import Polygon
# # # from shapely.affinity import translate
# # # import cv2
# # # import numpy as np

# # # # Hardcoded paths
# # # FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\irregular shapes 2"
# # # FRAME_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\frame_01.png"  # Path to the frame image
# # # OUTPUT_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons\outcome_vers11.png"

# # # def read_polygon_from_image(path):
# # #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# # #     if img is None:
# # #         raise ValueError(f"Image at path {path} could not be read.")
    
# # #     img_inverted = cv2.bitwise_not(img)
    
# # #     contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# # #     contour = max(contours, key=cv2.contourArea, default=None)
# # #     if contour is None or len(contour) < 4:
# # #         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
# # #     poly = Polygon(contour.squeeze())
# # #     if not poly.is_valid:
# # #         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
# # #     return poly

# # # def check_collision(poly, other_polys):
# # #     for other in other_polys:
# # #         if poly.intersects(other):
# # #             return True
# # #     return False

# # # def arrange_polygons_within_frame(polygons, frame):
# # #     positioned_polygons = []
# # #     grid_spacing = 10

# # #     for poly in polygons:
# # #         position_found = False
# # #         x_offset, y_offset = 0, 0
# # #         max_range = 100

# # #         while not position_found:
# # #             for dx in range(-max_range, max_range + 1, grid_spacing):
# # #                 for dy in range(-max_range, max_range + 1, grid_spacing):
# # #                     translated_poly = translate(poly, xoff=dx, yoff=dy)
# # #                     if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
# # #                         positioned_polygons.append(translated_poly)
# # #                         position_found = True
# # #                         break
# # #                 if position_found:
# # #                     break
# # #             if not position_found:
# # #                 max_range += 100
# # #                 if max_range > 5000:  # Prevent infinite loop
# # #                     raise RuntimeError("Could not place a polygon inside the frame without collision.")
    
# # #     return positioned_polygons

# # # def plot_polygons(polygons, output_path):
# # #     fig, ax = plt.subplots()
    
# # #     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
# # #     for i, poly in enumerate(polygons):
# # #         x, y = poly.exterior.xy
# # #         ax.plot(x, y, color=colors[i % len(colors)])
    
# # #     plt.savefig(output_path)

# # # def main():
# # #     valid_extensions = ['.png', '.jpg', '.jpeg']
# # #     polygon_paths = [
# # #         os.path.join(FOLDER_PATH, filename)
# # #         for filename in os.listdir(FOLDER_PATH)
# # #         if os.path.splitext(filename)[1].lower() in valid_extensions
# # #     ]

# # #     print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

# # #     frame_polygon = read_polygon_from_image(FRAME_PATH)
# # #     polygons = [read_polygon_from_image(path) for path in polygon_paths]
# # #     positioned_polygons = arrange_polygons_within_frame(polygons, frame_polygon)
# # #     plot_polygons(positioned_polygons, OUTPUT_PATH)
# # #     print(f"Output image saved to '{OUTPUT_PATH}'")

# # # if __name__ == "__main__":
# # #     main()

# # import os
# # import matplotlib.pyplot as plt
# # from shapely.geometry import Polygon
# # from shapely.affinity import translate
# # import cv2
# # import numpy as np

# # # Hardcoded paths
# # FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\irregular shapes 4"
# # FRAME_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\frame_03.png"
# # OUTPUT_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons\outcome_vers13.png"
# # UNFIT_FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\unfit_polygons"

# # def read_polygon_from_image(path):
# #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# #     if img is None:
# #         raise ValueError(f"Image at path {path} could not be read.")
    
# #     img_inverted = cv2.bitwise_not(img)
    
# #     contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# #     contour = max(contours, key=cv2.contourArea, default=None)
# #     if contour is None or len(contour) < 4:
# #         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
# #     poly = Polygon(contour.squeeze())
# #     if not poly.is_valid:
# #         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
# #     return poly

# # def check_collision(poly, other_polys):
# #     for other in other_polys:
# #         if poly.intersects(other):
# #             return True
# #     return False

# # def arrange_polygons_within_frame(polygons, frame):
# #     positioned_polygons = []
# #     unfit_polygons = []
# #     grid_spacing = 10

# #     for poly in polygons:
# #         position_found = False
# #         x_offset, y_offset = 0, 0
# #         max_range = 100

# #         while not position_found:
# #             for dx in range(-max_range, max_range + 1, grid_spacing):
# #                 for dy in range(-max_range, max_range + 1, grid_spacing):
# #                     translated_poly = translate(poly, xoff=dx, yoff=dy)
# #                     if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
# #                         positioned_polygons.append(translated_poly)
# #                         position_found = True
# #                         break
# #                 if position_found:
# #                     break
# #             if not position_found:
# #                 max_range += 100
# #                 if max_range > 5000:  # Prevent infinite loop
# #                     unfit_polygons.append(poly)
# #                     break
    
# #     return positioned_polygons, unfit_polygons

# # def plot_polygons(frame, polygons, output_path):
# #     fig, ax = plt.subplots()
    
# #     # Plot the frame polygon
# #     x, y = frame.exterior.xy
# #     ax.plot(x, y, color='black', linewidth=2)  # Frame in black

# #     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
# #     for i, poly in enumerate(polygons):
# #         x, y = poly.exterior.xy
# #         ax.plot(x, y, color=colors[i % len(colors)])

# #     plt.axis('equal')
# #     plt.savefig(output_path)

# # def save_unfit_polygons(unfit_polygons):
# #     if not os.path.exists(UNFIT_FOLDER_PATH):
# #         os.makedirs(UNFIT_FOLDER_PATH)
    
# #     for i, poly in enumerate(unfit_polygons):
# #         # Save the vertices of the unfit polygons as files (e.g., for inspection)
# #         np.savetxt(os.path.join(UNFIT_FOLDER_PATH, f"unfit_polygon_{i}.txt"), np.array(poly.exterior.coords), fmt='%.6f')

# # def main():
# #     valid_extensions = ['.png', '.jpg', '.jpeg']
# #     polygon_paths = [
# #         os.path.join(FOLDER_PATH, filename)
# #         for filename in os.listdir(FOLDER_PATH)
# #         if os.path.splitext(filename)[1].lower() in valid_extensions
# #     ]

# #     print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

# #     frame_polygon = read_polygon_from_image(FRAME_PATH)
# #     polygons = [read_polygon_from_image(path) for path in polygon_paths]
# #     positioned_polygons, unfit_polygons = arrange_polygons_within_frame(polygons, frame_polygon)
# #     plot_polygons(frame_polygon, positioned_polygons, OUTPUT_PATH)
# #     save_unfit_polygons(unfit_polygons)

# #     print(f"Output image saved to '{OUTPUT_PATH}'")
# #     print(f"Unfit polygons saved to '{UNFIT_FOLDER_PATH}'")

# # if __name__ == "__main__":
# #     main()
    


# import os
# import matplotlib.pyplot as plt
# from shapely.geometry import Polygon
# from shapely.affinity import translate
# import cv2
# import numpy as np

# # Hardcoded paths
# FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\irregular shapes 4"
# FRAME_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\frame_03.png"
# OUTPUT_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons\outcome_vers14.png"
# UNFIT_FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\unfit_polygons"

# def read_polygon_from_image(path):
#     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#     if img is None:
#         raise ValueError(f"Image at path {path} could not be read.")
    
#     img_inverted = cv2.bitwise_not(img)
    
#     contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     contour = max(contours, key=cv2.contourArea, default=None)
#     if contour is None or len(contour) < 4:
#         raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
#     poly = Polygon(contour.squeeze())
#     if not poly.is_valid:
#         raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
#     return poly

# def check_collision(poly, other_polys):
#     for other in other_polys:
#         if poly.intersects(other):
#             return True
#     return False

# def arrange_polygons_within_frame(polygons, frame):
#     positioned_polygons = []
#     unfit_polygons = []
#     grid_spacing = 10

#     # Start placement from the bottom-left corner of the frame
#     frame_bounds = frame.bounds
#     start_x, start_y = frame_bounds[0], frame_bounds[1]  # Bottom-left corner of bounding box

#     for poly in polygons:
#         position_found = False
#         max_range = 100

#         while not position_found:
#             for dx in range(0, max_range + 1, grid_spacing):
#                 for dy in range(0, max_range + 1, grid_spacing):
#                     translated_poly = translate(poly, xoff=start_x + dx, yoff=start_y + dy)
#                     if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
#                         positioned_polygons.append(translated_poly)
#                         position_found = True
#                         break
#                 if position_found:
#                     break
#             if not position_found:
#                 max_range += 100
#                 if max_range > 5000:
#                     unfit_polygons.append(poly)
#                     break
    
#     return positioned_polygons, unfit_polygons

# def plot_polygons(frame, polygons, output_path):
#     fig, ax = plt.subplots()
    
#     # Plot the frame polygon
#     x, y = frame.exterior.xy
#     ax.plot(x, y, color='black', linewidth=2)  # Frame in black

#     colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
#     for i, poly in enumerate(polygons):
#         x, y = poly.exterior.xy
#         ax.plot(x, y, color=colors[i % len(colors)])

#     plt.axis('equal')
#     plt.savefig(output_path)

# def save_unfit_polygons(unfit_polygons):
#     if not os.path.exists(UNFIT_FOLDER_PATH):
#         os.makedirs(UNFIT_FOLDER_PATH)
    
#     for i, poly in enumerate(unfit_polygons):
#         np.savetxt(os.path.join(UNFIT_FOLDER_PATH, f"unfit_polygon_{i}.txt"), np.array(poly.exterior.coords), fmt='%.6f')

# def main():
#     valid_extensions = ['.png', '.jpg', '.jpeg']
#     polygon_paths = [
#         os.path.join(FOLDER_PATH, filename)
#         for filename in os.listdir(FOLDER_PATH)
#         if os.path.splitext(filename)[1].lower() in valid_extensions
#     ]

#     print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

#     frame_polygon = read_polygon_from_image(FRAME_PATH)
#     polygons = [read_polygon_from_image(path) for path in polygon_paths]
#     positioned_polygons, unfit_polygons = arrange_polygons_within_frame(polygons, frame_polygon)
#     plot_polygons(frame_polygon, positioned_polygons, OUTPUT_PATH)
#     save_unfit_polygons(unfit_polygons)

#     print(f"Output image saved to '{OUTPUT_PATH}'")
#     print(f"Unfit polygons saved to '{UNFIT_FOLDER_PATH}'")

# if __name__ == "__main__":
#     main()




import os
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.affinity import translate
import cv2
import numpy as np

# Hardcoded paths
FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\irregular shapes 5"
FRAME_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\frame_03.png"
OUTPUT_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons\outcome_vers19.png"
UNFIT_FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\unfit_polygons 2"

def read_polygon_from_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image at path {path} could not be read.")
    
    img_inverted = cv2.bitwise_not(img)
    
    contours, _ = cv2.findContours(img_inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    contour = max(contours, key=cv2.contourArea, default=None)
    if contour is None or len(contour) < 4:
        raise ValueError(f"Contours in image at path {path} are not valid polygons.")
    
    poly = Polygon(contour.squeeze())
    if not poly.is_valid:
        raise ValueError(f"Polygon created from image at path {path} is not valid.")
    
    return poly

def check_collision(poly, other_polys):
    for other in other_polys:
        if poly.intersects(other):
            return True
    return False

def find_touching_position(frame, positioned_polygons, poly, grid_spacing=5):
    frame_bounds = frame.bounds
    start_x, start_y = frame_bounds[0], frame_bounds[1]

    # Try to position the polygon by considering touching placement
    for positioned in positioned_polygons:
        for xoff, yoff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Basic directions for touching sides
            dx = positioned.bounds[0] - poly.bounds[0] + xoff
            dy = positioned.bounds[1] - poly.bounds[1] + yoff
            translated_poly = translate(poly, xoff=dx, yoff=dy)
            if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
                return translated_poly
    
    # If touching positions aren't found, check the grid
    max_range = 50
    for dx in range(0, max_range + 1, grid_spacing):
        for dy in range(0, max_range + 1, grid_spacing):
            translated_poly = translate(poly, xoff=start_x + dx, yoff=start_y + dy)
            if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
                return translated_poly
    return None

def arrange_polygons_within_frame(polygons, frame):
    positioned_polygons = []
    unfit_polygons = []

    for poly in polygons:
        positioned_poly = find_touching_position(frame, positioned_polygons, poly)
        if positioned_poly:
            positioned_polygons.append(positioned_poly)
        else:
            unfit_polygons.append(poly)

    return positioned_polygons, unfit_polygons

def plot_polygons(frame, polygons, output_path):
    fig, ax = plt.subplots()
    
    # Plot the frame polygon
    x, y = frame.exterior.xy
    ax.plot(x, y, color='black', linewidth=2)  # Frame in black

    colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
    for i, poly in enumerate(polygons):
        x, y = poly.exterior.xy
        ax.plot(x, y, color=colors[i % len(colors)])

    plt.axis('equal')
    plt.savefig(output_path)

def save_unfit_polygons(unfit_polygons, polygon_paths):
    if not os.path.exists(UNFIT_FOLDER_PATH):
        os.makedirs(UNFIT_FOLDER_PATH)
    
    for i, poly in enumerate(unfit_polygons):
        original_file = os.path.basename(polygon_paths[i])
        np.savetxt(os.path.join(UNFIT_FOLDER_PATH, f"unfit_{original_file}.txt"), np.array(poly.exterior.coords), fmt='%.6f')

# def save_unfit_polygons(unfit_polygons, polygon_paths):
#     if not os.path.exists(UNFIT_FOLDER_PATH):
#         os.makedirs(UNFIT_FOLDER_PATH)
    
#     file_path = os.path.join(UNFIT_FOLDER_PATH, "unfit_polygons_list.txt")
#     with open(file_path, "w") as f:
#         for poly in unfit_polygons:
#             # Find the original filename of the unfit polygon
#             original_file = next(os.path.basename(path) for path, p in zip(polygon_paths, polygons) if p.equals(poly))
#             f.write(f"{original_file}\n")

def main():
    valid_extensions = ['.png', '.jpg', '.jpeg']
    polygon_paths = [
        os.path.join(FOLDER_PATH, filename)
        for filename in os.listdir(FOLDER_PATH)
        if os.path.splitext(filename)[1].lower() in valid_extensions
    ]

    print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

    frame_polygon = read_polygon_from_image(FRAME_PATH)
    polygons = [read_polygon_from_image(path) for path in polygon_paths]
    positioned_polygons, unfit_polygons = arrange_polygons_within_frame(polygons, frame_polygon)
    plot_polygons(frame_polygon, positioned_polygons, OUTPUT_PATH)
    save_unfit_polygons(unfit_polygons, polygon_paths)

    print(f"Output image saved to '{OUTPUT_PATH}'")
    print(f"Unfit polygons saved to '{UNFIT_FOLDER_PATH}'")

if __name__ == "__main__":
    main()

#fak you again