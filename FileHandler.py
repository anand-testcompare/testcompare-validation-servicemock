__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2025 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"

import csv
import os.path


class FileHandler:
    @staticmethod
    def readCSV(relPath):
        absPath = os.path.abspath(relPath)
        with open(absPath, mode='r') as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
            return data
