module.exports = function Route(app){

//recieves app variable that we passed throught the route on server.js
  app.get("/", function(request, response){
    response.render("index")
  })

  app.post("/result", function(request, response){
    var submitted_info = {
      name: request.body.full_name,
      location: request.body.location,
      language: request.body.language,
      comment: request.body.comments,
    }
    console.log(request.body);
    response.render("results", {user_data: submitted_info});
  })
}
