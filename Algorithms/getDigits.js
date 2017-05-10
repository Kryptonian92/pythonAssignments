//
var string_thing = '12a3'

function getDigits(str){ //define a function
  var new_string ="" //declare a new string variable
  for(var i = 0; i< str.length; i++){ // for loop over elements inteh string
    if(parseInt(str[i]) || parseInt(str[i]) === 0){ // checking for numbers and zeros
      new_string += str[i] // new_string = new string + str[i]
    }
  }
  return Number(new_string)// convert new_string to number and return
}

console.log(getDigits)
