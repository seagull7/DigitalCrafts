function Person(name, email, phone) {
    this.name = name;
    this.email = email;
    this.phone = phone;
}

Person.prototype.greet = function(other) {
    console.log('Hello ' + other.name + ', I am ' + this.name + '!');
}; 

var Sonny = new Person("Sonny", "sonny@hotmail.com", "483-485-4948");
var Jordan = new Person("Jordan", "jordan@hotmail.com", "495-486-3456");
Sonny.greet(Jordan);
Jordan.greet(Sonny);
console.log(Sonny.email, Sonny.phone);
console.log(Jordan.email, Jordan.phone);

//////////
function Card(point, suit) {
    this.point = point;
    this.suit = suit;
}
var myCard = new Card(5, 'diamonds')

console.log(myCard.point)
console.log(myCard.suit)

//////////
Card.prototype.getImageURL= function(){
    return 'JPEG/'+ this.point + this.suit + ".jpg";
}
console.log(myCard.getImageURL());

//////////
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

var myHand = new Hand()
myHand.addCard(new Card(5, 'diamonds'))
myHand.addCard(new Card(13, 'spades'))
console.log(myHand.getPoints());

//////////
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
var myDeck = new Deck();
myDeck.draw();
myDeck.draw();
myDeck.shuffle();
myDeck.numCardsLeft() ;
