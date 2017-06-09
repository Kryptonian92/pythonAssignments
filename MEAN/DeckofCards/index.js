function DeckConstructor(){
  var suits = ["Hearts", "Spades", "Clubs", "Diamonds"];
  var values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King"];
  var deck ;
  this.show = function(){
    console.log(deck);
    console.log("Length:", deck.length);
    return this;
  }
  var generateDeck = function(){
    deck = [];
    for(var i=0; i<suits.length; i++){
      for(var j=0; j<values.length; j++){
        // var card = {
        //   suit = suits[i];
        //   values = values[j];
        // };
          var card = new Card(suits[i], values[j]);
          deck.push(card);
        }
      }
    }
    generateDeck();

    this.shuffle= function(){
      var numbersOfShuffles = Math.floor((Math.random() * 100) + 50);
      for(var i=0; i<=numbersOfShuffles; i++){
        var randomInteger1 = Math.floor(Math.random() * deck.length);
        var randomInteger2 = Math.floor(Math.random() * deck.length);
        var temp = deck[randomInteger1];
        deck[randomInteger1] = deck[randomInteger2];
        deck[randomInteger2] = temp;
      }
      return this;
    }
    this.reset = generateDeck;
  }
  

function Card(suit, value){
  this.suit = suit;
  this.value = value;
}

var myDeck = new DeckConstructor();

// myDeck.show()

myDeck.shuffle().reset();
myDeck.show();
