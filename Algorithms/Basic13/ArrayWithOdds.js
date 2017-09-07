// The following function will create an array with odd integers from 1-255

function oddArray1to255(){
  var oddArray = [];
  for (var num = 1; num <= 255; num += 2){
    oddArray.push(num);
  }
  console.log(oddArray);
}
return oddArray1to255();
