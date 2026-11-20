from folder_creator import create_folder
import shutil

downloads_path = create_folder()

images_folder = downloads_path/"Images"


image_extensions = [
    items for items in downloads_path.iterdir()
    if items.is_file() and items.suffix.lower() in (".png",".jpg",".jpeg",".gif",".webp")
]

if not image_extensions:
    print("No images found")

else:
    for file in image_extensions:
        shutil.move(str(file), str(images_folder/file.name))
        print(f"Moved {file.name} to {images_folder}")




