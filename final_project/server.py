from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench" ,  methods=['GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate', '')
    # Write your code here
    translated_text = translator.english_to_french(english_text)
    return "Translated text to French"

@app.route("/frenchToEnglish" ,  methods=['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate', '')
    translated_text = translator.french_to_english(french_text)
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
