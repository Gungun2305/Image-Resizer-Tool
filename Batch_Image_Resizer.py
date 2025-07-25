import os
from PIL import Image

# Configuration
input_folder = "images"         # Folder containing original images
output_folder = "resized"       # Folder to save resized images
new_size = (800, 600)           # Target size (width, height)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)

        # Save resized image
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)
        print(f"Resized and saved: {output_path}")

print("✅ All images resized successfully.")
