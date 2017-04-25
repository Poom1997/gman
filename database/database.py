import psycopg2
import bcrypt
import psycopg2.extras

#class database:
    #def __init__(self):
        #self.

##conn = psycopg2.connect(host="horton.elephantsql.com",database="hklptrrl", user="hklptrrl", password="8IP7CXbIe7E5NPV34b8LyGjrRFq57AKo")
##cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
##cur.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
##resultset = cur.fetchone()
##print(resultset["table_catalog"])
##conn.close()

password = b"abcde"
hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
print(hashed)
if (bcrypt.hashpw(password, hashed) == hashed):
    print("It Matches!")
else:
    print("Error")

