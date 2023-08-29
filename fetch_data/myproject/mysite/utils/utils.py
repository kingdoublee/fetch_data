import pymysql

class utlis:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "king1234@"
        self.port = 3306
        self.database = "fetch_data"
        self.connection = None

    
    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )


    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    
    def close(self):
        if self.connection:
            self.connection.close()