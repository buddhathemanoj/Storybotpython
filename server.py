# from flask import Flask, request, jsonify
# from flask_cors import CORS  # Import the CORS extension
# import openai
# import os
# from dotenv import load_dotenv

# app = Flask(__name__)
# CORS(app) 
# # Load environment variables from .env file
# load_dotenv()

# # Set your OpenAI API key here
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# if not OPENAI_API_KEY:
#     raise ValueError("OpenAI API key not found. Make sure to set the OPENAI_API_KEY environment variable.")

# openai.api_key = OPENAI_API_KEY


# @app.route('/generate_story', methods=['POST'])
# def generate_story():
#     try:
#         data = request.get_json()
#         genre = data['genre']
#         character_name = data['character_name']

#         # Generate the prompt for the story
#         prompt = f"Write a {genre} story with {character_name}."
#         print(f"Incoming prompt: {prompt}")  # Print the incoming prompt

#         # Make a call to the OpenAI API to generate the story
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=prompt,
#             max_tokens=150  # You can adjust the number of tokens as per your requirement
#         )

#         story = response['choices'][0]['text']
#         print(f"OpenAI API Response: {response}")  # Print the OpenAI API response

#         return jsonify({'story': story})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)
# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Make sure to set the OPENAI_API_KEY environment variable.")

openai.api_key = OPENAI_API_KEY


@app.route('/generate_story', methods=['POST'])
def generate_story():
    try:
        data = request.get_json()
        genre = data['genre']
        character_name = data['character_name']

        # Generate the prompt for the story
        prompt = f"Write a {genre} story with {character_name}."
        print(f"Incoming prompt: {prompt}")  # Print the incoming prompt

        # A list to store the generated rough drafts
        rough_drafts = []

        # Define different temperature values to get varied responses
        temperatures = [0.5, 0.7, 1.0]

        for temperature in temperatures:
            # Make a call to the OpenAI API to generate the story with the specified temperature
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=20,  # You can adjust the number of tokens as per your requirement
                temperature=temperature
            )

            rough_draft = response['choices'][0]['text']
            rough_drafts.append({'temperature': temperature, 'story': rough_draft})

        print(f"OpenAI API Responses: {rough_drafts}")  # Print the OpenAI API responses

        return jsonify({'rough_drafts': rough_drafts})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
