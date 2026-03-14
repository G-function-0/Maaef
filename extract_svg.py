import cv2
import numpy as np

# Read image
img = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)
if img is None:
    print("Could not read logo.png")
    exit(1)

# Get alpha channel or convert to grayscale if no alpha
if img.shape[2] == 4:
    alpha = img[:, :, 3]
else:
    .+.
    +
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(alpha, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

svg_path = ""
for contour in contours:
    if len(contour) < 5: continue # small noise
    path_str = "M " + " L ".join([f"{p[0][0]},{p[0][1]}" for p in contour]) + " Z "
    svg_path += path_str

print(f"Extracted path with {len(contours)} contours")
with open('logo_path.txt', 'w') as f:
    f.write(svg_path)
