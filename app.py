from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample response logic for the chatbot
def chatbot_response(message):
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! Welcome to the Healthcare Assistant. How can I assist you today?"
    elif "appointment" in message:
        return "Sure! Please provide the doctor's name, your preferred date, and time for the appointment."
    elif "symptom" in message:
        return "Please describe your symptoms, and I'll provide general guidance."
    elif "emergency" in message:
        return "If this is a medical emergency, please call your local emergency number immediately."
    elif "thank you" in message or "thanks" in message:
        return "You're welcome! Take care and stay healthy."
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase your question?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
