import os
import shutil
from watchdog.observers import Observer #will be watching for download directory 
from watchdog.events import FileSystemEventHandler #for different file system evenst
import subprocess #runs subprocesses
import time

extensions = {"documents": ["pdf", "doc", "docx", "odt", "rtf", "txt", "xlsx", "xlsm", "xltx", "xlsb"] , 
                "pictures": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "avif", "webp"], 
                "music": ["mp3", "wav", "flac", "ogg", "aac"], 
                "videos": ["mp4", "avi", "mov", "mkv", "wmv"]}

DOWNLOAD_FOLDER_PATH = "C:/Users/dann0/Downloads"

DOCUMENTS_FOLDER_PATH = "C:/Users/dann0/Documents"
PICTURES_FOLDER_PATH = "C:/Users/dann0/Pictures"
MUSIC_FOLDER_PATH = "C:/Users/dann0/Music"
VIDEOS_FOLDER_PATH = "C:/Users/dann0/Videos"

APP_NAME = "DownloadSorter"

class DownloadHanlder(FileSystemEventHandler):
    def on_created(self, event): #self references to instance of an object not class
        if event.is_directory: #checks if event was done to the directory itself like renaming and ignores it
            return

        number_of_files_prev = len(os.listdir(DOWNLOAD_FOLDER_PATH))
        file_path = event.src_path

        try:

            while True: # check if a file is still downloading; nothing happens if file was cancelled or still downloading, after it's been downloaded it's sorted out
                if os.path.exists(file_path):
                    time.sleep(0.5)
                    continue
                elif number_of_files_prev > len(os.listdir(DOWNLOAD_FOLDER_PATH)):
                    return
                else:
                    break

            for file in os.listdir(DOWNLOAD_FOLDER_PATH):
                full_file_path = os.path.join(DOWNLOAD_FOLDER_PATH, file)

                if not os.path.isfile(full_file_path): # skips not files
                    continue

                file_extnesion = file.split(".")[-1].lower()
                for file_type in extensions:
                    if file_extnesion in extensions[file_type]:
                        match file_type:
                            case "documents":
                                shutil.move(DOWNLOAD_FOLDER_PATH + f"/{file}", DOCUMENTS_FOLDER_PATH + f"/{file}")
                            case "pictures":
                                shutil.move(DOWNLOAD_FOLDER_PATH + f"/{file}", PICTURES_FOLDER_PATH + f"/{file}")
                            case "music":
                                shutil.move(DOWNLOAD_FOLDER_PATH + f"/{file}", MUSIC_FOLDER_PATH + f"/{file}")
                            case "videos":
                                shutil.move(DOWNLOAD_FOLDER_PATH + f"/{file}", VIDEOS_FOLDER_PATH + f"/{file}")
        except NameError:
            error_message = f"{APP_NAME} ran into a problem: {NameError}"
            print(f"Error in download_sort function: {error_message}")

            try:
                subprocess.run(["cmd", "/c", f"echo {error_message} && pause"]) #opens cmd and shows message and pauses so it won't close
            except NameError:
                print(f"Failed to open cmd: {NameError}")
      

if __name__ == "__main__":
    event_handler = DownloadHanlder()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOAD_FOLDER_PATH, recursive=False)

    observer.start()
    print(f"{APP_NAME} has started and monitoring downloads...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()