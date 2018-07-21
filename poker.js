//VARIABLES
    var DC1 = document.getElementById("1d");
    var DC2 = document.getElementById("2d");
    var DC3 = document.getElementById("3d");
    var DC4 = document.getElementById("4d");
    var DC5 = document.getElementById("5d");
    var DC6 = document.getElementById("6d");
    var DC7 = document.getElementById("7d");
    var DC8 = document.getElementById("8d");
    var DC9 = document.getElementById("9d");
    var dealArray = [DC1, DC2, DC3, DC4, DC5, DC6, DC7, DC8, DC9];
    var dealerHand = [];
    // PLAYER CARDS
    var PC1 = document.getElementById("1p");
    var PC2 = document.getElementById("2p");
    var PC3 = document.getElementById("3p");
    var PC4 = document.getElementById("4p");
    var PC5 = document.getElementById("5p");
    var PC6 = document.getElementById("6p");
    var PC7 = document.getElementById("7p");
    var PC8 = document.getElementById("8p");
    var PC9 = document.getElementById("9p");
    var playArray = [PC1, PC2, PC3, PC4, PC5, PC6, PC7, PC8, PC9];
    var playerHand = [];
    //BUTTONS
    var deal = document.getElementById("deal-button");
    var hit = document.getElementById("hit-button");
    var stand = document.getElementById("stand-button");
    //FUNCTION VARS
    var pCounter = 2;
    //DECK
    var deck = [];
    //POINTS
    var dealerPoints = document.getElementById("dealer-points");
    var playerPoints = document.getElementById("player-points");

/////////////////////////////////////////////////////////
deal.onclick = function(){
    dealArray.forEach(element => {
        element.setAttribute("src", "");
    });
    playArray.forEach(element => {
        element.setAttribute("src", "");
    });
    var cardD1 = dealFunc();
    dealerHand.push(cardD1.value);
    let DC1img = "JPEG/" + cardD1.name + cardD1.suit + ".jpg"
    DC1.setAttribute("src", DC1img);

    var cardD2 = dealFunc();
    dealerHand.push(cardD2.value);
    let DC2img = "JPEG/" + cardD2.name + cardD2.suit + ".jpg"
    DC2.setAttribute("src", DC2img);

    var cardP1 = dealFunc();
    playerHand.push(cardP1.value);
    let PC1img = "JPEG/" + cardP1.name + cardP1.suit + ".jpg"
    PC1.setAttribute("src", PC1img);

    var cardP2 = dealFunc();
    playerHand.push(cardP2.value);
    let PC2img = "JPEG/" + cardP2.name + cardP2.suit + ".jpg"
    PC2.setAttribute("src", PC2img);
    pCounter = 2;
    dealerPoints.textContent= (sumArr(dealerHand));
    playerPoints.textContent= (sumArr(playerHand));
}

hit.onclick = function(){
    if(pCounter < 10){
        var cardH = dealFunc();
        playerHand.push(cardH.value);
        let Himg = "JPEG/" + cardH.name + cardH.suit + ".jpg"
        playArray[pCounter].setAttribute("src", Himg);
        pCounter ++;
        dealerPoints.textContent= (sumArr(dealerHand));
        playerPoints.textContent= (sumArr(playerHand));
    }

}

function makeCard(value, name, suit){
	this.value = value;
	this.name = name;
	this.suit = suit;
}

function makeDeck(){
    this.names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
    this.suits = ['H','D','S','C'];
    var cards = [];
    
    for( var s = 0; s < this.suits.length; s++ ) {
        for( var n = 0; n < this.names.length; n++ ) {
            cards.push( new makeCard( n+1, this.names[n], this.suits[s] ) );
        }
    }

    return cards;
}

function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
    
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
    
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
    
        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    
    return array;
}

function dealFunc(){
    if(deck.length == 0){
        deck = shuffle(makeDeck());
    }
    return deck.pop();
}
function sumArr(array, counter = [0]){
    if (array.length != 0){
        counter[0] += array.pop();
        sumArr(array, counter);
    }
    return counter[0];
}
//
var box = document.getElementById('contain');
var boxinbox = document.getElementById('center');
var pop = document.createElement("img");