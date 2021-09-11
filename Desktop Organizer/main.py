import os
import shutil


Folder_Dictionary = {
    "IMG": [".jpg", ".png", ".gif", ".jfif", ".drawio"],
    "AUD": [".mp3", ".ogg"],
    "VID": [".mp4"],
    "DOC": [".pdf", ".docx", ".xlsx", ".txt"],
    "EXE": [".exe"],
}


def file_organizer():
    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        filename, file_ext = os.path.splitext(file)
        if file_ext:
            for folder in Folder_Dictionary:
                for ext in Folder_Dictionary[folder]:
                    if file_ext == ext:
                        if not os.path.exists(os.path.join(current_dir, f'{folder}')):
                            os.mkdir(os.path.join(current_dir, f'{folder}'))
                        shutil.move(os.path.join(current_dir, f'{filename}{file_ext}'),
                                    os.path.join(current_dir, f'{folder}'))


def file_killer():
    current_dir = os.getcwd()
    for direc in os.listdir(current_dir):
        if os.path.isdir(direc):
            if not os.listdir(os.path.join(current_dir, direc)):
                os.rmdir(os.path.join(current_dir, direc))


if __name__ == "__main__":
    file_organizer()
    file_killer()
