from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
import pandas as pd
from model import algorithm
import re

# Data Loading
restoran_df = pd.read_csv('./data/dataFinal.csv')

# Data Cleaning
restoran_df = restoran_df.drop(['Unnamed: 0', 'Price'], axis=1)
restoran_df = restoran_df.drop(index=135, axis=0)

weight_recommendation = []

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    global weight_recommendation
    global restoran_df

    areas = ["Setiabudi", "Dharmawangsa", "Thamrin", "Senopati", "SCBD", "Fatmawati", "Kemang", "Sudirman",
             "Menteng", "Blok M", "Kuningan", "Melawai", "Bogor Utara", "Gandaria", "Cikini", "Senayan",
             "Tebet", "Pluit", "Cilandak", "Kelapa Gading", "Bogor Timur", "Pantai Indah Kapuk", "Ancol",
             "Karet", "Tanjung Duren", "Pondok Melati", "Cisarua", "Bendungan Hilir", "Tanah Sareal", "Jagakarsa",
             "Serpong Utara", "Tanah Abang", "Pinang"]

    types = ["Casual Dining", "Fine Dining", "Café", "Lounge", "Quick Bites", "Bar", "Dessert Parlor",
             "Food Court", "Indonesian", "Japanese", "Asian", "Desserts", "Steak", "Western", "Italian",
             "Peranakan", "Wine Bar", "Burger", "Cafe", "Coffee", "Korean", "Grill", "Sushi", "Continental",
             "Jawa", "Spanish", "Fusion", "Betawi", "Seafood", "Ice Cream", "Pizza", "Bakery", "Arabian",
             "Sunda", "BBQ", "European", "French", "Peruvian", "Ramen", "Finger Food", "German", "Indian",
             "American", "South American", "Healthy Food", "Tea", "North Indian", "Australian", "Chinese",
             "Middle Eastern", "Dimsum", "Beverages", "Snacks", "Kebab", "Moroccan", "Belanda", "Thai"]

    # prios = ["Lokasi", "Jenis", "Rating"]

    if request.method == 'POST':

        if request.form.get('cari-restoran') == 'Cari Restoran':
            preference_area = request.form['preference-area']
            preference_type = request.form['preference-type']
            preference_prio_1 = request.form.get('prio-1')
            preference_prio_2 = request.form.get('prio-2')

            restoran_df = restoran_df.sort_values(by='Restaurant_ID')

            weight_recommendation = algorithm.weighted_filtering(
                restoran_df, preference_type, preference_area, preference_prio_1, preference_prio_2)

            return redirect('/result')
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html', areas=areas, types=types)


@app.route('/result', methods=['GET', 'POST'])
def result():
    global weight_recommendation

    if request.method == 'POST':
        if request.form.get('kembali') == 'Kembali':
            return redirect('/')
        elif request.form.get('more-result-1') == 'Other Similar Result':
            nama = request.form['result-1']
            weight_recommendation = algorithm.content_based_filtering(
                restoran_df, nama)
            nama = nama.lower()
            nama = re.sub(r'[^.,a-zA-Z0-9 \n\.]', ' ', nama)
            nama = re.sub(r'[^\w\s]', '', nama)
            nama = re.sub('[\s]+', ' ', nama)
            nama = nama.replace(" ", "")
            return redirect(url_for('specific_result', nama=nama))
        elif request.form.get('more-result-2') == 'Other Similar Result':
            nama = request.form['result-2']
            weight_recommendation = algorithm.content_based_filtering(
                restoran_df, nama)
            nama = nama.lower()
            nama = re.sub(r'[^.,a-zA-Z0-9 \n\.]', ' ', nama)
            nama = re.sub(r'[^\w\s]', '', nama)
            nama = re.sub('[\s]+', ' ', nama)
            nama = nama.replace(" ", "")
            return redirect(url_for('specific_result', nama=nama))
        elif request.form.get('more-result-3') == 'Other Similar Result':
            nama = request.form['result-3']
            weight_recommendation = algorithm.content_based_filtering(
                restoran_df, nama)
            nama = nama.lower()
            nama = re.sub(r'[^.,a-zA-Z0-9 \n\.]', ' ', nama)
            nama = re.sub(r'[^\w\s]', '', nama)
            nama = re.sub('[\s]+', ' ', nama)
            nama = nama.replace(" ", "")
            return redirect(url_for('specific_result', nama=nama))
        else:
            pass
    elif request.method == 'GET':
        return render_template('result.html', result1=weight_recommendation[0], result2=weight_recommendation[1], result3=weight_recommendation[2])


@app.route('/result/<nama>', methods=['GET', 'POST'])
def specific_result(nama):
    global weight_recommendation

    if request.method == 'POST':
        if request.form.get('kembali') == 'Kembali':
            return redirect('/')
        elif request.form.get('more-result-1') == 'Other Similar Result':
            nama = request.form['result-1']
            weight_recommendation = algorithm.content_based_filtering(
                restoran_df, nama)
            nama = nama.lower()
            nama = re.sub(r'[^.,a-zA-Z0-9 \n\.]', ' ', nama)
            nama = re.sub(r'[^\w\s]', '', nama)
            nama = re.sub('[\s]+', ' ', nama)
            nama = nama.replace(" ", "")
            return redirect('/result/')
        elif request.form.get('more-result-2') == 'Other Similar Result':
            nama = request.form['result-2']
            weight_recommendation = algorithm.content_based_filtering(
                restoran_df, nama)
            nama = nama.lower()
            nama = re.sub(r'[^.,a-zA-Z0-9 \n\.]', ' ', nama)
            nama = re.sub(r'[^\w\s]', '', nama)
            nama = re.sub('[\s]+', ' ', nama)
            nama = nama.replace(" ", "")
            return redirect(url_for('specific_result', nama=nama))
        elif request.form.get('more-result-3') == 'Other Similar Result':
            nama = request.form['result-3']
            weight_recommendation = algorithm.content_based_filtering(
                restoran_df, nama)
            nama = nama.lower()
            nama = re.sub(r'[^.,a-zA-Z0-9 \n\.]', ' ', nama)
            nama = re.sub(r'[^\w\s]', '', nama)
            nama = re.sub('[\s]+', ' ', nama)
            nama = nama.replace(" ", "")
            return redirect(url_for('specific_result', nama=nama))
        else:
            pass
    elif request.method == 'GET':
        return render_template('result.html', result1=weight_recommendation[0], result2=weight_recommendation[1], result3=weight_recommendation[2])


if __name__ == '__main__':
    app.run()
