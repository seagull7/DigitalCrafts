
function add (x, y, callback) {
    setTimeout(function () {
    var result = x + y;
    callback(result);
    }, 3000);
}
 
 function subtract(x, y, callback) {
    setTimeout(function () {
    var result  = x - y
    callback(result);
    }, 3000);;
 }
 
 function greeting(person, callback) {
    setTimeout(function () {
    var result = 'Hola, ' + person + '!';
    callback(result);
    }, 3000);
 }
 
 function product(numbers, callback) {
    setTimeout(function () {
    var result = numbers.reduce(function(a, b) {
       return a * b;
    }, 3000);
    }, 1);
     callback(result);
 } 




