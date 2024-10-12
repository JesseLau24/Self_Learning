from PIL import Image
import os

# Input Dir
input_dir = '/home/jesse/Pictures/Test_Pics/Raw'
output_dir = '/home/jesse/Pictures/Test_Pics/Processed'

# Make output directory
os.makedirs(output_dir, exist_ok=True)

# iterate the pics in input dir
for image_file in os.listdir(input_dir):
    if image_file.endswith('.png'):
        # Open pics
        image_path = os.path.join(input_dir, image_file)
        image = Image.open(image_path)

        # Resize to 28x28
        image = image.resize((28, 28), Image.Resampling.LANCZOS)

        # Save to putput directory
        output_path = os.path.join(output_dir, image_file)
        image.save(output_path)

print("Pics have been resized!")
