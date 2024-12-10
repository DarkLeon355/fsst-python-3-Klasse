import mysql.connector as mariadb
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask
import base64
from io import BytesIO
from matplotlib.figure import Figure
import time

global xpoints
global ypoints

#connect to db
mydb = mariadb.connect(
host="localhost",
user="leon",
password="leon",
database = "sensor")
mycursor = mydb.cursor()
# finished connecting to db


while(True):

    app = Flask(__name__)

    mycursor.execute('SELECT Value FROM sensor')
    values = mycursor.fetchall() 

    mycursor.execute('SELECT Time FROM sensor')
    times = mycursor.fetchall() 

    ypoints = np.array(values)
    xpoints = np.array(times)

    @app.route("/")
    def prog():
        # Generate the figure **without using pyplot**.
        fig = Figure()
        fig.set_size_inches(10, 4)
        ax = fig.subplots()
        ax.plot(xpoints, ypoints)
        # Save it to a temporary buffer.
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return f"<img src='data:image/png;base64,{data}'/>"

    if __name__ == '__main__':

        app.run(debug=True, host='0.0.0.0')
    time.sleep(1.0)
