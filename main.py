import os, globals
import sys
from network.UOServer import *

globals.initialize()
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


runServer = runserver()
