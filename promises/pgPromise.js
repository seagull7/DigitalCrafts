
var express = require('express');
var app = express();
var co = require('co');
var prompt = require('prompt-promise');

const promise = require('bluebird');

// pg-promise initialization options:
const initOptions = {
    // Use a custom promise library, instead of the default ES6 Promise:
    promiseLib: promise, 
};

// Database connection parameters:
const config = {
    host: 'localhost',
    port: 5432,
    database: 'restaurant',
    user: 'postgres'
};

// Load and initialize pg-promise:
const pgp = require('pg-promise')(initOptions);
// Create the database instance:
const db = pgp(config);
    
// db.query('SELECT * FROM restaurant')
//     .then(function(results){
//         results.forEach(function(r){
//             console.log(r.id, r.name);
//         });
//     })
//     .catch(function(error){
//         console.log(error);
//     })


    var res = [];  
    prompt('name: ')
    .then(function username(val) {
      res.push(val);
      return prompt('adress: ');
    })
    .then(function username(val) {
        res.push(val);
        return prompt('category: ');
    })
    .then(function pasword(val) {
      res.push(val);
      console.log(res);


      // INSERTION 
      db.result(`INSERT INTO restaurant
      VALUES (default, '${res[0]}', '${res[1]}', '${res[2]}')`)
      .then(function (result) {
        console.log(result);

      });
      prompt.done();
    })
    .catch(function rejected(err) {
      console.log('category:', err.stack);
      prompt.finish();
    });


  
  


  

var server = app.listen(3000);

server.on('close', function(){
    pgp.end();
})