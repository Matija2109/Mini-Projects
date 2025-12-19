# File Organizer 🗂️

A simple Python script that automatically sorts files in a chosen folder (like `Downloads`) into subfolders based on their file extension.  
Finally, a cure for the digital landfill that is your Downloads folder.

---

## Features
- Categorizes files by extension (images, documents, music, videos, archives, installers, etc.)
- Creates destination folders automatically if they don’t exist
- Skips subfolders so only files get moved
- Easily extendable: just add more extensions to the `categories` dictionary

---

## How It Works
1. Looks at all files inside the target folder (`Downloads` by default).
2. Splits the filename to get its extension.
3. Checks the extension against the `categories` dictionary.
4. Moves the file into the appropriate subfolder using `shutil.move`.

---

