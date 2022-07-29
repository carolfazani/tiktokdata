import sys
import mysql.connector
from mysql.connector import Error

class  Mydb:
    def __init__(self):
        self.mydb = None
        self.cursor = None

    def open(self):
        try:
            self.mydb = mysql.connector.connect(
                host="127.0.0.1",
                port="3306",
                user="root",
                passwd="84907350caio***",
                database="tk_data",
                # charset="utf8mb4",
                # collation="utf8mb4_general_ci",
                auth_plugin="mysql_native_password"
            )
            self.cursor = self.mydb.cursor()

        except Error as e:
            print('Erro ao acessar MySQL.', e)

    def close(self):
        if self.mydb and (self.mydb.is_connected()):
            self.cursor.close() if self.cursor else None
            self.mydb.close()
            print('Conexão MySQL encerrada.')

    def query(self, sql, single=False, noret= False, commit=False):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(sql)
            if commit:
                self.mydb.commit()
                print('Dados inseridos com sucesso')
            if noret:
                return None
            if single:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
        except Error as e:
            print('Erro ao acessar MySQL.', e)



    """Run SELECT query.
    Usage: query("SELECT codigo_mun_tse, uf, nome FROM municipios", False)
    """