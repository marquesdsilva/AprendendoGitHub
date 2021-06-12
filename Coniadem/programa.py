import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="828706",
  database= "marks_bazar"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE teste (nome VARCHAR(50), endereço VARCHAR(50))")

