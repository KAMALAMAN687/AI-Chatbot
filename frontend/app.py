import streamlit as st
import requests

# Frontend using Streamlit
st.title("E-commerce Chatbot")

st.write("Ask me anything related to your orders, products, or payments!")

# Input field for user message
user_input = st.text_input("You:", "")

# Add a button to send the query
if st.button("Send"):
    if user_input:
        try:
            # Make a POST request to the backend
            response = requests.post("http://localhost:3000/query", json={"message": user_input})
            # Display the bot's response
            st.write("Bot:", response.json().get("fulfillmentText"))
        except requests.exceptions.RequestException as e:
            st.error(f"Error: Could not connect to backend. {e}")
    else:
        st.warning("Please enter a message before sending.")
