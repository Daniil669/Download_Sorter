import os
import shutil
from watchdog.observers import Observer #will be watching for download directory 
from watchdog.events import FileSystemEventHandler #for different file system evenst
import subprocess #runs subprocesses
import time
import dotenv
import os
import pystray
from PIL import Image, ImageDraw
import threading

dotenv.load_dotenv()

extensions = {"documents": ["pdf", "doc", "docx", "odt", "rtf", "txt", "xlsx", "xlsm", "xltx", "xlsb"] , 
                "pictures": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "avif", "webp"], 
                "music": ["mp3", "wav", "flac", "ogg", "aac"], 
                "videos": ["mp4", "avi", "mov", "mkv", "wmv"]}

is_running = True

DOWNLOAD_FOLDER_PATH = os.getenv("DOWNLOAD_FOLDER_PATH")

DOCUMENTS_FOLDER_PATH = os.getenv("DOCUMENTS_FOLDER_PATH")
PICTURES_FOLDER_PATH = os.getenv("PICTURES_FOLDER_PATH")
MUSIC_FOLDER_PATH = os.getenv("MUSIC_FOLDER_PATH")
VIDEOS_FOLDER_PATH = os.getenv("VIDEOS_FOLDER_PATH")

APP_NAME = "DownloadSorter"

class DownloadHanlder(FileSystemEventHandler):
    def on_created(self, event):
        global is_running
        if not is_running: #check the global state of the app
           return
         
        if event.is_directory: #checks if event was done to the directory itself like renaming and ignores it
            return

        number_of_files_prev = len(os.listdir(DOWNLOAD_FOLDER_PATH))
        file_path = event.src_path

        try:

            while True: # checks if a file is still downloading; nothing happens if file was cancelled or still downloading, after it's been downloaded it's sorted out
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

# Generate an image and draw a pattern
def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image

#Changes state of the app after an interaction with the tray icon
def change_app_state():
    global is_running
    if is_running:
        is_running = False
        return
    is_running = True
    return

#tray icon actions; query is basically option in the menu
def icon_actions(icon, query):
    global is_running
    if str(query) == "Pause":
        change_app_state()
    elif str(query) == "Continue":
        change_app_state()
    elif str(query) == "Exit":
        icon.stop()


def download_surveillance(icon=None):
    try:
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
    except NameError:
        print(f"In download surveillance: {NameError}")



if __name__ == "__main__":
    try:
        icon = pystray.Icon(
        'Download_Sorter',
        icon=create_image(64, 64, 'black', 'white'),
        title="Download Sorter", 
        menu=pystray.Menu(
            pystray.MenuItem(lambda option : 'Pause' if is_running else 'Continue',icon_actions),
            pystray.MenuItem(
                'Exit',
                icon_actions
            )
        ))

        icon.run()
    except NameError:
        print(f"In main: {NameError}")