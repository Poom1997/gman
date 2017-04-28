import psycopg2
import psycopg2.extras
import bcrypt
from Crypto.Cipher import AES

class invalidQueryException(Exception): pass

class database:
    def __init__(self):
        self.__HOST = "myawsdatabase.ckpmuridajwz.us-west-2.rds.amazonaws.com"
        self.__DATABASE = "crazypetData"
        self.__DBUSER = "app"
        self.__DBPASS = "2rG3RSfTZ1"
        self.__connection = ""
        self.__query = ""
        
    def connect(self):
        self.__connection = psycopg2.connect(host=self.__HOST,database=self.__DATABASE, user=self.__DBUSER, password=self.__DBPASS)
        self.__query = self.__connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def disconnect(self):
        self.__connection.close()

    def execute(self, command):
        self.__query.execute(command)
        resultset = cur.fetchall()
        return resultset

    def userLogin(self,username, password):
        self.__query.execute("SELECT password FROM "+'"'+ "GMan" + '"' +".user_login WHERE username = '"+ username + "'")
        resultset = self.__query.fetchone()
        print(resultset)
        if(len(resultset)==0):
            raise invalidQueryException("Username do not exists")
        hashed = bytes(resultset['password'], encoding="ascii")
        password = bytes(password, encoding="ascii")
        print(password)
        if (bcrypt.hashpw(password, hashed) == hashed):
            print('correct')
            return True
        else:
            raise invalidQueryException("Either Username or Password is Incorrect")
        
    def createLogin(self,userid,username,password,email,userStatus= 0, userType = 0):
        passwd_enc = password = bytes(password, encoding="ascii")
        passwd_hashed = bcrypt.hashpw(passwd_enc, bcrypt.gensalt(14))
        passwd_hashed_dec = passwd_hashed.decode(encoding = "ascii")
        query = "INSERT INTO "+'"'+"GMan"+'"'+".user_login(user_id, username, password, email, status, user_type)VALUES('"\
            +userid+"', '"\
            +username+"', '"\
            +passwd_hashed_dec+"', '"\
            +email+"', "+str(userStatus)+", "+str(userType)+")"
        self.__query.execute(query)
        self.__connection.commit()

    def editLogin(self, userid, username, email, userStatus=0):
        query = "UPDATE "+'"'+ "GMan" + '"' +".user_login SET username='"\
                + username + "',email='"\
                +email + "',status='"\
                + str(userStatus) + "' WHERE user_id='"+ userid + "' AND username = '"+ username + "'"
        print(query)
        self.__query.execute(query)
        self.__connection.commit()


    def deleteLogin(self,userid,username):
        query = "DELETE FROM "+'"'+"GMan"+'"'+".user_login WHERE user_id='"+ userid+ "' AND username = '"+ username + "'";
        self.__query.execute(query)
        self.__connection.commit()
        
##HOST = "myawsdatabase.ckpmuridajwz.us-west-2.rds.amazonaws.com"
##conn = psycopg2.connect(host=HOST,database="crazypetData", user="app", password="2rG3RSfTZ1")
##cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
##cur.execute("SELECT * FROM "+'"'+ "GMan" + '"' +".test")
##resultset = cur.fetchall()
##print(resultset[0]['id'])
##conn.close()

##password = b"abcde"
##hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
##print(hashed)
##if (bcrypt.hashpw(password, hashed) == hashed):
##    print("It Matches!")
##else:
##    print("Error")

a = database()
a.connect()
a.deleteLogin("c580", "pun")
