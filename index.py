from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    areas = ["Setiabudi", "Dharmawangsa", "Thamrin", "Senopati", "SCBD", "Fatmawati", "Kemang", "Sudirman",
        "Menteng", "Blok M", "Kuningan", "Melawai", "Bogor Utara", "Gandaria", "Cikini", "Senayan",
        "Tebet", "Pluit", "Cilandak", "Kelapa Gading", "Bogor Timur", "Pantai Indah Kapuk", "Ancol",
        "Karet", "Tanjung Duren", "Pondok Melati", "Cisarua", "Bendungan Hilir", "Tanah Sareal", "Jagakarsa",
        "Serpong Utara", "Tanah Abang", "Pinang"]

    types = ["Casual Dining", "Fine Dining", "Café", "Lounge", "Quick Bites", "Bar", "Dessert Parlor", "Food Court", 
        "Indonesian", "Japanese", "Asian", "Desserts", "Steak", "Western", "Italian", "Peranakan", "Wine Bar", "Burger", 
        "Cafe", "Coffee", "Korean", "Grill", "Sushi", "Continental", "Jawa", "Spanish", "Fusion", "Betawi", "Seafood", "Ice Cream", 
        "Pizza", "Bakery", "Arabian", "Sunda", "BBQ", "European", "French", "Peruvian", "Ramen", "Finger Food", "German", "Indian", 
        "American", "South American", "Healthy Food", "Tea", "North Indian", "Australian", "Chinese", "Middle Eastern", "Dimsum", 
        "Beverages", "Snacks", "Kebab", "Moroccan", "Belanda", "Thai"]

    if request.method == 'POST':
        if request.form.get('cari-restoran') == 'Cari Restoran':
            return redirect('/result')
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html', areas=areas, types=types)
    
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        if request.form.get('kembali') == 'Kembali':
            return redirect('/')
        else:
            pass
    elif request.method == 'GET':
        return render_template('result.html')

    return render_template('result.html')

if __name__ == '__main__':
    app.run()