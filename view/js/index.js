const find = document.getElementById("button-find");
find.addEventListener("click", postFind);
const form = document.querySelector("form");

const areas =
    ["Setiabudi", "Dharmawangsa", "Thamrin", "Senopati", "SCBD", "Fatmawati", "Kemang", "Sudirman",
        "Menteng", "Blok M", "Kuningan", "Melawai", "Bogor Utara", "Gandaria", "Cikini", "Senayan",
        "Tebet", "Pluit", "Cilandak", "Kelapa Gading", "Bogor Timur", "Pantai Indah Kapuk", "Ancol",
        "Karet", "Tanjung Duren", "Pondok Melati", "Cisarua", "Bendungan Hilir", "Tanah Sareal", "Jagakarsa",
        "Serpong Utara", "Tanah Abang", "Pinang"
    ]

const types =
    ["Casual Dining", "Fine Dining", "Café", "Lounge", "Quick Bites", "Bar", "Dessert Parlor", "Food Court", "Indonesian",
        "Japanese", "Asian", "Desserts", "Steak", "Western", "Italian", "Peranakan", "Wine Bar", "Burger", "Cafe", "Coffee", "Korean",
        "Grill", "Sushi", "Continental", "Jawa", "Spanish", "Fusion", "Betawi", "Seafood", "Ice Cream", "Pizza", "Bakery", "Arabian",
        "Sunda", "BBQ", "European", "French", "Peruvian", "Ramen", "Finger Food", "German", "Indian", "American", "South American",
        "Healthy Food", "Tea", "North Indian", "Australian", "Chinese", "Middle Eastern", "Dimsum", "Beverages", "Snacks", "Kebab",
        "Moroccan", "Belanda", "Thai"
    ]

function populateLokasi(n) {
    var ul = document.getElementById("lokasi");
    populateOption(n, ul);
}
function populateJenis(n) {
    var ul = document.getElementById("jenis");
    populateOption(n, ul);
}

function populateOption(n, ul) {
    var li = document.createElement("option");
    li.appendChild(document.createTextNode(n));
    li.setAttribute("value", n);
    ul.appendChild(li);
}

// prioritas = ["Lokasi", "Jenis", "Rating"]

// function populatePrioritas() {
//     var ul = document.getElementsByClassName("prioritas");
//     console.log(ul)
//     var li = document.createElement("option");
//     li.appendChild(document.createTextNode(prioritas[0]));
//     li.appendChild(document.createTextNode(prioritas[1]));
//     li.appendChild(document.createTextNode(prioritas[2]));
//     li.setAttribute("value", prioritas[0]);
//     li.setAttribute("value", prioritas[]);
//     li.setAttribute("value", prioritas[2]);
//     ul[0].appendChild(li);
//     ul[1].appendChild(li);
//     ul[2].appendChild(li);
// }

areas.forEach(populateLokasi)
types.forEach(populateJenis)
// populatePrioritas()



async function postFind() {
    const lokasi = form.lokasi.value;
    const jenis = form.jenis.value;
    const prioritas = [form.prioritas1.value, form.prioritas2.value, form.prioritas3.value];
    const data = {
        "lokasi": lokasi,
        "jenis": jenis,
        "prioritas1": prioritas[0],
        "prioritas2": prioritas[1],
        "prioritas3": prioritas[2],
    };

    window.location.href = '/result'
}