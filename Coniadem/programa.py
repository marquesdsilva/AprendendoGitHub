import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="828706",
  database= "marks_bazar"
)

print(mydb)
print("renato")
