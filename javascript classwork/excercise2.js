function madLib(name, subject){
    return name + "\'s favorite subject in school is " + subject + ".";
}

function tipAmount(bill, service){
    var levelOf = {
        "good" : .2,
        "fair" : .15,
        "bad" : .1,
    }
    return (bill * levelOf[service]);

}

function tipTotal(bill, service){
    return bill + tipAmount(bill, service);
}

function printNumbers(first, last){
    for(first; first <= last; first ++){
        console.log(first);
    }
}

function printNumbers(first, last){
    var start = first;
    while(start <= last){
        console.log(start);
        start ++;
    }
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

function printSquare(factor){
    var line = "";
    var side = "*";
    for(i = 0; i < factor; i ++){
        line += "*";
    }
    console.log(line);
    for(i = 0; i < factor-2; i ++){
        side += " ";
    }
    side += "*";
    for(i = 0; i < factor-2; i ++){
        console.log(side);
    }
    console.log(line);
}

function printBanner(banner){
    var line = "";
    var side = "* " + banner + " *";
    for(j = 0; j < banner.length + 4; j++){
        line += "*";
    }
    console.log(line);
    console.log(side);
    console.log(line);
}

function leetSpeak(leet){
    var dic = {
        "A" : "4",
        "E" : "3",
        "G" : "6",
        "I" : "1",
        "O" : "0",
        "S" : "5",
        "T" : "7",
    }
    var rtrn = ""
    for (i = 0; i < leet.length; i ++){
        if(leet.charAt(i).toUpperCase() in dic){
            rtrn += dic[leet.charAt(i).toUpperCase()];
        }
        else{
            rtrn += leet.charAt(i)
        }
    }
    return rtrn;
}

function LongVowels(input){
    var rtrn = "";
    for (i = 0; i < input.length; i ++){
        if(input.charAt(i) == input.charAt(i+1)){
            rtrn += input.charAt(i) + input.charAt(i) + input.charAt(i) + input.charAt(i);
        }
        else{
            rtrn += input.charAt(i);
        }
    }
    return rtrn;
}

function positiveNumbers(array){
    var nArray = [];
    for (i = 0; i < array.length; i ++){
        if(array[i] >= 0){
            nArray.push(array[i])
        }
    }
    return nArray;
}

function CaesarCipherEncode(str, offset) {
    var nstr = ""
    var a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for (i in str){
        nstr += ((a[(a.indexOf(str.charAt(i).toUpperCase()) + offset) % 26]))
    }
    return nstr
}

function CaesarCipherDecode5(str, offset) {
    var nstr = ""
    var a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for (i in str){
        nstr += ((a[(a.indexOf(str.charAt(i).toUpperCase()) + 26 - offset) % 26]))
    }
    return nstr
}