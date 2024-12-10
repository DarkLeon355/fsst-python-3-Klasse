import random
import mysql.connector as mariadb


def database_setup():
    mydb = mariadb.connect(
        host="localhost",
        user="leon@localhost",
        password="maier",
        database = "python_test_01"
    )
    return mydb


def abfrage(mydb):
    mycursor = mydb.cursor()
    numbers = []
    name1 = str(input(f"Bitte Namen eingeben: "))
    while (True):
        ui = input(f"Bitte Zahl eingeben zum beenden end ")
        if ui == 'end':
            break
        else:
            ui = int(ui)
            numbers.append(ui)
    
    lengh = len(numbers)
    summe = sum(numbers)
    sql = f"INSERT IGNORE INTO werte (name, number, sum) VALUES (%s,%s,%s)"
    val =[(name1, lengh, summe)]
    mycursor.executemany(sql,val)
    mydb.commit()
    mycursor.close()
    

abfrage(database_setup())
