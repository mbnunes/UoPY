import os
import sys
from network.WPServer import *

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


runServer = runserver()
