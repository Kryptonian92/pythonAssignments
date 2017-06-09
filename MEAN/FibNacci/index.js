function fib() {
 var p = 0;
 var c = 1;
 // var temp = p;
 function nacci() {
   console.log("Fib:", c);
   console.log("previous:", p)
   var temp = p;
   p = c;
   c = c + temp;
 }
 return nacci
}
var fibCounter = fib();
fibCounter() // should console.log "1"
fibCounter() // should console.log "1"
fibCounter() // should console.log "2"
fibCounter() // should console.log "3"
fibCounter() // should console.log "5"
fibCounter() // should console.log "8"
fibCounter()
fibCounter()
fibCounter()
fibCounter()
