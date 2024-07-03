# app.py

from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Assuming the JSON input has a 'message' key
    message = data.get('message', '')

    # Perform some processing (e.g., prediction)
    # Here, we simply echo back the input message
    response = {
        'input_message': message,
        'output_message': f'Hello, {message}!'
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
