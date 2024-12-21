from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pyodbc
from sqlalchemy.orm import declarative_base,sessionmaker
import os,sys
from dotenv import load_dotenv, find_dotenv
import urllib

load_dotenv(find_dotenv())

server = os.environ.get("SERVER")
database = os.environ.get("DATABASE")
username = os.environ.get("USERNAME")
password= os.environ.get("PASSWORD")

connection_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string}
)

engine = create_engine(connection_url)

Base = declarative_base()
Session=sessionmaker()

if __name__=="__main__":
    __all__ = ["engine","Base","Session"]


