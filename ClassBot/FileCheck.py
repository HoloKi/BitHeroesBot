# Check inside image folder if all file are presents
import os.path
from pathlib import Path
import logging


class FileCheck:

    def __init__(self, filename):
        self.filename = filename


    def getFilename(self):
        return self.filename


    def CheckPath(self):
        if os.path.isdir(self.filename):
            logging.debug(f"Folder {self.getFilename()} presente!")
        else:
            logging.debug(f"Folder {self.getFilename()} NOT presente!")
            #Install image folder

    def CheckImage(self):
        if Path(self.filename).is_file():
            logging.debug(f"Image {self.getFilename()} presente!")
        else:
            logging.debug(f"Image {self.getFilename()} NOT presente!")

