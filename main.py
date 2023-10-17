from PIL import Image
import os

# Define input and output directories
input_directory = "/Users/manshisagar/Desktop/sem-7assign/col865/project/COL865_MMRS/movie_posters_new"
output_directory = "/Users/manshisagar/Desktop/sem-7assign/col865/project/COL865_MMRS/movie_posters_resized"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the maximum size you want for the images
max_size = (128, 128)  # Adjust these values as needed

# Loop through the files in the input directory
for file_name in os.listdir(input_directory):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        # Open the image file
        image = Image.open(os.path.join(input_directory, file_name))

        # Resize the image
        image.thumbnail(max_size)

        # Save the resized image to the output directory
        image.save(os.path.join(output_directory, file_name))

print("Images resized and saved successfully.")
