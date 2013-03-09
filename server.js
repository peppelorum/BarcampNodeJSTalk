
var app = require('express').createServer();

var logic = require('./static/secret/logic');

app.get('/calc/:voltage/', function(req, res){
    
    var ret = logic.niccokick.turn27(req.params.voltage);

    res.setHeader("Content-Type", "application/json; charset=utf-8");
    res.send(ret);

});

app.listen(8020);
