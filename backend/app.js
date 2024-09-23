const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const { classifyIntent } = require("./intentClassifier");
const fs = require("fs");
const path = require("path");

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(cors());

app.post("/query", async (req, res) => {
  try {
    const userMessage = req.body.message;

    // Classify the intent and extract entities
    const intentResponse = await classifyIntent(userMessage);
    console.log("Intent Response:", intentResponse); // Log the raw response

    let parsedResponse;
    try {
      parsedResponse = JSON.parse(intentResponse);
      console.log("Parsed Response:", parsedResponse);
    } catch (error) {
      console.error("JSON Parse Error:", error);
      return res.status(500).send("Error parsing intent response");
    }

    if (parsedResponse.intent === "Check Order Status") {
      const orderDetails = await getOrderDetails(
        parsedResponse.entities.order_number
      );
      if (orderDetails) {
        const { order_number, status, product, delivery_date } = orderDetails;
        res.json({
          fulfillmentText: `Order ${order_number} for ${product} is currently ${status} and is expected to be delivered on ${delivery_date}.`,
        });
      } else {
        res.json({
          fulfillmentText: `Order ${parsedResponse.entities.order_number} not found.`,
        });
      }
    } else {
      res.json({ fulfillmentText: `Intent: ${parsedResponse.intent}` });
    }
  } catch (err) {
    console.error("Error:", err);
    res.status(500).send("Error processing request");
  }
});

// Function to retrieve order details from orders.json
async function getOrderDetails(orderNumber) {
  try {
    const data = fs.readFileSync(path.join(__dirname, "orders.json"));
    const orders = JSON.parse(data).orders;
    return orders.find((order) => order.order_number === orderNumber) || null;
  } catch (error) {
    console.error("Error reading orders file:", error);
    return null;
  }
}

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
