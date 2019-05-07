import sys
import os
from py_translator import Translator
from translate import Translator

from PIL import Image
import pytesseract 
import goslate

from flask import Flask
from flask_cors import CORS
from flask import request
# from flask import Response
import json
import base64
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io

app = Flask(__name__)
CORS(app)

@app.route('/uploadimage', methods=['POST'])
def uploadimage():

    fileData = request.form['file']

    i = base64.b64decode(fileData)
    i = io.BytesIO(i)
    imageFile = mpimg.imread(i, format='PNG')

    imgpng = Image.fromarray(np.uint8(imageFile))
    imgpng.save('img.png', 'PNG')

    # Please check here if you get what ypu want then return 

    im = imgpng
    text = pytesseract.image_to_string (im , lang='hin')
    print(text)

    translator= Translator(from_lang="hin",to_lang="en")
    translation = translator.translate(text)
    print (translation)


    response = app.response_class(
        # response=json.dumps(translation),
        response=json.dumps('one (1) two (2) china (3) four (4) five (5)'),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)