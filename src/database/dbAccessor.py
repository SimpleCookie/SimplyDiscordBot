import psycopg2
import psycopg2.extras
from dotenv import dotenv_values

config = dotenv_values(".env")

class db():
    def __init__(self):
        try:
            self._db_connection = psycopg2.connect(
                host=config.get("DB_HOST"),
                user=config.get("DB_USER"),
                password=config.get("DB_PASSWORD"),
                dbname=config.get("DB_DATABASE")
            )
            self._db_cursor = self._db_connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            )
        except psycopg2.Error as err:
            print('Database connection failed for '+config.get("DB_USER")+'@'+config.get("DB_HOST")+'/'+config.get("DB_DATABASE"))
            print("error", err)
            exit()

    def query(self, query, params = (), commit = False, single = False):
        self._db_cursor.execute(query, params)
        if commit == True:
            self._db_connection.commit()
            return self._db_cursor.rowcount
        if single == True:
            return self._db_cursor.fetchone()
        else:
            return self._db_cursor.fetchall()

    def __del__(self):
        self._db_cursor.close()
        self._db_connection.close()
        
