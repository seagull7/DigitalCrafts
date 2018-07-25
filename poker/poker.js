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
    var popUpMessage = document.getElementById("popUpMessage");
    var continueButton = document.getElementById("continue-button");
    var overButton = document.getElementById("over-button");
    var bet5 = document.getElementById("bet5");
    var bet10 = document.getElementById("bet10");
    var allIn = document.getElementById("allIn");
    var betDown5 = document.getElementById("bet-5");
    var betButtons = document.getElementById("betButtons");
    var done = document.getElementById("done");
    //FUNCTION VARS
    var pCounter = 2;
    var popUpMessage = document.getElementById("popUpMessage");
    var popUpImage = document.getElementById("popUpImage");
    var dCounter = 3;
    var cardD1 =[]
    //DECK
    var deck = [];
    var green = document.getElementById("green")
    //POINTS
    var dealerPoints = document.getElementById("dealer-points");
    var playerPoints = document.getElementById("player-points");
    var dealerWins = document.getElementById("dealer-wins");
    var playerWins = document.getElementById("player-wins");
    var playerWinCounter = 0;
    var dealerWinCounter = 0;
    //$$$
    var cash = document.getElementById("cash");
    var balance = 500;
    var currentBet = document.getElementById("currentBet");
    var betBalance = 0;

/////////////////////////////////////////////////////////
cash.textContent= balance;
overButton.onclick = function(){
    overButton.setAttribute("style", "visibility: hidden;")
    betButtons.setAttribute("style", "visibility: visible;")
}

bet5.onclick = function(){
    if (balance >= 5){
        betBalance += 5;
        balance -= 5;
        cash.textContent = balance;
        currentBet.textContent = betBalance;
    }
    else{
        alert("You dont have that much money left.")
    }
}

bet10.onclick = function(){
    if (balance >= 10){
        betBalance += 10;
        balance -= 10;
        cash.textContent = balance;
        currentBet.textContent = betBalance;
    }
    else{
        alert("You dont have that much money left.")
    }
}

allIn.onclick = function(){
    if (balance >= 0){
        betBalance += balance;
        balance = 0;
        cash.textContent = balance;
        currentBet.textContent = betBalance;
    }
    else{
        alert("You have no money left.")
    }
}

betDown5.onclick = function(){
    betBalance -= 5;
    balance +=5;
    cash.textContent = balance;
    currentBet.textContent = betBalance;
}

done.onclick = function(){
    betButtons.setAttribute("style", "visibility: hidden;")
}

deal.onclick = function(){

    dealerHand = [];
    playerHand = [];
    dealerPoints.textContent= "";

    dealArray.forEach(element => {
        element.setAttribute("src", "");
    });
    playArray.forEach(element => {
        element.setAttribute("src", "");
    });
    cardD1 = dealFunc();
    dealerHand.push(cardD1.value);
    let DC1img = "JPEG/Gray_back.jpg"
    DC1.setAttribute("src", DC1img);
    move(DC1);

    var cardD2 = dealFunc();
    dealerHand.push(cardD2.value);
    let DC2img = "JPEG/" + cardD2.name + cardD2.suit + ".jpg"
    DC2.setAttribute("src", DC2img);
    move(DC2);


    var cardP1 = dealFunc();
    playerHand.push(cardP1.value);
    let PC1img = "JPEG/" + cardP1.name + cardP1.suit + ".jpg"
    PC1.setAttribute("src", PC1img);
    move(PC1);


    var cardP2 = dealFunc();
    playerHand.push(cardP2.value);
    let PC2img = "JPEG/" + cardP2.name + cardP2.suit + ".jpg"
    PC2.setAttribute("src", PC2img);
    move(PC2);
    pCounter = 2;
    playerPoints.textContent= (playerHand.reduce(getSum));
    if (playerHand.reduce(getSum) == 21){
        playerWin();
    }

}

hit.onclick = function(){
    if(dealerHand.length== 0){
        alert("you havent even asked the dealer to deal yet...")
    }
    else{
        if(pCounter < 10){
            var cardH = dealFunc();
            playerHand.push(cardH.value);
            let Himg = "JPEG/" + cardH.name + cardH.suit + ".jpg"
            playArray[pCounter].setAttribute("src", Himg);
            move(playArray[pCounter]);
            pCounter ++;
            playerPoints.textContent= (playerHand.reduce(getSum));
        }
        if(playerHand.reduce(getSum) > 21 ){
            if (playerHand.indexOf(11) !== -1) {
                    playerHand[playerHand.indexOf(11)] = 1;
                    playerPoints.textContent= (playerHand.reduce(getSum));
                }
            else{
                popUpImage.setAttribute("src", "https://media3.giphy.com/media/l0ExeAkpaMaEAuX5e/giphy.gif");
                popUpMessage.setAttribute("style", "visibility: visible;");
                dealerWinCounter ++
                dealerWins.textContent= (dealerWinCounter);
                betBalance = 0;
                cash.textContent = balance;
                currentBet.textContent = betBalance;
            }
        }
    }
}

