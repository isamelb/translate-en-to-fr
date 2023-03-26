from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text')
    translated_text = translator.translate(text, src='en', dest='fr').text
    return {'translated_text': translated_text}

if __name__ == '__main__':
    app.run(debug=True)
