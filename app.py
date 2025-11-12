from flask import Flask, request, jsonify
from bu_chatbot import generate_response, words, classes, model

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    bot_reply = generate_response(user_input, model, words, classes)
    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
