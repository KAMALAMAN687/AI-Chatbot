E-commerce Chatbot
This project is a chatbot designed for an e-commerce platform. The chatbot handles common customer queries such as checking order status, asking about products, managing returns and refunds, payment issues, and personalized product recommendations. The system uses a Python-based Natural Language Processing (NLP) engine with a simple frontend built using Streamlit and a backend using Node.js and Express.

Features
Order Status Tracking: Users can check the status of their orders.
Product Inquiries: Users can ask questions about products.
Returns and Refunds: Handles customer inquiries related to returning items or requesting refunds.
Payment Issues: Addresses issues related to payment.
Personalized Recommendations: Provides product suggestions to users.
User Interface: Built using Streamlit for a simple and interactive frontend.
Backend Server: Node.js server that integrates with the Python NLP engine for intent classification.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/ecommerce-chatbot.git
Install Node.js dependencies:

bash
Copy code
cd backend
npm install
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Install the spacy model:

bash
Copy code
python -m spacy download en_core_web_sm
Usage
Run the backend server:

bash
Copy code
node app.js
Run the Streamlit frontend:

bash
Copy code
streamlit run app.py
Open the Streamlit app in your browser:

arduino
Copy code
http://localhost:8501
Enter queries such as:

"What is the status of my order?"
"Can I return my product?"
"Suggest me a product."
"I have a payment issue."
Files Overview

1. intentClassifier.py (Python)
   This file contains logic for classifying intents and extracting entities using the spaCy NLP library.

classify_intent(text): Identifies the intent of the user's query (e.g., "Check Order Status", "Product Inquiry").
extract_entities(text): Extracts entities such as product names, order numbers, and user IDs. 2. app.js (Node.js Backend)
This is the main backend server, built using Express.js.

Handles HTTP POST requests to /query where it:
Calls the classifyIntent function to determine the intent of the user's message.
Returns appropriate responses based on the identified intent (e.g., checking order status).
Reads from orders.json to retrieve order details for status queries. 3. intentClassifier.js (Node.js to Python Integration)
This file contains the classifyIntent function that spawns a child process to run the Python intentClassifier.py script and return its output.

Uses child_process to execute Python scripts and handle the output from the NLP model. 4. app.py (Streamlit Frontend)
The user interface is built with Streamlit and serves as the chatbot interface.

It accepts user input and sends the input to the backend via an HTTP POST request.
Displays the chatbot's response on the frontend. 5. orders.json (Data File)
This JSON file contains mock data for orders. It is used to simulate fetching order details such as order number, product name, order status, and delivery date.

Example structure:
json
Copy code
{
"orders": [
{
"order_number": "12345",
"product": "Laptop",
"status": "shipped",
"delivery_date": "2024-09-30"
}
]
}
How It Works
User Query: The user enters a message in the Streamlit interface (e.g., "What is the status of my order?").
Intent Classification: The backend sends the message to the intentClassifier.py Python script to classify the intent and extract entities like order number or product.
Order Status: If the intent is "Check Order Status", the backend fetches order details from orders.json and sends a structured response.
Response: The chatbot responds in the Streamlit app with relevant information (e.g., "Your order is shipped and will be delivered by 2024-09-30.").
Dependencies
Backend:

Node.js
Express.js
body-parser
cors
child_process (for running Python scripts)
Frontend:

Streamlit
requests (for HTTP calls to the backend)
NLP Engine:

Python 3.x
spaCy (with the en_core_web_sm model)
Future Improvements
Expand the range of intents (e.g., "Cancel Order").
Improve entity extraction by customizing spaCy's Named Entity Recognition (NER) model.
Enhance the frontend UI with more conversational capabilities.
Feel free to customize this README.md and the project structure to match your specific needs!

I prefer this response
