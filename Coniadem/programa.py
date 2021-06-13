import mysql.connector
from mysql.connector import cursor
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senha",
  database= "marks_bazar"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE teste (nome VARCHAR(50), endereço VARCHAR(50))")

