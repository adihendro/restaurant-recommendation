const find = document.getElementById("button-find");
find.addEventListener("click", postFind);
const form = document.querySelector("form");

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
    console.log(data)
    // window.location.href = '/result'
}