class Person {
    constructor(name){
    this.name = name;
    this.friends = [];
    }
    addFriend(friend){
        this.friends.push(friend);
    }
    createGreeting(other){
        return ('Yo ' + other.name + '! from ' + this.name + '.');
    };
    lazyGreet(other){
        setTimeout(
            function() {
                console.log('Yo ' + other.name + '! from ' + this.name + '.');
            }, 2000);
    };
    createGreetingsForFriends(){    
        this.friends.map(function(e) {
            console.log("Yo " + e.name + "! From " + this);
        });
    }
}
var alfie = new Person('Alfie');
var anushka = new Person('Anushka');
var henrique = new Person('Henrique');
alfie.addFriend(anushka); 
alfie.addFriend(henrique);
alfie.createGreetingsForFriends(); 
alfie.lazyGreet(anushka);