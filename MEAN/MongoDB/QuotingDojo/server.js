var express = require('express'),
    bodyParser = require('body-parser'),
    mongoose = require('mongoose'),
    path = require('path'),
    port = 8000,
    app = express();

// Set up body-parser to parse form data
app.use(bodyParser.urlencoded({extended: false}));

// Set up database connection, Schema, model
mongoose.connect('mongodb://localhost/quoting_dojo');

var QuoteSchema = new mongoose.Schema({
  name: String,
  quote: String
});

var Quote = mongoose.model('quotes', QuoteSchema);

// Point server to views
app.set('views', path.join(__dirname, './views'));
// We're using ejs as our view engine
app.set('view engine', 'ejs');

// Here are our routes!
app.get('/', function(req, res){
  res.render('welcome');
});

app.get('/quotes', function(req, res){
  // Logic to grab all quotes and pass into the rendered view
  Quote.find({}, function(err, results){
    if(err) { console.log(err); }
    res.render('quotes', { quotes: results });
  });
});

app.post('/quotes', function(req, res){
  Quote.create(req.body, function(err){
    if(err) { console.log(err); }
    res.redirect('/quotes');
  });
});
// END OF ROUTING...
app.listen(port, function() {
    console.log("listening on port 8000");
})
// app.listen(port);




// // Require the Express Module
// var express = require('express');
// // Create an Express App
// var app = express();
// // Require body-parser (to receive post data from clients)
// var mongoose = require('mongoose');
// var bodyParser = require('body-parser');
// // Integrate body-parser with our App
// mongoose.connect('mongodb://localhost/basic_mongoose');
// var UserSchema = new mongoose.Schema({
//  name: String,
//  age: Number
// })
// mongoose.model('User', UserSchema); // We are setting this Schema in our Models as 'User'
// var User = mongoose.model('User') // We are retrieving this Schema from our Models, named 'User'
//
// app.use(bodyParser.urlencoded({ extended: true }));
// // Require path
// var path = require('path');
// // Setting our Static Folder Directory
// app.use(express.static(path.join(__dirname, './static')));
// // Setting our Views Folder Directory
// app.set('views', path.join(__dirname, './views'));
// // Setting our View Engine set to EJS
// app.set('view engine', 'ejs');
// // Routes
// // Root Request
// app.get('/', function(req, res) {
//     // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
//     res.render('index');
// })
// // Add User Request
// app.post('/users', function(req, res) {
//     console.log("POST DATA", req.body);
//     // This is where we would add the user from req.body to the database.
//     res.redirect('/');
// })
// // Setting our Server to Listen on Port: 8000
// app.listen(8000, function() {
//     console.log("listening on port 8000");
// })
