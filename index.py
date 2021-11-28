from flask import Flask, render_template, request, redirect
import pandas as pd
from model import algorithm

# Data Loading
restoran_df = pd.read_csv('./data/dataFinal.csv')

# Data Cleaning
restoran_df = restoran_df.drop(['Unnamed: 0','Price'],axis=1)
restoran_df = restoran_df.drop(index=135, axis=0)

weight_recommendation = []

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    global weight_recommendation

    areas = ["", "Setiabudi", "Dharmawangsa", "Thamrin", "Senopati", "SCBD", "Fatmawati", "Kemang", "Sudirman",
        "Menteng", "Blok M", "Kuningan", "Melawai", "Bogor Utara", "Gandaria", "Cikini", "Senayan",
        "Tebet", "Pluit", "Cilandak", "Kelapa Gading", "Bogor Timur", "Pantai Indah Kapuk", "Ancol",
        "Karet", "Tanjung Duren", "Pondok Melati", "Cisarua", "Bendungan Hilir", "Tanah Sareal", "Jagakarsa",
        "Serpong Utara", "Tanah Abang", "Pinang"]

    types = ["", "Casual Dining", "Fine Dining", "Café", "Lounge", "Quick Bites", "Bar", "Dessert Parlor", 
        "Food Court", "Indonesian", "Japanese", "Asian", "Desserts", "Steak", "Western", "Italian", 
        "Peranakan", "Wine Bar", "Burger", "Cafe", "Coffee", "Korean", "Grill", "Sushi", "Continental", 
        "Jawa", "Spanish", "Fusion", "Betawi", "Seafood", "Ice Cream", "Pizza", "Bakery", "Arabian", 
        "Sunda", "BBQ", "European", "French", "Peruvian", "Ramen", "Finger Food", "German", "Indian", 
        "American", "South American", "Healthy Food", "Tea", "North Indian", "Australian", "Chinese", 
        "Middle Eastern", "Dimsum", "Beverages", "Snacks", "Kebab", "Moroccan", "Belanda", "Thai"]

    prios = ["", "Lokasi", "Jenis", "Rating"]

    if request.method == 'POST':
        if request.form.get('cari-restoran') == 'Cari Restoran':
            preference_area = request.form['preference-area']
            preference_type = request.form['preference-type']
            preference_prio_1 = request.form['prio-1']
            preference_prio_2 = request.form['prio-2']

            weight_recommendation = algorithm.weighted_filtering(restoran_df, preference_type, preference_area, preference_prio_1, preference_prio_2)

            return redirect('/result')
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html', areas=areas, types=types, prios=prios)

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        if request.form.get('kembali') == 'Kembali':
            return redirect('/')
        else:
            pass
    elif request.method == 'GET':
        return render_template('result.html', result1=weight_recommendation[0], result2=weight_recommendation[1], result3=weight_recommendation[2])

if __name__ == '__main__':
    app.run()