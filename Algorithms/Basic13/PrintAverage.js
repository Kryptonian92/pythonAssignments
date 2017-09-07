// the following function will analyze an array's values
// and print the average

function printAverage(arr){
  if(arr.length == 0){
    console.log("Error no value");
    return;
  }
  var sum = arr[0];
  for(var i = 1; idx < arr.length; i++){
    sum += arr[idx];
  }
  console.log("Average value is:" + sum/arr.length);
}
