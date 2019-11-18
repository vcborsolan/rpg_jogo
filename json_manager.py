from json import *
from os.path import dirname,realpath,isfile


class JsonManager:

    def __init__(self):
        self.path = dirname(realpath(__file__))+'/'

    def read_json(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = f.read()
                data = json.loads(data)
            return data
        else:
            return False