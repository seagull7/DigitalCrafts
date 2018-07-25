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
console.log(makeDeck());