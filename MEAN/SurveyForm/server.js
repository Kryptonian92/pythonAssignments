var express = require("express");
var path = require("path");
//loads express and path module, its already included.
var bodyParser = require("body-parser");

//envokes
var app = express();
app.use(bodyParser.urlencoded());
//used for post information
app.use(express.static(path.join(__dirname, "./static")));
//for static files. Theres no static folder for this file, but will look in static folders in the future
app.set("views", path.join(__dirname, "./views"));
//all the views will be in the views folder
app.set("view engine", "ejs");

var route = require("./routes/index.js")(app)
// passing app on line 7 "var app" to var route
app.listen(3000, function(){
  console.log("listening on port 3000")
  // app is using local host 3000. Importat to let you know that your server is working!
});
