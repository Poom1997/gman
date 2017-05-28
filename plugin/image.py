from pathlib import Path
from PIL import Image
import plugin.databaseConn as database
import base64
import os

class imageHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.p = Path(__file__).parents[1]
        self.default_path = (str(self.p) + "\\resources\\profiles\\noData.jpg")
        self.path = (str(self.p) + "\\resources\\profiles\\"+user_id+".jpg")

    def readImageFile(self, path):
        blob_value = open(path, 'rb').read()
        blob_data = base64.encodestring(blob_value)
        size = os.path.getsize(path)
        im = Image.open(path)
        dimension = im.size
        if(size > 200000):
            return "ERRORSIZE"
        if(dimension[0] < 225 or dimension[0] > 235 or dimension[1] < 275 or dimension[1]> 285):
            return "ERRORDIMENSION"
        else:
            return self.writeData(blob_data)

    def writeData(self, blob):
        db = database.databaseUser()
        imageWrite = db.editProfilePicture(blob, self.user_id)
        db.disconnect()
        return imageWrite

    def createImageFile(self):
        db = database.databaseUser()
        blob = db.getProfilePicture(self.user_id)
        if(blob[0].picture != None):
            file = open(self.path, "wb")
            file.write(base64.decodestring(blob[0].picture))
            file.close()
        else:
            self.path = self.default_path

    def deleteData(self):
        try:
            self.path = (str(self.p) + "\\resources\\profiles\\"+self.user_id+".jpg")
            os.remove(self.path)
        except FileNotFoundError:
            pass

    def getPath(self):
        return self.path
