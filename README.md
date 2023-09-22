# Flask Translation App

This is a Flask app that utilizes the OpenAI API for translation purposes. It translates the input text into the target language using the GPT-3.5-turbo-0613 model.

## Prerequisites
- Python
- Flask
- dotenv
- requests
- flask_cors

## Installation
1. Clone the repository.
2. Install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your OpenAI API key as `OPEN_AI_KEY`.

## Usage
1. Start the Flask server by running the following command:
   ```
   python app.py
   ```
2. Navigate to `http://localhost:8001` in your web browser.
3. You will see the translation app interface.
4. Enter your input text and select the target language.
5. Click the "Translate" button.
6. The translated text will be displayed on the page.

## API Endpoint

### Endpoint
```
/api/translate/
```

### Method
```
POST
```

### Request Body
```json
{
  "input": "Hello!",
  "target": "german"
}
```

### Response
```json
{
  "success": true,
  "data": {
    "text": "Hallo!",
    "target": "german"
  }
}
```

## Example Usage

```python
import requests

url = "http://localhost:8001/api/translate/"

payload = {
    "input": "Hello!",
    "target": "german"
}

response = requests.post(url, json=payload)
data = response.json()

print(data["data"]["text"])
```

## License
This project is licensed under the [MIT License](LICENSE).
