// var readline = require('readline');
// var fs = require('fs');
// var dns = require('dns');

// var rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// rl.question("filename: ", function(answer) {
//     fs.readFile(answer, function (error, buffer) {
//         if (error) {
//             console.error(error.message);
//             return;
//         }
//         console.log(buffer.toString().toUpperCase());
//         rl.close();
//     });
// });

///////////////
// var readline = require('readline');
// var fs = require('fs');
// var dns = require('dns');

// var rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout
// });

// rl.question("Domain name: ", function(answer) {
//     dns.lookup(answer, (err, address, family) => {
//         console.log('IP Address: '+ address);
//       });
// });

///////////////
// var readline = require('readline');
// var fs = require('fs');

// var rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
//   });

// rl.question("Input File: ", function(answer) {
//     fs.readFile(answer, function (error, buffer) {
//         if (error) {
//             console.error(error.message);
//             return;
//         }
//         rl.question("Output File: ", function(answer2) {
//             rl.close;
//             var txt = buffer.toString();
//             fs.writeFile(answer2, txt, function (error) {
//                 if (error) {
//                   console.error(error.message);
//                   return;
//                 }
//                 console.log('Wrote to file: ', answer2);
//             });
//         });
//         rl.close();
//     });
// });
///////////////
var readline = require('readline');
var request = require('request');
var fs = require('fs');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('URL: ', function(url) {
  request.get(url, function(err, response, html) {
    if (err) {
      console.log(err.message);
      return;
    }
    rl.question('Filename: ', function(filename) {
      rl.close();
      fs.writeFile(filename, html, function(err) {
        if (err) {
          console.log(err.message);
          return;
        }
        console.log('Saved to ' + filename + '.');
      });
    });
  });
});
