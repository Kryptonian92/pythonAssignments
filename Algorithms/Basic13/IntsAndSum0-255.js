//The following program will print integers from 0 to 255, and the sum so far

var num = 1;
var sum = 0;
while(num < 256){
  sum+=num;
  console.log("Current Number:" + num + "The Sum is:" + sum)
  num+=1;
}

// OR

function printIntsAndSum0to255(){
  var sum = 0;
  for (var num = 0; num <= 255; num++){
    sum += num;
    console.log("new number:" + num + "Sum:" + sum );
  }
}
