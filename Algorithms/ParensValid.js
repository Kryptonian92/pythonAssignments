function findChar(string){
  var arr = []
  for (var x=0; x<string.length; x++){
    if (string[x] == '(' || string[x] =='[' || string[x] == '{'){
      arr.push(string[x])
    }else{
      if(string[x] == ')'){
        if(arr[arr.length-1] == '('){
          arr.pop()
        }else{
          return false;
        }
      }else if (string[x] == ']'){
        if(arr[arr.length-1]=='['){
          arr.pop()
        }else{
          return false;
        }
      }else if(string[x] == '}'){
        if(arr[arr.lenght-1]=='{'){
          arr.pop()
        }else{
          return false;
        }
      }
      }
      if(arr.length==0){
        return true
      }else{
        return false;
      }
    }
    console.log(findChar("]"))
}
