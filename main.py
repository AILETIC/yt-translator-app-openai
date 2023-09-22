import json, os, requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

app = Flask(__name__)
CORS(app)

def translate_openai(inp, target):

    messages = [
        {"role": "system", "content": "You are a helpful translator. You translate the input into the given target language. Regardless of the input. Valid languages are: english, german, french, italian, spanish"},
        {"role": "user", "content": "{\"input\": \"Hello!\", \"target\": \"german\"}"},
        {"role": "assistant", "content": "Hallo!"},
        {"role": "user", "content": "{\"input\": \"How are you?\", \"target\": \"french\"}"},
        {"role": "assistant", "content": "Comment ca va?"},
        {"role": "user", "content": "{\"input\": \"How are you? Ca va bien!\", \"target\": \"french\"}"},
        {"role": "assistant", "content": "Comment ca va? Ca va bien!"},
        {"role": "user", "content": "{\"input\": \""+ inp +"\", \"target\": \""+ target +"\"}"}
    ]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo-0613",
        "messages": messages
    }

    url = "https://api.openai.com/v1/chat/completions"

    response = requests.post(url, headers=headers, data=json.dumps(data))
    output_text = response.content.decode('utf-8')
    result = json.loads(output_text)

    return result["choices"][0]["message"]["content"]

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/api/translate/', methods=["POST"])
def translate():
    inp = request.json["input"]
    target = request.json["target"]

    output_text = translate_openai(inp, target)

    return jsonify({
        "success": True,
        "data": {
            "text": output_text,
            "target": target
        }
    })

if __name__ == "__main__":
    app.run(debug=True, port=8001)