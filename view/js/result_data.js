var resultData = '{"rest_1": "Hause Rooftop", "rest_2": "The Neighbourhood", "rest_3": "SKYE"}';
let jsonData = JSON.parse(resultData);
const resultDiv_1 = document.getElementById('result-content-1');
resultDiv_1.innerText = jsonData.rest_1;
const resultDiv_2 = document.getElementById('result-content-2');
resultDiv_2.innerText = jsonData.rest_2;
const resultDiv_3 = document.getElementById('result-content-3');
resultDiv_3.innerText = jsonData.rest_3;
