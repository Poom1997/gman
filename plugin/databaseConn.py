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
        try:
            self.connection = psycopg2.connect(host=self.__HOST,database=self.__DATABASE, user=self.__DBUSER, password=self.__DBPASS)
            self.query = self.connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        except psycopg2.OperationalError:
            raise invalidQueryException("Database Connection Error!")
        
    def disconnect(self):
        self.connection.close()

    def execute(self, command):
        self.query.execute(command)
        resultset = cur.fetchall()
        return resultset

class databaseLogin(database):
    def __init__(self):
        super().__init__()

    def userLogin(self, username, password):
        password = bytes(password, encoding="ascii")
        SQL = "SELECT password FROM \"GMan\".user_login WHERE username = %s"
        DATA = (username,)
        self.query.execute(SQL,DATA)
        resultset = self.query.fetchone()
        if(resultset == None):
            raise invalidQueryException("Either Username or Password is Incorrect")
        hashed = bytes(resultset.password, encoding="ascii")
        if (bcrypt.hashpw(password, hashed) == hashed):
            print('correct')
            return True
        else:
            print('invalid')
            raise invalidQueryException("Either Username or Password is Incorrect")
        
    def createLogin(self,userid,username,password,email,userStatus= 0, userType = 0):
        passwd_enc = bytes(password,encoding ="ascii")
        passwd_hashed = bcrypt.hashpw(passwd_enc, bcrypt.gensalt(14))
        passwd_hashed_dec = passwd_hashed.decode(encoding = "ascii")
        SQL = "INSERT INTO \"GMan\".user_login(user_id, username, password, email, status, user_type)VALUES(%s,%s,%s,%s,%s,%s)"
        DATA = (userid, username, passwd_hashed_dec, email, str(userStatus), str(userType))
        try:
            self.query.execute(SQL, DATA)
            self.connection.commit()
        except psycopg2.IntegrityError as e:
            raise invalidQueryException("UserID or Username already exists")
        
    def editLogin(self, username, email, userStatus=0):
        SQL = "UPDATE \"GMan\".user_login SET username=%s,email=%s,status=%s WHERE username=%s"
        DATA = (username, email, str(userStatus),userid)
        self.query.execute(SQL, DATA)
        self.connection.commit()

    def changePassword(self, username, oldPassword, newPassword):
        password = bytes(oldPassword, encoding="ascii")
        SQL = "SELECT password FROM \"GMan\".user_login WHERE username = %s"
        DATA = (username,)
        self.query.execute(SQL,DATA)
        resultset = self.query.fetchone()
        if(resultset == None):
            raise invalidQueryException("Either Username or Password is Incorrect")
        hashed = bytes(resultset.password, encoding="ascii")
        if (bcrypt.hashpw(password, hashed) == hashed):
            print('correct')
            passwd_enc = bytes(newPassword,encoding ="ascii")
            passwd_hashed = bcrypt.hashpw(passwd_enc, bcrypt.gensalt(14))
            passwd_hashed_dec = passwd_hashed.decode(encoding = "ascii")
            SQL = "UPDATE \"GMan\".user_login SET password=%s WHERE username = %s"
            DATA = (passwd_hashed_dec,username)
            self.query.execute(SQL, DATA)
            self.connection.commit()
        else:
            raise invalidQueryException("Either Username or Password is Incorrect")
        
    def deleteLogin(self,userid,username):
        query = "DELETE FROM "+'"'+"GMan"+'"'+".user_login WHERE user_id='"+ userid+ "' AND username = '"+ username + "'";
        self.query.execute(query)
        self.connection.commit()

    def terminate(self):
        self.disconnect()

