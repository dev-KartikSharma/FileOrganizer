import os
from queue import Queue
import shutil, threading, time


ext_map = {
    'Documents': ['.txt','.docx', '.pdf'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Images': ['.jpg', '.png', '.gif'],}
q = Queue()

def scan_directory(path):
    try:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                q.put(f)
        print(f"\t---- Scanned the directory ----\n")
        print(f"Files in {path}: {list(q.queue)}")
        # print(type(q))
        print("\nStarting to move files based on extensions...")
    except FileNotFoundError:
        print("Error: Directory not found.")
        print(f"(Directory {path} not found.)")

def move_files(q, directory_path):
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
                
if __name__ == "__main__":
    # Example usage
    # directory_path = "C:\\Users\\HP\\Downloads"
    # scan_directory(directory_path)
    
    # Creating threads for scanning and moving files
    directory_path = "C:\\Users\\HP\\Downloads"
    scan_thread = threading.Thread(target=scan_directory, args=(directory_path,))
    move_thread = threading.Thread(target=move_files, args=(q, directory_path))

    # starting threads
    scan_thread.start()
    time.sleep(2)  
    move_thread.start()

    # waiting for threads to finish
    scan_thread.join()
    move_thread.join()
    print("\nFile organization completed.")