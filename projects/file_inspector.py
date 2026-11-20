from pathlib import Path

folder = Path.home()/"Documents"

for contents in folder.iterdir():
    