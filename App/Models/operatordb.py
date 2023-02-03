import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

conn_str = (
  r'Driver={driver};'
  r'Server=localhost\SQLEXPRESS;'
  r'Database={db};'
  r'UID={login};'
  r'PWD={password};'
  r'TrustServerCertificate=Yes;'
).format(driver=os.environ.get("DRIVER_PATH"),
         db=os.environ.get("OPERATOR_DB"), 
         login=os.environ.get("OPERATOR_DB_LOGIN"), 
         password=os.environ.get("OPERATOR_DB_PASSWORD"))

def connectToOperatorDB():
  connection = pyodbc.connect(conn_str)
  return connection.cursor()
