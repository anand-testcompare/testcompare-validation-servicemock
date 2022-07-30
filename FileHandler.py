__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2021 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "anand@protrader.gg"

import csv
import os.path


class FileHandler:
    @staticmethod
    def readCSV(relPath):
        print(relPath)
        absPath = os.path.abspath(relPath)
        with open(absPath, mode='r') as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
            return data
