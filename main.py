import os
from queue import Queue
import shutil



# extensions to folder mapping
ext_map = {
    'Documents': ['.txt','.docx', '.pdf'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Images': ['.jpg', '.png', '.gif'],}


# emply queue for file handling
q = Queue()


# scans the directory and puts only files in the queue and any folders are ignored
def scan_directory(path):
    try:
        files = []
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                q.put(f)
                files.append(f)
        print(f"\nScanned directory: {path}")
        print(f"Files: {files}")
        return files  # ✅ returning list here
    except FileNotFoundError:
        print(f"Error: Directory not found → {path}")
        return None


# moves files from the queue to their respective folder based on their extensions, if no match is found, it moves to the 'Others' folder
def move_files(directory_path):
    while not q.empty():
        file = q.get()
        for folder, extensions in ext_map.items():
            if any(file.endswith(ext) for ext in extensions):
                src = os.path.join(directory_path, file)
                dest = os.path.join(directory_path, folder, file)
                shutil.move(src, dest)
                print(f"Moved {file} to {folder}")
                break
        else:
            src = os.path.join("C:\\Users\\HP\\Downloads", file)
            dest = os.path.join("C:\\Users\\HP\\Downloads\\Others", file)
            shutil.move(src, dest)
            print(f"Moved {file} to Others")
            
        q.queue.clear()

