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
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO datasets(module,source,filename,url)
                VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, dataset_info)
        self.conn.commit()
        return cur.lastrowid

    def update_dataset(self,id,field,value):
        """
        update priority, begin_date, and end date of a task
        :param conn:
        :param task:
        :return: project id
        """ 
        sql = ''' UPDATE datasets
                SET module = ? ,
                    source = ? ,
                    filename = ?,
                    url = ?
                WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, task)
        self.conn.commit()
    def list_datasets(self):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM datasets")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def delete_dataset(self,id):
        """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
        """
        sql = 'DELETE FROM datasets WHERE id=?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()

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