const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/commandDB", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;

db.on("connected", () => {
  console.log("Database Conected");
});

db.on("error", () => {
  console.log("ERROR: While Connecting Database");
});

module.exports = db;
