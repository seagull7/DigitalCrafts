var deck = [];

function deal(){
    if(deck.length == 0){
        deck = shuffle(makeDeck());
    }
    return deck.pop();
}

function makeCard(value, name, suit){
	this.value = value;
	this.name = name;
	this.suit = suit;
}

function makeDeck(){
    this.names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
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



console.log(deal())