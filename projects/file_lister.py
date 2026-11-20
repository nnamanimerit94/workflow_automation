from pathlib import Path 

folder = Path.home()/"Downloads"

files = [items for items in folder.iterdir() if items.is_file()]

if not files:
    print("No files found")

else:
    print("\nFILES IN DOWNLOADS")
    for items in files:
        print(f"{items.name}- Extension: {items.suffix}")


folders = [item for item in folder.iterdir() if item.is_dir()]

if not folders:
    print("No folder found")
else:

    print("\nFOLDERS IN DOWNLOADS")

    for folder in folders:
        print(folder.name)
