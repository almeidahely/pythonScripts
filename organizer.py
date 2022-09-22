from pathlib import Path
import shutil
import os

INITIAL_PATH = Path.home()
DOWNLOADS = Path(f"{INITIAL_PATH}", "Downloads")


def create_directory(directory_name):
    """ create directory into download folder """
    if directory_name not in os.listdir(DOWNLOADS):
        os.makedirs(f"{DOWNLOADS}/{directory_name}")

    return DOWNLOADS / directory_name


# noinspection PyGlobalUndefined
def move_files(move_to, *args):
    """ Move files of download directory to new directory assigned """

    global item
    for arg in args:
        file = DOWNLOADS.glob(f"**/*.{arg}")
        list_files = [file_.name for file_ in file]
        try:
            for item in list_files:
                shutil.move(f"{DOWNLOADS}/{item}", move_to)
        except shutil.Error:
            print(f"Error! The file {item} exists!")


# image_directory = create_directory("Pictures")
# move_files(image_directory, "jpg", "png")

# text_directory = create_directory("Text Files")
# move_files(text_directory, "txt", "rtf", "doc", "docx", "otf")
