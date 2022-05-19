const express = require("express");
//const 

let app = express()
let port = app.listen(5050)


app.get('/', function(req, res) {
    res.sendFile(__dirname + "/index.html")
})

app.listen(port, function() {
    console.log('start! express server');
})

