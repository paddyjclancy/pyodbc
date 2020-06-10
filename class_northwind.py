import pyodbc


class NorthwindCon:

    # Sets up attributes in order to establish connection
    def __init__(self, server='databases2.spartaglobal.academy', database='Northwind', username='SA',
                 password='Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = self.establish_connection()
        self.cursor = self.connection.cursor()

    # Connects to database
    def establish_connection(self):
        connection = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        return connection

    # Simplifies querying throughout class
    def sql_query(self, query_str):
        return self.cursor.execute(query_str)
