# # import os
# # import matplotlib.pyplot as plt
# # from shapely.geometry import Polygon
# # from shapely.affinity import translate
# # import cv2
# # import numpy as np

# # # Hardcoded paths
# # FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\real_trial 1"
# # FRAME_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\frames\frame_04.png"
# # OUTPUT_FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons 6"
# # VARIATIONS_COUNT = 2

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

# # def find_touching_position(frame, positioned_polygons, poly, grid_spacing=5):
# #     frame_bounds = frame.bounds
# #     start_x, start_y = frame_bounds[0], frame_bounds[1]

# #     # Try to position the polygon by considering touching placement
# #     for positioned in positioned_polygons:
# #         for xoff, yoff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Basic directions for touching sides
# #             dx = positioned.bounds[0] - poly.bounds[0] + xoff
# #             dy = positioned.bounds[1] - poly.bounds[1] + yoff
# #             translated_poly = translate(poly, xoff=dx, yoff=dy)
# #             if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
# #                 return translated_poly
    
# #     # If touching positions aren't found, check the grid
# #     max_range = 600
# #     for dx in range(0, max_range + 1, grid_spacing):
# #         for dy in range(0, max_range + 1, grid_spacing):
# #             translated_poly = translate(poly, xoff=start_x + dx, yoff=start_y + dy)
# #             if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
# #                 return translated_poly
# #     return None

# # def arrange_polygons_within_frame(polygons, frame):
# #     positioned_polygons = []
# #     unfit_polygons = []

# #     for poly in polygons:
# #         positioned_poly = find_touching_position(frame, positioned_polygons, poly)
# #         if positioned_poly:
# #             positioned_polygons.append(positioned_poly)
# #         else:
# #             unfit_polygons.append(poly)

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
# #     plt.close(fig)

# # def main():
# #     valid_extensions = ['.png', '.jpg', '.jpeg']
# #     polygon_paths = [
# #         os.path.join(FOLDER_PATH, filename)
# #         for filename in os.listdir(FOLDER_PATH)
# #         if os.path.splitext(filename)[1].lower() in valid_extensions
# #     ]

# #     if not os.path.exists(OUTPUT_FOLDER_PATH):
# #         os.makedirs(OUTPUT_FOLDER_PATH)

# #     print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

# #     frame_polygon = read_polygon_from_image(FRAME_PATH)
# #     polygons = [read_polygon_from_image(path) for path in polygon_paths]

# #     for variation in range(1, VARIATIONS_COUNT + 1):
# #         np.random.shuffle(polygons)  # Shuffle the polygons to get different variations
# #         positioned_polygons, unfit_polygons = arrange_polygons_within_frame(polygons, frame_polygon)

# #         output_image_path = os.path.join(OUTPUT_FOLDER_PATH, f"outcome_variation_{variation}.png")
        
# #         plot_polygons(frame_polygon, positioned_polygons, output_image_path)

# #         print(f"Variation {variation}: Output image saved to '{output_image_path}'")

# # if __name__ == "__main__":
# #     main()


# import os
# import matplotlib.pyplot as plt
# from shapely.geometry import Polygon
# from shapely.affinity import translate
# import cv2
# import numpy as np

# # Hardcoded paths
# FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\real_trial 1"
# FRAME_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\frames\frame_04.png"
# OUTPUT_FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons 6"
# VARIATIONS_COUNT = 2

# def read_polygon_from_image(path):
#     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#     if img is None:
#         raise ValueError(f"Image at path {path} could not be read.")
    
#     # Apply black mask to the image
#     _, img_thresh = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
#     img_inverted = cv2.bitwise_not(img_thresh)
    
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

# def find_touching_position(frame, positioned_polygons, poly, grid_spacing=5):
#     frame_bounds = frame.bounds
#     start_x, start_y = frame_bounds[0], frame_bounds[1]

#     # Try to position the polygon by considering touching placement
#     for positioned in positioned_polygons:
#         for xoff, yoff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Basic directions for touching sides
#             dx = positioned.bounds[0] - poly.bounds[0] + xoff
#             dy = positioned.bounds[1] - poly.bounds[1] + yoff
#             translated_poly = translate(poly, xoff=dx, yoff=dy)
#             if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
#                 return translated_poly
    
#     # If touching positions aren't found, check the grid
#     max_range = 600
#     for dx in range(0, max_range + 1, grid_spacing):
#         for dy in range(0, max_range + 1, grid_spacing):
#             translated_poly = translate(poly, xoff=start_x + dx, yoff=start_y + dy)
#             if frame.contains(translated_poly) and not check_collision(translated_poly, positioned_polygons):
#                 return translated_poly
#     return None

# def arrange_polygons_within_frame(polygons, frame):
#     positioned_polygons = []
#     unfit_polygons = []

#     for poly in polygons:
#         positioned_poly = find_touching_position(frame, positioned_polygons, poly)
#         if positioned_poly:
#             positioned_polygons.append(positioned_poly)
#         else:
#             unfit_polygons.append(poly)

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
#     plt.close(fig)

# def main():
#     valid_extensions = ['.png', '.jpg', '.jpeg']
#     polygon_paths = [
#         os.path.join(FOLDER_PATH, filename)
#         for filename in os.listdir(FOLDER_PATH)
#         if os.path.splitext(filename)[1].lower() in valid_extensions
#     ]

#     if not os.path.exists(OUTPUT_FOLDER_PATH):
#         os.makedirs(OUTPUT_FOLDER_PATH)

#     print(f"Found {len(polygon_paths)} polygon image(s) in folder '{FOLDER_PATH}'.")

#     frame_polygon = read_polygon_from_image(FRAME_PATH)
#     polygons = [read_polygon_from_image(path) for path in polygon_paths]

#     for variation in range(1, VARIATIONS_COUNT + 1):
#         np.random.shuffle(polygons)  # Shuffle the polygons to get different variations
#         positioned_polygons, unfit_polygons = arrange_polygons_within_frame(polygons, frame_polygon)

#         output_image_path = os.path.join(OUTPUT_FOLDER_PATH, f"outcome_variation_{variation}.png")
        
#         plot_polygons(frame_polygon, positioned_polygons, output_image_path)

#         print(f"Variation {variation}: Output image saved to '{output_image_path}'")

# if __name__ == "__main__":
#     main()

import os
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.affinity import translate
import cv2
import numpy as np

# Hardcoded paths
FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\real_trial 1"
FRAME_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\frames\frame_04.png"
OUTPUT_FOLDER_PATH = r"C:\Users\berka\OneDrive\Desktop\CORE\tet-ris\outcome_polygons 6"
VARIATIONS_COUNT = 2

def read_polygon_from_image(path):
    # Read image with transparency
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise ValueError(f"Image at path {path} could not be read.")
    
    if img.shape[2] == 4:  # Check if the image has an alpha channel
        alpha_channel = img[:, :, 3]
        _, mask = cv2.threshold(alpha_channel, 1, 255, cv2.THRESH_BINARY)
    else:
        mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
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
    max_range = 600
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
    ax.plot(x, y, color='black)

