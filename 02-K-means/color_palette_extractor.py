from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# Load image
image_path = "image.png"
if not os.path.exists(image_path):
    image_path = input("Enter image path: ")

# Process image
image = np.array(Image.open(image_path).convert('RGB'))
pixels = image.reshape(-1, 3)

# Extract palette
palette = KMeans(n_clusters=5, random_state=42).fit(pixels).cluster_centers_.astype(int)

# Display results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.imshow(image)
ax1.axis('off')
ax1.set_title('Original Image')

ax2.imshow([palette], aspect='auto')
ax2.axis('off')
ax2.set_title('Color Palette')

plt.tight_layout()
plt.show()