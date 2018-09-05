////////WEB SCRAPING

// var express = require('express');
// var app = express();
// var rp = require('request-promise');


// const promise = require('bluebird');

// // pg-promise initialization options:
// const initOptions = {
//     // Use a custom promise library, instead of the default ES6 Promise:
//     promiseLib: promise, 
// };

// // Database connection parameters:
// const config = {
//     host: 'localhost',
//     port: 3000,
//     database: 'restaurant',
//     user: 'postgres'
// };

// // Load and initialize pg-promise:
// const pgp = require('pg-promise')(initOptions);
// // Create the database instance:
// const db = pgp(config);

// Promise.all([ 'https://en.wikipedia.org/wiki/Futures_and_promises', 'https://en.wikipedia.org/wiki/Continuation-passing_style', 'https://en.wikipedia.org/wiki/JavaScript', 'https://en.wikipedia.org/wiki/Node.js', 'https://en.wikipedia.org/wiki/Google_Chrome' ])
// .then(function (responses) {
//     responses.forEach(function(e){
//         rp(e)
//         .then(function (dog) {
//             console.log(dog);
//         })
//         .catch(function (err) {
//             // Crawling failed...
//         });
//     })
    
//   });

  

// var server = app.listen(3000);

// server.on('close', function(){
//     pgp.end();
// })

//////////////////
///////// CHAINING
//////////////////

// var express = require('express');
// var app = express();
// var rp = require('request-promise');
// const fs = require('fs-extra')

// const promise = require('bluebird');

// // pg-promise initialization options:
// const initOptions = {
//     // Use a custom promise library, instead of the default ES6 Promise:
//     promiseLib: promise, 
// };

// // Database connection parameters:
// const config = {
//     host: 'localhost',
//     port: 3000,
//     database: 'restaurant',
//     user: 'postgres'
// };

// // Load and initialize pg-promise:
// const pgp = require('pg-promise')(initOptions);
// // Create the database instance:
// const db = pgp(config);

// function bringItIn(url, filename){
//     rp(url)
//         .then(function (dog) {
//             fs.outputFile(filename, dog)
//                 .then(() => fs.readFile(filename, 'utf8'))
//                 .then(data => {
//                 console.log(data) // => hello!
//             })
//             .catch(err => {
//                 console.error(err)
//             })
//         })
//     .catch(function (err) {
//         // Crawling failed..
//     });
// }

// bringItIn('https://en.wikipedia.org/wiki/Futures_and_promises', 'promiseCopy.html');

  

// var server = app.listen(3000);

// server.on('close', function(){
//     pgp.end();
// })

// ////////////////
// /////Cat 2 Files
// ////////////////

// var express = require('express');
// var app = express();
// var rp = require('request-promise');
// const fs = require('fs-extra')

// const promise = require('bluebird');

// // pg-promise initialization options:
// const initOptions = {
//     // Use a custom promise library, instead of the default ES6 Promise:
//     promiseLib: promise, 
// };

// // Database connection parameters:
// const config = {
//     host: 'localhost',
//     port: 3000,
//     database: 'restaurant',
//     user: 'postgres'
// };

// // Load and initialize pg-promise:
// const pgp = require('pg-promise')(initOptions);
// // Create the database instance:
// const db = pgp(config);

// function bringItIn2(url1, url2, filename){
//     var sURL = "";
//     rp(url1)
//         .then(function (dog) {
//             sURL += dog;
//             rp(url2)
//                 .then(function (cat) {
//                 sURL += cat;
//                 fs.outputFile(filename, sURL)
//                     .then(() => fs.readFile(filename, 'utf8'))
//                     .then(data => {
//                     console.log(data) // => hello!
//                     })
//                 })
//             .catch(function (err) {
//                 // Crawling failed..
//             });
//         })
//     .catch(function (err) {
//         // Crawling failed..
//     });
    
// }

// bringItIn2('https://en.wikipedia.org/wiki/Continuation-passing_style','https://en.wikipedia.org/wiki/Futures_and_promises', 'promiseCopy.html');

  

// var server = app.listen(3000);

// server.on('close', function(){
//     pgp.end();
// })



/////////////////
//Resolve, reject
/////////////////

var express = require('express');
var app = express();
var rp = require('request-promise');
const fs = require('fs-extra')

const promise = require('bluebird');

// pg-promise initialization options:
const initOptions = {
    // Use a custom promise library, instead of the default ES6 Promise:
    promiseLib: promise, 
};

// Database connection parameters:
const config = {
    host: 'localhost',
    port: 3000,
    database: 'restaurant',
    user: 'postgres'
};

// Load and initialize pg-promise:
const pgp = require('pg-promise')(initOptions);
// Create the database instance:
const db = pgp(config);

function addItIn(n1, n2){
    p1 = new Promise(function(resolve, reject){
        if (Number.isInteger(n1) && Number.isInteger(n2)){
            resolve(n1+n2);
        }
        reject('error');
    })
    return resolve;
}

addItIn(1, 2)
    .then(function(answer){
        return answer;
    })
    .catch(function (error) {
        console.log(error);
    });

  

var server = app.listen(3000);

server.on('close', function(){
    pgp.end();
})