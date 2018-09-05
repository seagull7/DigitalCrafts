// var summary = 0;
// for( i = 2; i < process.argv.length; i++){
//     summary += Number(process.argv[i]);
// }

// var fs = require('fs') ;
// fs.readdir(process.argv[2], (err, data) => {
//     if (err) throw err;
//     for(i = 0 ; i < data.length; i ++){
//         if (data[i].toString().indexOf(".md") > -1){
//             console.log(data[i]);
//         }
//     }
//   });
var fs = require('fs')
var path = require('path')

var folder = process.argv[2]
var ext = '.' + process.argv[3]

fs.readdir(folder, function (err, files) {
  if (err) return console.error(err)
  files.forEach(function (file) {
    if (path.extname(file) === ext) {
      console.log(file)
    }
  })
})

// var fs = require('fs')  
// var result = fs.readFile(process.argv[2]).toString().split("\n").length - 1
// console.log(result);