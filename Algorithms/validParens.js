function validParens(str){
    var countOpen = 0;
    for (var i = 0; i < str.length; i++){
        if (str[i]) == "("){
        countOpen++;
        }
        if (str[i] == ")"){
            countOpen --;
            if (countOpen < 0) return false
        }
    }
    return countOpen == 0
}
validParens("((())")

// # ternary operator
// # condition ? true : false
// #     if (countOpen ==0) return true
// #     else return false
// #
// #     equals
// #
// #     count Open == 0? return true : return false
