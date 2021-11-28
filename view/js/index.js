const find = document.getElementById("button-find");
const form = document.querySelector("form");
const prioritas1 = document.getElementById("prioritas1");
const prioritas2 = document.getElementById("prioritas2");
const prioritas3 = document.getElementById("prioritas3");

find.addEventListener("click", postFind);
async function postFind() {
    const lokasi = form.lokasi.value;
    const jenis = form.jenis.value;
    const prioritas = [prioritas1.innerHTML, prioritas2.innerHTML, prioritas3.innerHTML];
    const data = {
        "lokasi": lokasi,
        "jenis": jenis,
        "prioritas1": prioritas[0],
        "prioritas2": prioritas[1],
        "prioritas3": prioritas[2],
    };
    console.log(data)

    // window.location.href = '/result'
}