
from flask import Flask, render_template, request, jsonify
import openai  # You might need to install the openai package

app = Flask(__name__)

# Load your OpenAI GPT API key here (you should keep this secure and not expose it in the code)
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json['query']
    
    # Get response from GPT model (you might want to customize this part based on your needs)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You might want to choose a different engine
        messages=[
            {"role": "system", "content": "You are a helpful tax auditor from Deloitte specializing in US Tax Laws."},
            {"role": "user", "content": user_query}
        ],
        max_tokens=200, temperature=0.2
    )
    
    bot_response = response['choices'][0]['message']['content']
    
    # Save the conversation to a local file (customize this part if you want a different storage solution)
    with open('responses.txt', 'a') as file:
        file.write(f"User: {user_query}\nBot: {bot_response}\n")
        
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
