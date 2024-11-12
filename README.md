# SheBuildAI
# Google's Women Techmakers presents She Builds AI

# Testing Instructions
- To test the Gender Equality Chatbot application, follow these steps:

1. Clone the Repository
- First, clone the repository to your local machine using the following command:

bash
- Copy code
- git clone https://github.com/your-username/gender-equality-chatbot.git

# 2. Set Up the Environment
Navigate to the project directory:

bash
Copy code
cd gender-equality-chatbot
Create a virtual environment to isolate the project's dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment:

For Windows:
bash
Copy code
.\venv\Scripts\activate
For macOS/Linux:
bash
Copy code
source venv/bin/activate

# 3. Install Dependencies
Install the required Python dependencies using pip:

bash
Copy code
pip install -r requirements.txt

# 4. Run the Flask Application
Start the Flask development server:

bash
Copy code
python app.py
The application should now be running at http://127.0.0.1:5000/. Open this URL in your browser to interact with the chatbot.

# 5. Testing the Chatbot
- Once the app is running, open the browser and go to the main page (http://127.0.0.1:5000/).
- In the chatbot interface, type your message and click "Send" or press Enter.
- The chatbot will respond based on the predefined responses in the responses dictionary.
- Test various inputs like "Hello", "What is gender equality?", "How can I support gender equality?", and other questions related to gender equality.

# 6. Testing Edge Cases
Test with blank messages (the bot should respond with a default "I'm sorry, I didn't understand that" message).
Test with various phrasings of questions, like "What are gender roles?" vs "Explain gender roles" to see if the bot responds accurately.
Test the chatbot's responsiveness by interacting with the input field and observing the message flow.
