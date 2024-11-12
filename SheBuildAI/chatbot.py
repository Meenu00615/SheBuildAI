from flask import Flask, render_template, request, jsonify  # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests if needed

responses = {
    "Hi": "Hello! How can I assist you today?",
    "Hello": "Hi there! How can I help you?",
    "What's your name?": "I am a chatbot created to help you with various topics.",
    "What is your name?": "I'm your virtual assistant, here to help!",
    "How are you?": "I'm doing great, thank you for asking! How about you?",
    "Good morning": "Good morning! How can I assist you today?",
    "Good evening": "Good evening! How can I help you?",
    "What is gender equality?": "Gender equality means that people of all genders have equal rights, responsibilities, and opportunities.",
    "Why is gender equality important?": "Gender equality promotes fairness and inclusivity, improves economic growth, reduces poverty, and leads to happier societies.",
    "How can I support gender equality?": "You can support gender equality by promoting fairness, respect, and inclusivity in your daily actions and advocating for equal opportunities.",
    "What are the challenges to gender equality?": "Challenges include gender-based violence, wage gaps, lack of representation in leadership roles, and traditional gender norms.",
    "What is gender bias?": "Gender bias refers to the preferential treatment or discrimination against individuals based on their gender, which can result in unequal opportunities or outcomes.",
    "How can we eliminate gender bias?": "Eliminating gender bias requires challenging stereotypes, promoting equality in all spheres of life, and encouraging inclusivity in both personal and professional environments.",
    "What is the gender pay gap?": "The gender pay gap is the difference in earnings between men and women, often resulting from factors like unequal opportunities, discrimination, and societal expectations.",
    "What is the glass ceiling?": "The glass ceiling is an invisible barrier that prevents women from reaching top leadership roles or achieving equal career advancement compared to men.",
    "What are gender roles?": "Gender roles are societal expectations about how individuals should behave, dress, and interact based on their assigned gender, which often limits personal freedoms and equality.",
    "What is gender equality in the workplace?": "Gender equality in the workplace means ensuring that all employees, regardless of gender, have equal opportunities for career advancement, fair pay, and respectful treatment.",
    "How can men support gender equality?": "Men can support gender equality by advocating for equal rights, sharing domestic responsibilities, challenging gender stereotypes, and supporting women in leadership roles.",
    "What is feminism?": "Feminism is the belief in and advocacy for the social, political, and economic equality of the sexes, aiming to address gender-based inequalities and discrimination.",
    "What is the importance of female representation in leadership?": "Female representation in leadership is essential for ensuring diverse perspectives, promoting equal opportunities, and inspiring future generations of women to break barriers.",
    "How does gender inequality affect society?": "Gender inequality can lead to social, economic, and cultural disadvantages for marginalized genders, hindering progress and creating division in society.",
    "What is intersectionality in gender equality?": "Intersectionality refers to how various aspects of a person's identity (such as race, gender, class, etc.) intersect and contribute to unique experiences of discrimination or privilege.",
    "What are some global efforts to promote gender equality?": "Global efforts include the United Nations' Sustainable Development Goal 5, international campaigns like HeForShe, and initiatives focused on closing the gender gap in education, employment, and politics.",
    "How can education contribute to gender equality?": "Education plays a vital role in promoting gender equality by challenging stereotypes, empowering individuals with knowledge, and providing equal opportunities for all students."
}

def get_response(user_input: str) -> str:
    return responses.get(user_input, "I'm sorry, I didn't understand that. Can you ask something else?")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
