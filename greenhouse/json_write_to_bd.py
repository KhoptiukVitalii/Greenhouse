import requests
import sqlite3
import datetime

url = "http://194.126.183.219:8080/pvliXzHfH3f2a92cQ6ACtDgVw5-_r8tW/get/"
for i in range(9):
    v_id = "v" + str(i)
    json_response = requests.get(url + v_id).json()[0]

    tables = dict(v0='AtmosphericPressure', v1='Temperature', v2='Humidity', v3='SoilTemperature', v4='SoilMoisture',
                  v5='Light', v6='OutsideTemperature', v7='HumidityOutside', v8='ComfortIndicator')

    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    sql = "insert into greenhouse_" + tables[v_id] + "(value_date, value) values (?, ?)"
    c.execute(sql, [datetime.datetime.now(), json_response])

    conn.commit()
