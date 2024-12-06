from flask import Flask, request, jsonify
from model.model import chatbot_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """
    API endpoint for the chatbot.
    Expects a JSON payload with a 'user_input' field.

    Returns:
        JSON: The chatbot's response or an error message.
    """
    data = request.json
    if 'user_input' not in data:
        return jsonify({"error": "Missing 'user_input' field"}), 400

    user_input = data['user_input']
    if not user_input.strip():
        return jsonify({"error": "Input cannot be empty"}), 400

    try:
        response , input_token , prompt_token = chatbot_response(user_input)
        return jsonify({"response": response, "input_token":input_token, "prompt_token":prompt_token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0", port=8000)
