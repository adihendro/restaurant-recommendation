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

var dragPrioritas = document.getElementsByClassName("prioritas");
function draggablePrioritas() {
    for (i = 0; i < dragPrioritas.length; i++) {
        dragPrioritas[i].draggable = true
        dragPrioritas[i].ondragstart = (e) => { dragStart(e) }
        dragPrioritas[i].ondragend = (e) => { dragEnd(e) }
        dragPrioritas[i].ondragenter = (e) => { dragEnter(e) }
        dragPrioritas[i].ondragover = (e) => { dragOver(e) }
        dragPrioritas[i].ondragleave = (e) => { dragLeave(e) }
        dragPrioritas[i].ondrop = (e) => { drop(e) }
    }
}

function dragStart(e) {
    e.target.classList.add("drag-start");
    e.dataTransfer.setData("text", e.target.id);
}

function dragEnd(e) {
    e.target.classList.remove("drag-start");
}

function dragEnter(event) {
    if (!event.target.classList.contains("drag-start")) {
        event.target.classList.add("drag-enter");
    }
}

function dragOver(e) {
    e.preventDefault();
}

function dragLeave(e) {
    e.target.classList.remove("drag-enter");
}

function drop(e) {
    e.preventDefault();
    e.target.classList.remove("drag-enter");

    var sourceElementId = e.dataTransfer.getData("text");
    var sourceElement = document.getElementById(sourceElementId);
    var targetElement = e.target.innerHTML;

    e.target.innerHTML = sourceElement.innerHTML;
    sourceElement.innerHTML = targetElement;

    e.target.classList.remove("drag-start");
}

draggablePrioritas();

// areas.forEach(populateLokasi)
// types.forEach(populateJenis)