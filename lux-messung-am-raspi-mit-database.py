import time
import board
import adafruit_tsl2591
import mysql.connector as mariadb

#connect to db
mydb = mariadb.connect(
host="localhost",
user="leon",
password="leon",
database = "sensor")
mycursor = mydb.cursor()
# finished connecting to db

i2c = board.I2C() 

sensor = adafruit_tsl2591.TSL2591(i2c)

while True:
    lux = sensor.lux
    lux = round(lux, 3)

    print("Total light: {0}lux".format(lux))
    string = f"INSERT INTO sensor (Value) Values({lux});"

    try:
        mycursor.execute(string)
        mydb.commit()
        print("Succeded writing to db")
    except:
        print("Failed to write to db")

    time.sleep(1.0)