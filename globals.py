
from config.uopy import UoPYConfig

def initialize():
    global clientList
    clientList = {}
    global DEBUG
    uopy = UoPYConfig()
    DEBUG = uopy.Debug()