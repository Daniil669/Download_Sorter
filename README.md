# Download_Sorter
📁 Download Folder Auto-Sorter
This Python-based tool automatically monitors your download folder and sorts files into categorized directories such as Documents, Pictures, Music, and Videos. It runs silently in the background with a tray icon interface and is ideal for automating file organization.

⚙️ Features
✅ Real-time monitoring using watchdog

✅ Auto-sorting files into folders by type (document, music, video, image)

✅ System tray interface with options: Pause, Continue, Exit

✅ Logging with timestamps and error tracking

✅ Windows Scheduler ready as a .exe

📂 File Types Sorted
Category	Extensions
Documents	pdf, doc, docx, odt, rtf, txt, xlsx, xlsm, xltx, xlsb
Pictures	jpg, jpeg, png, gif, bmp, tiff, avif, webp
Music	    mp3, wav, flac, ogg, aac
Videos	    mp4, avi, mov, mkv, wmv

🧪 Requirements
Install dependencies using:

bash
pip install -r requirements.txt

Example requirements.txt:
watchdog
python-dotenv
pystray
Pillow

🛠️ Setup
Configure Environment Variables
Create a .env file in the root folder (example below):

env
DOWNLOAD_FOLDER_PATH=C:/Users/YourName/Downloads
DOCUMENTS_FOLDER_PATH=C:/Users/YourName/Documents
PICTURES_FOLDER_PATH=C:/Users/YourName/Pictures
MUSIC_FOLDER_PATH=C:/Users/YourName/Music
VIDEOS_FOLDER_PATH=C:/Users/YourName/Videos
LOG_FILE=C:/Users/YourName/Documents
You can also copy .env.example and modify it.

Run the App
bash
python main.py
🪟 Convert to .exe (Windows only)
Use PyInstaller to bundle into an executable:

bash
pyinstaller --onefile --add-data ".env;." --add-data "README.md;." main.py
Your .exe will be in the dist/ folder.

📅 Add to Windows Scheduler
To run at login:

Open Task Scheduler

Create Task → Triggers: At log on

Actions → Start a program → point to dist/main.exe

🖥️ Tray Icon Options
Pause: Temporarily stops monitoring downloads

Continue: Resumes monitoring

Exit: Shuts down the app gracefully

📓 Logging
Logs are saved under:

bash
[LOG_FILE]/Download Sorter/Logs/logs.log
