from flask import Flask, request, jsonify, render_template
from openai import OpenAI

client = OpenAI(api_key='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')
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables (use dotenv for local development)
from dotenv import load_dotenv
load_dotenv()

# Set the OpenAI API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.json.get('prompt')

    try:
        # Call OpenAI's image generation API
        response = client.images.generate(prompt=prompt,
        n=1,
        size="512x512")

        image_url = response.data[0].url

        return jsonify({'image_url': image_url})

    except Exception as e:
        # Handle errors
        print(f"Error generating image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
