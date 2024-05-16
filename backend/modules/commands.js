const mongoose = require("mongoose");

const CommandSchema = new mongoose.Schema({
  platform: String,
  command_name: String,
  code: String,
});

const Command = mongoose.model("Command", CommandSchema);

module.exports = { Command };
