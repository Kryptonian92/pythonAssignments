function Flatten(arr){
  var newArr = [];
  arr = [1,2,3]
  for(var i=0; i<arr.length; i++){
    if(Array.isArray(arr[i])){
      for(var j=0; i<arr[i].length; j++){
        newArr[newArr.length] = arr[i][j];
      }
    }
    else newArr[newArr.length]=arr[i]
  }
  return arr
}
