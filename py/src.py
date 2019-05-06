import sys
from py_translator import Translator
from translate import Translator

from PIL import Image
import pytesseract 
import goslate

from flask import Flask
from flask_cors import CORS
from flask import request
import json


app = Flask(__name__)
CORS(app)

@app.route('/uploadimage', methods=['POST'])
def uploadimage():
    uploadedFile = request.files['imageData']

    uploadedFile.save('uploads/'+uploadedFile.filename)

    # Please check here if you get what ypu want then return 

    # im = Image.open(urlpath)

    # text = pytesseract.image_to_string (im , lang='hin')
    # print(text)

    # translator= Translator(from_lang="hin",to_lang="en")
    # translation = translator.translate(text)
    # print (translation)

    # return translation

    response = app.response_class(
        # response=json.dumps(translation),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)