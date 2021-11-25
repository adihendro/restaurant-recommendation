//set up library
const express = require('express');
const bodyParser = require('body-parser');
const port = parseInt(process.env.PORT, 10) || 3000;
const path = require('path');

//set up express app
const app = express();

//handle static content
app.use(express.static('./view'));

//handle change body to json
app.use(bodyParser.json());

//handle result page
app.get('/result', function (req, res) {
    res.sendFile(path.join(__dirname + '/result.html'));
});

//listen for request
app.listen(port, function () {
    console.log(`now listening on port ${port}`);
});



