from databaseconnector import connect

class Database:
    _cursor,_db = connect()