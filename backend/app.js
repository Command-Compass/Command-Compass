const express = require("express");
const bodyParser = require("body-parser");

const app = express();

const db = require("./database");

app.use(bodyParser.json());

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
