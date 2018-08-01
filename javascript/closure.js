function counter(a=0){
    var count = a;

    var countItUp = function(){
     ++count;
     return count;
    }
    return countItUp;
}

var count1 = counter(3)
var count2 = counter()
console.log(count1());
count1()
count2()
count2()
console.log(count1());
////////
function counter(a=0){
    var count = a;

    class countIt{
        constructor(a){
        this.count = a;
    }
    
    increment(){
        this.count ++;
        return this.count;
    }

    decrement(){
        this.count --;
        return this.count;
    }
}
    var countItUp = new countIt(a);
    return countItUp;
}