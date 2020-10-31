import pathlib
import sqlite3
from sqlite3 import Error

class DataRegistry():
    def __init__(self,db_file):
        """ 
        English:
        \nCreates a database connection to a SQLite database 
        \ndb_file: path to a .db file where the data will be stored, if file does not exists it will create it
        \nEspañol
        \nCrea una conección a la base de datos SQLite  
        \ndb_file: ruta a archivo .db donde la data va a ser guardada, si el archivo no existe lo crea en dicha ruta
        """
        self.file=db_file
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def run_statement(self,statement):
        """ 
        English:
        \nRuns a SQL statement against the database
        \nstatement: string with SQL statement
        \nEspañol:
        \nEjecuta codigo SQL en la base de datos
        \nstatement: string con codigo SQL
        """
        try:
            c = self.conn.cursor()
            c.execute(statement)
        except Error as e:
            print(e)

    def upload_dataset(self,dataset_info):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' 
        INSERT INTO datasets(module,source,filename,url)
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
        sql = ''' 
                UPDATE datasets
                SET module = ? ,
                    source = ? ,
                    filename = ?,
                    url = ?
                WHERE id = ?
                '''
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
    db.run_statement("""
    CREATE TABLE IF NOT EXISTS datasets (
        id integer PRIMARY KEY,
        module text NOT NULL,
        source text NOT NULL,
        filename text NOT NULL,
        url text NOT NULL
        );
    """)