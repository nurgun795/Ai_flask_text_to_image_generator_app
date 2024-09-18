from flask import Flask, request, jsonify, render_template
from openai import OpenAI

client = OpenAI(api_key='API KEY')
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
