// the following algorithim will find and print
//the largest element in a given array

function printArrayMax(arr){
  if(arr.length == 0){
    console.log("Empty array, no max value");
    return;
  }
  var max = arr[0];
  for (var idx = 1; idx< arr.length; idx++){
    if (arr[idx] > max){
      max = arr[idx];
    }
  }
  console.log("Max value is:" + max);
}
