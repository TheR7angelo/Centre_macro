import json
import os


class Json:
    def __init__(self, lien_json):
        self.lien_json = lien_json

    def OPEN(self):
        with open(os.path.abspath(self.lien_json), "r") as fichier:
            return json.load(fichier)
    def WRITE(self, data):
        with open(self.lien_json, 'w') as fichier:
            json.dump(data, fichier, indent=4)
    def UPDATE(self, dct):
        with open(self.lien_json, "r+") as fichier:
            data = json.load(fichier)
            data.update(dct)
            fichier.seek(0)
            json.dump(data, fichier, indent=4)
            fichier.truncate()
    def REMOVE(self, key):
        with open(self.lien_json, "r+") as fichier:
                data = json.load(fichier)
                data.pop(key)
                fichier.seek(0)
                json.dump(data, fichier)
