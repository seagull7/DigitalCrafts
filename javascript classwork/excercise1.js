function lvl1exercise1() {
    // Declare a variable without instantiating it and return it.
    var itsaMe;
    return itsaMe

}

function lvl1exercise2() {
    // Declare and instantiate a number and return it
    var count = 4;
    return count;

}

function lvl1exercise3() {
    // Declare and instantiate a floating point number that isn't a whole number and return it
    var count = 4.5;
    return count;

}

function lvl1exercise4() {
    // Declare and instantiate a string "Hello World!" and return it
    var greeting = "Hello World";
    return greeting;

}

function lvl1exercise5() {
    // Declare and instantiate an array containing the string "Hello World!" and the number 4 and return it
    var greeting = "Hello World" + 4;
    return greeting;

}

function lvl1exercise6() {
    // Declare and instantiate an object containing the key-value pairs key1 -> "Hello World!" and key2 -> 4, and return it
    var combo = {
        key1: 'Hello World',
        key2: 4,
    }
    return combo;
    
}

function lvl1exercise7() {
    // Declare and instantiate a boolean value 'false' and return it
    var liar = false;
    return liar;

}

function lvl2exercise1(num1, num2) {
    // Return the sum of num1 and num2
    return (num1 + num2);

}

function lvl2exercise2(num1, num2) {
    // Return the difference of num1 and num2
    return(num1 - num2);

}

function lvl2exercise3(num1, num2) {
    // Return the multiplication of num1 and num 2
    return(num1 * num2);

}

function lvl2exercise4(num1, num2) {
    // Return the division of num1 and num2
    return(num1 / num2);

}

function lvl2exercise5(num1) {
    // Add 2 to num1 using += and return it
    num1 +=2;
    return num1;
	
}

function lvl3exercise1() {
    // Create a "hello" and a "world", return the concatenation of the two
    var earth = "World";
    var yo = "Hello";
    return yo + earth;

}

function lvl3exercise2() {
    // Create a "hello" and a 12, return the concatenation of the two
    var earth = "World";
    var aggie = 12;
    return yo + earth;

}

function lvl3exercise3() {
    // Create a variable that equals 12 and convert it to a string with concatenation. Return it.
    var aggie = 12;
    var sAggie = "" + aggie;
    return sAggie;

}

function lvl3exercise4() {
    // Create a "hello world!" string. Return the length of the string
    var yoEarth = "Hello World!"
    return yoEarth.length;

}

function lvl3exercise5() {
    // Create a "hello world!" string. Return the index of the word "world".
    var yoEarth = "Hello World!"
    return yoEarth.indexOf(World)
	
}

function lvl4exercise1() {
    // Return the boolean value "true"
    return true;
	
}

function lvl4exercise2() {
    // Return the boolean value "false"
    return false;

}

function lvl4exercise3(bool) {
    // Return the opposite of the input boolean value
    var oBool = true;
    if(bool == true){
        oBool = false;
    }
    return oBool

}

function lvl4exercise4(bool1, bool2) {
    // Return the logical "and" of the input boolean values
    return (bool1 && bool2);

}

function lvl4exercise5(bool1, bool2) {
    // Return the logical "or" of the input boolean values
    return (boo1 || bool2);
	
}

function lvl4exercise6(bool1, bool2) {
    // Return the logical "equivalence" of the input boolean values
    return ( bool1 == bool2);
	
}

function lvl5exercise1() {
	// Push the string "hello" into the array and return it.
    var array = [1, "adam"];
    array[0] = "hello"
    return array;
	
}

function lvl5exercise2() {
	// Remove the last element from the array and return it
    var array = [1, "adam"];
    array.pop();
    return array;

}

function lvl5exercise3() {
	// Return the length of the array
    var array = [1, "adam"];
    return array.length;

}

function lvl5exercise4() {
	// Return the index of "adam" in the array
    var array = [1, "adam"];
    return array.indexOf("adam");

}

function lvl6exercise1(num) {
    // Return 'hello' if num is 1, 'world' if num is 2, otherwise return'bye'
    if(num == 1){
        return "hello"
    }
    else if (num == 1){
        return "world"
    }
    else{
        return "bye"
    }
	
}

function lvl6exercise2() {
	// Push 10 "hello" strings into the array using a for loop, then return it
    var array = [];
    for(i = 0; i < 10; i++){
        array.push("hello");
    }
    return array;

}

function lvl6exercise3() {
	// Empty this array using a while loop and return it
    var array = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"];
    var i = 0;
    while(i <10){
        array.pop()
    }
    return array;

}

function finalFunction(numberInput){
    var array = []
    for(i = 0; i < numberInput; i++){
        array.push("a string");
    }
    return array;
}

function printSquare(factor){
    var line = ""
    for(i = 0; i < factor; i ++){
        for(j = 0; j < factor; j++){
            line += "*"
        }
        console.log(line);
        line = ""
    }
}