stand.onclick = function(){
    if(dealerHand.length == 0){
        alert("you havent even asked the dealer to deal yet...")
    }
    else{
        let DCsimg = "JPEG/" + cardD1.name + cardD1.suit + ".jpg"
        DC1.setAttribute("src", DCsimg);
        dCounter =3;
        while(dealerHand.reduce(getSum) < 17){
            var cardS = dealFunc();
            dealerHand.push(cardS.value);
            let Simg = "JPEG/" + cardS.name + cardS.suit + ".jpg"
            dealArray[dCounter].setAttribute("src", Simg);
            move(dealArray[dCounter]);
            dealerPoints.textContent= (dealerHand.reduce(getSum));
            dCounter ++;
        }
        if(dealerHand.reduce(getSum) > 21 ){
            if (dealerHand.indexOf(11) !== -1) {
                dealerHand[dealerHand.indexOf(11)] = 1;
                dealerPoints.textContent= (dealerHand.reduce(getSum));
            }
            else{
                popUpImage.setAttribute("src", "https://media0.giphy.com/media/3orif9LivxKZv58qWs/giphy.gif");
                popUpMessage.setAttribute("style", "visibility: visible;");
                playerWinCounter ++;
                playerWins.textContent= (playerWinCounter);
                balance += betBalance*2;
                betBalance = 0;
                cash.textContent = balance;
                currentBet.textContent = betBalance;
            }
        }
        else if(dealerHand.reduce(getSum) > playerHand.reduce(getSum)){
            dealerWin();
        }
        else if(playerHand.reduce(getSum) > dealerHand.reduce(getSum)){
            playerWin();
        }
        else if(playerHand.reduce(getSum) == dealerHand.reduce(getSum)){
            tie();
        }
    }

}

continueButton.onclick = function(){
    popUpMessage.setAttribute("style", "visibility: hidden");
    dealArray.forEach(element => {
        element.setAttribute("src", "");
    });
    playArray.forEach(element => {
        element.setAttribute("src", "");
    });
    overButton.setAttribute("style", "visibility: visible");
    if(betBalance == 0 && balance  == 0){
        green.setAttribute("src", "https://media1.giphy.com/media/Krhe4z5Vy3tRe/giphy.gif")
    }
    playArray.forEach(element =>{
        element.setAttribute("style", "height: 0px;")
    });
    dealArray.forEach(element =>{
        element.setAttribute("style", "height: 0px;")
    });
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
            if(this.names[n] == "J" || this.names[n] == "Q" || this.names[n] == "K"){
                cards.push( new makeCard( 10, this.names[n], this.suits[s] ) );
            }
            else if (this.names[n] == "A"){
                cards.push( new makeCard( 11, this.names[n], this.suits[s] ) );
            }
            else{
                cards.push( new makeCard( n+1, this.names[n], this.suits[s] ) );
            }
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

function getSum(total, num) {
    return total + num;
}

function playerWin(){
    playerWinCounter ++;
    playerWins.textContent= (playerWinCounter);
    popUpImage.setAttribute("src", "https://media0.giphy.com/media/ToMjGpyO2OVfPLpoxu8/giphy.gif");
    popUpMessage.setAttribute("style", "visibility: visible;");
    balance += betBalance*2;
    betBalance = 0;
    cash.textContent = balance;
    currentBet.textContent = betBalance;
}

function dealerWin(){
    dealerWinCounter ++;
    dealerWins.textContent= (dealerWinCounter);
    popUpImage.setAttribute("src", "https://media3.giphy.com/media/EndO2bvE3adMc/giphy.gif");
    popUpMessage.setAttribute("style", "visibility: visible;");
    betBalance = 0;
    cash.textContent = balance;
    currentBet.textContent = betBalance;
}

function tie(){
    popUpImage.setAttribute("src", "https://media1.giphy.com/media/143SWpDkGbQkus/giphy.gif");
    popUpMessage.setAttribute("style", "visibility: visible;");
}
function move(a){
    a.setAttribute("style", "height: 100%;")
}
//

function Card(point, suit) {
    this.point = point;
    this.suit = suit;
}

Card.prototype.getImageURL= function(){
    return 'JPEG/'+ this.point + this.suit + ".jpg";
}

function Hand() {
    this.cards = [];
}

Hand.prototype.addCard = function(card) {
    this.cards.push(card);
}

Hand.prototype.getPoints = function() {
    var self = this;
    var points = self.cards.map(function(e) {
        return e.point;
    });
    points.reduce(function(a, b) {
        return a + b;
    });
}

function Deck(){
    this.deck =[];
}

Deck.prototype.draw = function(){
    let cardIndex = Math.floor(Math.random()*deck.length);
    var randCard = deck[cardIndex];
    randCard.splice(cardIndex, 1);
    return randCard;
}

Deck.prototype.shuffle = function() {
    for (var i = this.deck.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = this.deck[i];
        this.deck[i] = this.deck[j];
        this.deck[j] = temp;
    }
    return this.deck;
}

Deck.prototype.numCardsLeft = function() {
    return this.deck.length;
}
