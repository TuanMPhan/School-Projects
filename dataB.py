import mysql.connector

cnx = mysql.connector.connect(
    host ="localhost",
    user="tp",
    password="bi646999",
    database="weather"
)

mycursor = cnx.cursor()
mycursor.execute("CREATE TABLE hackensack (id INT AUTO_INCREMENT PRIMARY KEY,date VARCHAR(50), dayOrNight VARCHAR(255), temperature VARCHAR(30), short_desc VARCHAR(75), long_desc VARCHAR(500))")
mycursor.execute("CREATE TABLE hoboken (id INT AUTO_INCREMENT PRIMARY KEY,date VARCHAR(50), dayOrNight VARCHAR(255), temperature VARCHAR(30), short_desc VARCHAR(75), long_desc VARCHAR(500))")
mycursor.execute("CREATE TABLE princeton (id INT AUTO_INCREMENT PRIMARY KEY,date VARCHAR(50), dayOrNight VARCHAR(255), temperature VARCHAR(30), short_desc VARCHAR(75), long_desc VARCHAR(500))")
mycursor.execute("CREATE TABLE trenton (id INT AUTO_INCREMENT PRIMARY KEY,date VARCHAR(50), dayOrNight VARCHAR(255), temperature VARCHAR(30), short_desc VARCHAR(75), long_desc VARCHAR(500))")
mycursor.execute("CREATE TABLE newark (id INT AUTO_INCREMENT PRIMARY KEY,date VARCHAR(50), dayOrNight VARCHAR(255), temperature VARCHAR(30), short_desc VARCHAR(75), long_desc VARCHAR(500))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)