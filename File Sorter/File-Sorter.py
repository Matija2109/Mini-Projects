import os
import shutil

folder = os.path.join(os.path.expanduser("~"), "Downloads")

categories = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".txt": "Text",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".pdf": "Docs",
    ".docx": "Docs",
    ".xlsx": "Docs",
    ".ods": "Docs",
    ".py": "Python",
    ".zip": "Archives",
    ".rar": "Archives",
    ".exe": "Installers",
    ".msi": "Installers",
    ".aspx": "Other"

}

for file in os.listdir(folder):
    src = os.path.join(folder, file)

    if not os.path.isfile(src):
        continue

    _, ext = os.path.splitext(file)

    if ext in categories:
        dest_folder = os.path.join(folder, categories[ext])
        os.makedirs(dest_folder, exist_ok=True)
        dest = os.path.join(dest_folder, file)

        shutil.move(src, dest)
        print(f"Moved {file} into {dest_folder}")





