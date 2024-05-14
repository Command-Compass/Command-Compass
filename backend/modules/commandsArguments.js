const mongoose = require("mongoose");

const CommandArgumentSchema = new mongoose.Schema({
  command_id: { type: mongoose.Schema.Types.ObjectId, ref: "Command" },
  argument: String,
  description: String,
  examples: [{ input: String, output: String }],
});

const CommandArgument = mongoose.model(
  "CommandArgument",
  CommandArgumentSchema
);

module.exports = { CommandArgument };
