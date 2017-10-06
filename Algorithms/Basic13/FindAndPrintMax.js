// the following algorithim will find and print
//the largest element in a given array

function printArrayMax(arr){
  var newArray = [1,4,22343,7,334,7789]
  if(newArray.length == 0){
    console.log("Empty array, no max value");
    return;
  }
  var max = 0;
  for (var i = 1; i< newArray.length; i++){
    if (newArray[i] > max){
      max = newArray[i];
    }
  }
  console.log("Max value is:" + max);
}
return printArrayMax();
