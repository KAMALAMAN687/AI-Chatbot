import streamlit as st
import requests
import time
# Frontend using Streamlit
st.title("E-commerce Chatbot")

st.write("Ask me anything related to your orders, products, or payments! Try searching (e.g. :  I want track order (orderno.) available order numbers write now 1234 ,54321)")

# Input field for user message
user_input = st.text_input("You:", "")

def get_bot_response():
            time.sleep(3)  # Simulate a delay in fetching the bot response
            response = requests.post("http://localhost:3000/query", json={"message": user_input})
            # Display the bot's response
            bot_response = response.json().get("fulfillmentText")
            return bot_response

# Add a button to send the query
if st.button("Send"):
    if user_input:
        try:
            # Make a POST request to the backend
            

# Create a loading spinner while waiting for the bot's response
            with st.spinner("Bot is processing your request..."):
             bot_response = get_bot_response()
            
            
           

# Displaying the bot's response in a styled way using Markdown
            st.markdown(f"""
                <div style="background-color: #f9f9f9; padding: 10px; border-radius: 8px; border: 1px solid #ddd;">
                <p style="font-size: 18px; color: #333;"><strong>Bot:</strong> {bot_response}</p>
                </div>
            """, unsafe_allow_html=True)
            
            
            #st.write("Bot:", response.json().get("fulfillmentText"))
        except requests.exceptions.RequestException as e:
            st.error(f"Error: Could not connect to backend. {e}")
    else:
        st.warning("Please enter a message before sending.")
