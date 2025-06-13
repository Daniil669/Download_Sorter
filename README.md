# 📁 Download Sorter

**Download Sorter** is a lightweight Python tool that automatically monitors your Downloads folder and sorts files into categorized directories like **Documents**, **Pictures**, **Music**, and **Videos**. It runs silently in the background with a system tray icon — perfect for automated file organization.

---

## ⚙️ Features

- ✅ Real-time folder monitoring using `watchdog`
- ✅ Automatically sorts files by type (documents, music, videos, images)
- ✅ System tray icon with options: **Pause**, **Continue**, **Exit**
- ✅ Timestamped logs with error tracking
- ✅ Packaged as `.exe` for Windows Task Scheduler support

---

## 📂 File Types Sorted

| **Category** | **Extensions** |
|--------------|----------------|
| Documents    | `pdf`, `doc`, `docx`, `odt`, `rtf`, `txt`, `xlsx`, `xlsm`, `xltx`, `xlsb` |
| Pictures     | `jpg`, `jpeg`, `png`, `gif`, `bmp`, `tiff`, `avif`, `webp` |
| Music        | `mp3`, `wav`, `flac`, `ogg`, `aac` |
| Videos       | `mp4`, `avi`, `mov`, `mkv`, `wmv` |

---

## 🧪 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt

📦 Example `requirements.txt`
watchdog
python-dotenv
pystray
Pillow
```
---

## 🛠️ Setup

### 1. Create a `.env` file

In your project root, add:
```ini
DOWNLOAD_FOLDER_PATH=C:/Users/YourName/Downloads
DOCUMENTS_FOLDER_PATH=C:/Users/YourName/Documents
PICTURES_FOLDER_PATH=C:/Users/YourName/Pictures
MUSIC_FOLDER_PATH=C:/Users/YourName/Music
VIDEOS_FOLDER_PATH=C:/Users/YourName/Videos
LOG_FILE=C:/Users/YourName/Documents
```
You can also duplicate and rename `.env.example`.

---

### 2. Run the App
To start the app manually:

```bash
python main.py
```
---

## 🪟 Create Windows Executable (.exe)
Package the script using PyInstaller:

```bash
pyinstaller --onefile --windowed --add-data ".env;." --add-data "README.md;." main.py
```
The `.exe` file will appear in the dist/ folder.

---

## 📅 Add to Windows Task Scheduler
To run the app at login:

1. Open Task Scheduler

2. Click Create Task

3. Go to the Triggers tab → choose At log on

4. Go to the Actions tab → choose Start a program

5. Browse to dist/main.exe and confirm

---

## 🖥️ Tray Icon Menu
- Pause – Temporarily stop monitoring

- Continue – Resume monitoring

- Exit – Quit the app cleanly

---

## 📓 Logging
Logs are saved at:

```bash
[LOG_FILE]/Download Sorter/Logs/logs.log
```
These logs include:

- Timestamped file movements

- Errors and exceptions
