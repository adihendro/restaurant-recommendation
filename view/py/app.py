import json
import sys
import pandas as pd

sys.stdout = open('../js/result_data.js', 'w')

df_restoran = pd.read_csv('../../data/dataFinal.csv')

send_data = {
    'rest_1': df_restoran['Name'].values[0],
    'rest_2': df_restoran['Name'].values[1],
    'rest_3': df_restoran['Name'].values[2]
}

send_json = json.dumps(send_data)

print("var resultData = '{}';".format(send_json))
print("let jsonData = JSON.parse(resultData);")
print("const resultDiv_1 = document.getElementById('result-content-1');")
print("resultDiv_1.innerText = jsonData.rest_1;")
print("const resultDiv_2 = document.getElementById('result-content-2');")
print("resultDiv_2.innerText = jsonData.rest_2;")
print("const resultDiv_3 = document.getElementById('result-content-3');")
print("resultDiv_3.innerText = jsonData.rest_3;")