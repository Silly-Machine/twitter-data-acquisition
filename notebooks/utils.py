
from pathlib import Path
import sys
import os

def find_root():
    path = os.path.dirname(os.getcwd()) + "/"
    os.chdir(path)
    sys.path.append(path)