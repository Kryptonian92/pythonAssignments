
// Create a simple for loop that sums all the integers between x and y (inclusive). Have it console log the final sum.
function findSum(x, y){
  var sum=0;
  for (var i=x; i<=y; i++){
    sum+=i
    console.log(i);
  }
  console.log(sum);
}
return sum;

// Write a loop that will go through an array, find the minimum value, and then return it
function findMin(arr) {
    if (arr) {
        var min = arr[0];
        for (var i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
}

// Write a loop that will go through an array, find the average of all of the values, and then return it
function findAvg(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum / arr.length;
}

//rewrite the previous 3 as anon functions
// function 1
var findsum = function(x, y) {
    var sum = 0;
    for (var i = x; i < y + 1; i++) {
        sum += i;
    }
    return sum;
};

// function 2
var findAvg = function(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum / arr.length;
};

// function 3
var findMin = function findMin(arr) {
    if (arr) {
        var min = arr[0];
        for (var i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
};

//rewrite the previous 3 as methods of an object
//function 1
var myObject = {
    sumXY: function(x, y) {
        var sum = 0;
        for (var i = x; i < y + 1; i++) {
            sum += i;
        }
        return sum;
    }, //end sumxy
    findAvg: function(arr) {
        var sum = 0;
        for (var i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum / arr.length;
    }, //end findAvg
    findMin: function findMin(arr) {
        if (arr) {
            var min = arr[0];
            for (var i = 1; i < arr.length; i++) {
                if (arr[i] < min) {
                    min = arr[i];
                }
            }
            return min;
        }
    }// end find min
}//end object


var person = {
  name : "Charlie",
  distance_traveled : 0,
  say_name : function(){
    console.log(person.name);
  },
  say_something : function(phrase){
    console.log(`${person.name} says: ${phrase}`);
  },
  walk : function(){
    console.log(`${person.name} is walking!`);
    person.distance_traveled += 3;
    return person;
  },
  run : function(){
    console.log(`${person.name} is running!`);
    person.distance_traveled += 10;
    return person;
  },
  crawl : function(){
    console.log(`${person.name} is crawling!`);
    person.distance_traveled += 1;
    return person;
  },
  chewGum:function(){
    console.log("I can walk and chew gum, but I can't chew gum and walk...");
  }
}

person.walk().chewGum(); // why can I do this?
// but not this:
// person.chewgum().walk();
Files
