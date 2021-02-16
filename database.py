from pymysql import connect

#connect to DB
class connector:
    def connection(self):
        try:
            self.con = connect('localhost','root', '', 'users')
            self.cursor = self.con.cursor()
        except:
            print('error')

#insert a data
class signin(connector):
    def __init__(self, username, email, password):
        connector.connection(self)
        data = (username, email, password)
        query = 'INSERT INTO users_info(username, email, password) VALUES (%s,%s,%s)'

        self.cursor.execute(query, data)

        self.con.commit()

#get username and password
class login(connector):
    def __init__(self, username, password):
        connector.connection(self)

        data = (username, password)
        query = 'SELECT * FROM users_info WHERE username LIKE %s AND password LIKE %s'

        self.cursor.execute(query, data)
        self.values = self.cursor.fetchall()

    def get(self):
        return self.values

#get email 
class getpass(connector):
    def __init__(self, email):
        connector.connection(self)

        data = (email)
        query = 'SELECT * FROM users_info WHERE email LIKE %s'

        self.cursor.execute(query, data)
        self.result = self.cursor.fetchall()
    
    def get(self):
        return self.result

#get username
class account(connector):
    def __init__(self, username):
        connector.connection(self)

        data = (username)
        query = 'SELECT * FROM users_info WHERE username LIKE %s'

        self.cursor.execute(query, data)
        self.result = self.cursor.fetchall()
    
    def get(self):
        return self.result

