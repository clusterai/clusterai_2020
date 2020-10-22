import pathlib
import sqlite3
from sqlite3 import Error

class DataRegistry():
    def __init__(self,db_file):
        """ create a database connection to a SQLite database """
        self.file=db_file
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def create_table(self,create_statement):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_statement)
        except Error as e:
            print(e)
    def upload_dataset(self,dataset_info):
        pass

    def list_datasets(self):
        pass

    def delete_dataset(self,id):
        pass

if __name__ == '__main__':
    db=DataRegistry(pathlib.Path()/"datasets"/"datasets_registry.db")
    db.create_table("""
    CREATE TABLE IF NOT EXISTS datasets (
        id integer PRIMARY KEY,
        module text NOT NULL,
        source text NOT NULL,
        filename text NOT NULL,
        url text NOT NULL
        );
    """)