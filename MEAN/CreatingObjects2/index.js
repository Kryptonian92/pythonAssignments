//VehicleConstcutor for all of the following vehicles
function VehicleConstructor(name, wheels, passengerNumber,speed){
  if (!(this instanceof VehicleConstructor)){
    return new VehicleConstructor(name,wheels,passengerNumber, speed);
  }
  // Public Variable..Can be used throughout the function
  var distanceTraveled = 0;
  var self = this;
  function updateDistanceTraveled(){
    distanceTraveled += self.speed;
    console.log(distanceTraveled);
  }
  //Public Variable..can only be used within the function
  this.speed = speed;
  this.name = name || "unicycle";
  this.wheels = wheels || 1;
  this.passengerNumber = passengerNumber || 0;

  this.makeNoise = function(noise){
    var noise = noise || "Honk Honk";
    console.log(noise)
  };
  this.move = function(){
    this.makeNoise();
    updateDistanceTraveled();
  };
  this.checkMiles = function(){
    console.log(distanceTraveled);
  };
}

var car = new VehicleConstructor('car', 4, 2, 40);
car.move();
car.checkMiles();
console.log(car.speed);
