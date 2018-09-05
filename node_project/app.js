let express = require('express');
let app = express();
let data = require('./data/data.json');
app.set('view engine', 'ejs');
app.set('appData', data);





var http = require('http').Server(app);
var io = require('socket.io')(http);

app.use(express.static('public'));
io.on('connection', function(socket){
    socket.on('chat message', function(msg){
        io.emit('chat message', msg);
        console.log(msg);
    });
  });

//   io.on('incoming', function(msg){
//     io.emit('chat message', msg);
//   });






app.locals.siteTitle = "Roux Meetups";



app.use(require('./routes/index'));
app.use(require('./routes/doges'));
app.use(require('./routes/feedback'));
app.use(require('./routes/api'));
app.use(require('./routes/chat'));

http.listen(3000, ()=>{
    console.log("listening on port 3000");

})