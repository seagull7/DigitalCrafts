
//Positive Numbers
function positiveNumbers(array, newArray= []){
    if (array.length != 0){
        if(array[array.length-1] >= 0){
            newArray.push(array.pop());
        }
        else{
            array.pop();
        }
    positiveNumbers(array, newArray);
    }
    return newArray;
}

//Even Numbers
function sqrNumbers(array, newArray= []){
    if (array.length != 0){
        sqr = array[array.length-1] * array[array.length-1]
        newArray.unshift(sqr);
        array.pop();
        sqrNumbers(array, newArray);
    }
    return newArray;
}

//Square Numbers
var sqrArray = arr.map(function(element){
    return(element * element);
})
//function sqrNumbers(array, temp= -30){
    // if (array[array.length-1].temperature > temp){
    //     temp = array[array.length-1].temperature;
    // }
    // array.pop();
    // sqrNumbers(array, temp);
    // return temp;
    // var cray = array[array.length-1].temperature;
    // if(cray > temp){
    //     array.pop();
    //     sqrNumbers(array, temp)
    //     return cray;
    // }
//}


//Cities 1
var arr = [ { name: 'Los Angeles', temperature: 60.0}, { name: 'Atlanta', temperature: 52.0 }, { name: 'Detroit', temperature: 48.0 }, { name: 'New York', temperature: 80.0 } ]

var newArray = arr.filter(function(element){
    if (element.temperature < 70){
        return element;
    }
})

//Cities 2
var newArray2 = arr.map(function(element){
    return element["name"];
});

//Good Job
function goodJob(array){
    if(array.length != 0){
        console.log("Good Job, " + array.pop() + "!")
        goodJob(array);
    }
}

//Sort Array
var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ]; 
console.log(people.sort())

//Sort Array 2
people.sort(function( b, a){
    return b.length - a.length;
  });
console.log(people);

//Sort Array 3
var arrs = [ [1, 3, 4], [2, 4, 6, 8], [3, 6] ];
arrs.sort(function(b, a){
    return b.reduce((a, b) => a + b) - a.reduce((a, b) => a + b)
});

//3 Times
function fun(){
    console.log("Hello World");
}
function call3Times(fun){ fun(); fun(); fun(); } 

//N times
function fun(){
    console.log("Hello World");
}
function callNTimes(n, fun= fun){ for(i = 0; i < n; i ++){ fun()} } 

//Sum and Array
function count(array, counter = [0]){
    if (array.length != 0){
        counter[0] += array.pop();
        count(array, counter);
    }
    return counter[0];
}

//Acronym
// var acrony= ['very', 'important', 'person']
// function acronym(array){
//     array.reduce((a, b) => { return a + b[0];})}
// console.log(acronym(acrony))
function acronym (arr) {
    acroArr = [];
    for (var i=0; i<arr.length; i++) {
      acroArr.push(arr[i][0]);
    }
    return acroArr.join("");
  }
  