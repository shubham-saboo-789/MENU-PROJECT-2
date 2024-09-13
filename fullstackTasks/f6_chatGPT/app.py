from flask import Flask, render_template, request, jsonify

import google.generativeai as genai
from PIL import Image


app = Flask(__name__)


# Route for rendering the index page
@app.route('/')
def index():
    return render_template('index.html')


def generate_text(prompt):
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"




# API endpoint that returns a response based on the input
@app.route('/api/response', methods=['GET'])
def get_response():
    user_input = request.args.get('user_input', '')
    # Simple logic for reply, you can add more complex processing here
    reply = generate_text(user_input)
    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run(debug=True)
