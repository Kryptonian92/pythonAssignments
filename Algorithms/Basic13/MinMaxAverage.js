// The following will find and print the max, min and average values

function maxMinAverage(arr){
  if(arr.length == 0){
    console.log("Error. No min, max or average");
    return;
  }
  var min = arr[0];
  var max = arr[0];
  var sum = arr[0];
  for(var i = 1; i<arr.length; i++){
    if (arr[i] < min) {min = arr[i];}
    if (arr[i] > max) {max = arr[i];}
    sum += arr[i];
  }
  console.log("Max:" + max + "Min:" + min);
  console.log("Average:" + sum/arr.length);
}
