module.exports = function Route(app, server){
  //this gets the socket.io module
  var io = require("socket.io").listen(server)
//recieves app variable that we passed throught the route on server.js
  app.get("/", function(request, response){
    response.render("index");
  })

  io.sockets.on("connection", function(socket){
    socket.on("posting_form", function(data){
      console.log("This is console Data:", data);
      var random_number = Math.floor((Math.random() * 1000) + 1);
      socket.emit("updated_message", {response: data});
      socket.emit("random_number", {response: random_number});
      console.log(data);
    })
  })

}
