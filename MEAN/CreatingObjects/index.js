// Create a constructor. Create a VehicleConstcutor that takes in the name,
// number of wheels, and the number of passengers.
//
// Each vehicle should have a makeNoise Method
// Using the constructor, create a bike
// redefine the bikes makeNoise method to print "ring ring!"
// create sedan
// redifine the sedans makeNoise method to pring "Honk Honk!"
// Using the constructor, create a bus
// Add a method to Buss that takes in the number of passengers to pick up and adds them to the passenger count.


function VehicleConstcutor(name, wheels, passengers){
  var vehicle = {}
  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.passengers = passengers;
  vehicle.makeNoise = function(){
    console.log("Vroom");

    return vehicle;
  }
  return vehicle;
}
var bike = VehicleConstcutor("bike", 2, 1);
// console.log(bike);
bike.makeNoise();
//
bike.makeNoise = function(){
  // console.log("ring ring")
}
bike.makeNoise();

var sedan = VehicleConstcutor("Sedan", 4, 3);
bike.makeNoise = function(){
  // console.log("Honk Honk!")
}
bike.makeNoise();

var Bus = VehicleConstcutor("Bus", 6, 20);
Bus.pickUpPassengers = function(passengers){
  Bus.pasengers += passengers;
}
console.log(Bus.passengers);
Bus.pickUpPassengers(14);
console.log(Bus.passengers)
