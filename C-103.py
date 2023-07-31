import shutil
import time
from watchdog.observers import Observer
import os
import random
from watchdog.events import FileSystemEventHandler
import sys

fromDir = "C:/Users/catha/OneDrive/Desktop"
toDir = "C:/Users/catha/OneDrive/Desktop/file"

dirTree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print('file')
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dirTree.items():
            print('hello world')
            if extension in value:
                file_name = os.path.basename(event.src_path)
                path1 = fromDir+'/'+file_name
                path2 = toDir+'/'+key
                path3 = toDir+'/'+key+'/'+file_name
                if os.path.exists(path2):
                    print("pathExists")
                    shutil.move(path1, path3) 
                    time.sleep(1)
                else:
                    os.makedirs(path2)    
                    shutil.move(path1, path3)
                    time.sleep(1)

event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler, fromDir, recursive=True)
observer.start()

'''try: 
    while True:
        print('running')
except KeyboardInterrupt: 
    print('interrupted')
    observer.stop() '''
