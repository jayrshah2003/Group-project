import numpy as np
import model
from flask import Flask,render_template, request
import sqlite3
import pathlib
import pickle


base_path= pathlib.Path(r'C:\Users\jay\Downloads\Group project\Webpage')
db_name="final.db"
db_path= base_path/db_name


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Homepage.html")



@app.route("/weather")
def weather():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    weather = cursor.execute("SELECT * FROM pd_weather LIMIT 5").fetchall()
    con.close()

    return render_template("weather_table.html",weather=weather)
def predict():
    TempAvgF = request.args.get('TempAvgF')
    DewPointAvgF = request.args.get('DewPointAvgF')
    HumidityAvgPercent = request.args.get('HumidityAvgPercent')
    
    arr = np.array([TempAvgF,DewPointAvgF,HumidityAvgPercent])
    brr = np.asarray(arr, dtype=float)
    output = model.predict([brr])
    if(output==1):
        out = 'You have high chances of getting placed!!!'
    else:
        out = 'You have low chances of getting placed. All the best.'
    return render_template( output=out)


@app.route("/titanic")
def titanic():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    titanic = cursor.execute("SELECT * FROM pd_titanic LIMIT 5").fetchall()
    con.close()

    return render_template("titanic_table.html",titanic=titanic)

@app.route("/diabetes")
def diabetes():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    diabetes = cursor.execute("SELECT * FROM pd_diabetes LIMIT 5").fetchall()
    con.close()

    return render_template("diabetes_table.html",diabetes=diabetes)


load_saved_model = r"C:\Users\jay\Downloads\Group project\Webpage\savedmodels\knn_model.pickle"
with open(load_saved_model, 'rb') as f:
    knn_model = pickle.load(f)


    
    


if __name__ == "__main__":
    app.run(debug=True)



