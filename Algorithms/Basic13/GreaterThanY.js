// The following algorithm will count and print the
//number of array values less than a given "Y"

function greaterThan(arr, Y){
  var num = 0;
  for(var i=0; i<arr.length; i++){
    if (arr[i]>y) {num++;}
  }
  console.log("%d values are greater than %d", num, y);
}
