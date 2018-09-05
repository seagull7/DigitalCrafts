// function isPrime(prm){
//     for(i = 2; i < prm; i ++){
//         if (prm % i == 0){
//             return false;
//         }
//     }
//     return true;
// }
// function isOddComp(odd){
//     if(odd % 2 == 1){
//         if(!isPrime(odd)){
//             return true;
//         }
//     }
//     return false;
// }
// function canYou(can){
//     for (k= 1; k < can; k ++){
//         if(isPrime(k)){
//             for (j = 1; j < can/2; j ++){
//                 if(k + 2*j*j == can ){
//                     return true;
//                 }
//             }
//         }
//     }
//     return false;
// }

// function why(){
//     for(l = 1; l = l; l ++){
//         if(isOddComp(l)){
//             if(!canYou(l)){
//                 return l;
//             }
//         }
//     }
// }

// console.log(why());

// for(i = 99; i >=0; i --){
//     let h = (i).toString()
//         let j = (i-1).toString()
//     if(i%7 ==0 && i%5 ==0){
//         console.log(h + " Bottles of Shiner Amber, take one down, pass it around, " + j + " bottles of Shiner Amber on the wall ");
//     }
//     else if(i%7 == 0){
//         console.log(h + " Bottles of Shiner, take one down, pass it around, " + j + " bottles of Shiner on the wall ");
//     }
//     else if(i%5 == 0){
//         console.log(h + " Bottles of amber ale, take one down, pass it around, " + j + " bottles of amber ale on the wall ");
//     }
//     else{
//         console.log(h + " Bottles of beer, take one down, pass it around, " + j + " bottles of beer on the wall ");

//     }
// }

function maxCakes4ME(weightCap, cakes){
    var max =0;
    var weigh = 0;
    var val = 0;
    var space = weightCap;
    var MONEY = 0;

    while(space >= 2){
        max = 0;
        for(i = 0; i < cakes.length; i ++){
            stat = 0;
                if(cakes[i].weight <= space){
                    let stat = cakes[i].value/cakes[i].weight;
                    if(stat > max){
                        max = stat
                        weigh = cakes[i].weight;
                        val = cakes[i].value;
                    }
                }
        }
        while(space >= weigh){
            space = space - weigh;
            MONEY = MONEY + val;
        }

    }
    return MONEY;
}
var cakeTypes = [
    {weight: 7, value: 160},
    {weight: 3, value: 90},
    {weight: 2, value: 15},
];

console.log(maxCakes4ME(2170, cakeTypes));