import sqlite3
import hashlib

class database:
    def __init__(self):
        self.conn = sqlite3.connect("avalon.db",check_same_thread=False)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
             (uid text, uname text, pwd text, email text)''')

    def insert_user(self, data):
        uname =  data['username']
        pwd =  data['password']
        email =  data['email']
        uid = hashlib.md5(uname).hexdigest()

        params = (uid, uname, pwd, email)

        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE uname = '%s'" % uname)
        q = c.fetchone()
        if q == None:
            c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",params)
            self.conn.commit()

            return True, q
        return False

    def find_user(self, data):
        username =  data['username']
        pwd =  data['password']

        c = self.conn.cursor()
        c.execute("SELECT * FROM users WHERE uname = '%s'" % username)
        q = c.fetchone()
        if q == None:
            return False
        return True, q
