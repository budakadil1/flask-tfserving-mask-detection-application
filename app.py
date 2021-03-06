from werkzeug.wrappers import Request, Response
from flask import render_template
from flask import Flask, request
from prediction_handler import make_prediction
import numpy as np
import io
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = './upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # try for images
        if 'file1' not in request.files:
            return 'there is no image in form!'
        file1 = request.files['file1']
        img = Image.open(io.BytesIO(file1.read())).resize((64,64))
        # convert img (if not RGB, RGBA as example) to RGB as model expects 3 channels, not 4.
        if img.mode != 'RGB':
            img = img.convert('RGB')
        test_image = np.asarray(img)
        test_image = np.expand_dims(test_image, axis=0)
        results = make_prediction(test_image)

        return render_template('field.html', result=results)

    return render_template('field.html')

if __name__ == "__main__":
    app.run()
