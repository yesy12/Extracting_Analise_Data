import pyodbc
from platform import node
from dotenv import load_dotenv
from os import getcwd, environ
from logging import critical
load_dotenv()  

class credential:

    def __init__(self) -> None:   
        try:
            database = environ["database"]
            dados_conexao = (
                "Driver={Sql Server};"
                f"Server={node()};"
                f"Database={database};"
                "Trusted_Connection=yes"
            )
            self.conn = pyodbc.connect(dados_conexao) 
            self.cursor = self.conn.cursor()
            print("Connection is success...")
        except:
            print("Connections is failed...")

    def insert(self, sql) -> None:
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except pyodbc.DatabaseError as error:
            critical("*"*100)
            critical(error)
            self.conn.rollback()
        except pyodbc.IntegrityError as error:
            self.conn.rollback()

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()  
        except:
            critical("ERROR _ SELECT ")
            self.conn.rollback()
    
    def openFile(self, path):
        with open(path,"r", encoding="utf-8") as files:
            self.insert(files.read())
            print("INSERIDO")

    def initStructure(self):
        diretorioActual = f"{getcwd()}/Extracting_Data/sql/"
        self.openFile(f"{diretorioActual}SqlCreateTable.sql")
        self.openFile(f"{diretorioActual}SqlAlterTable.sql")
        self.openFile(f"{diretorioActual}SqlQueryInsert.sql")
    