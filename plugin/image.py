import os
import base64
import plugin.databaseConnect as database
from pathlib import Path
from PIL import Image

##Class which is use to handle profile pictures##
class imageHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.p = Path(__file__).parents[1]
        self.default_path = (str(self.p) + "\\resources\\profiles\\noData.jpg")
        self.path = (str(self.p) + "\\resources\\profiles\\"+user_id+".jpg")

    ##Read Image File from a path, if picture is accepted, we writeData##
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

    ##Write our picture ata to our Database##
    def writeData(self, blob):
        db = database.databaseUser()
        imageWrite = db.editProfilePicture(blob, self.user_id)
        db.disconnect()
        return imageWrite

    ##We create an imageFile from data in the database##
    def createImageFile(self):
        db = database.databaseUser()
        blob = db.getProfilePicture(self.user_id)
        if(blob[0].picture != None):
            file = open(self.path, "wb")
            file.write(base64.decodestring(blob[0].picture))
            file.close()
        else:
            self.path = self.default_path

    ##We delete data as soon as we use it to protect user data and privacy##
    def deleteData(self):
        try:
            self.path = (str(self.p) + "\\resources\\profiles\\"+self.user_id+".jpg")
            os.remove(self.path)
        except FileNotFoundError:
            pass

    ##Get File Location as relative paths##
    def getPath(self):
        return self.path
