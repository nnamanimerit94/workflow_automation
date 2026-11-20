from pathlib import Path

def create_folder():
    downloads = Path.home()/"Downloads"
    
    folders = ["PDFs","Documents","Images","Videos","Audios"]

  
    for folder_name in folders:
        
        folder_path = downloads/folder_name
        folder_path.mkdir(exist_ok=True)
    
    return downloads


