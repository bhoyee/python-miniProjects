import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)
    
    # Filter only the image files
    image_files = [file for file in file_list if file.lower().endswith(('.jpeg', '.jpg', '.png', '.gif'))]
    
    # Sort the image files alphabetically
    image_files.sort()
    
    # Rename and change the extension of each image file
    for i, image_file in enumerate(image_files):
        old_path = os.path.join(folder_path, image_file)
        new_file_name = f"{i + 1}.jpg"
        new_path = os.path.join(folder_path, new_file_name)
        os.rename(old_path, new_path)
    
    print("Image renaming complete.")

# Provide the folder path where the images are located
folder_path = "C:/Users/Bhoyee-pc/Desktop/yoloDemov2/img"

# Call the function to rename the images
rename_images(folder_path)
