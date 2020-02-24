from pymongo import MongoClient
from config.uopy import UoPYConfig


class PyUODB:

    def __init__(self):
        self.connect = MongoClient("mongodb://localhost:27017/")
        self.pyuocfg = UoPYConfig()
        self.dbname = self.pyuocfg.ConnectMongo()['database']
        self.db = self.connect[self.dbname]

