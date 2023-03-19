import sys
import os
import numpy as np
import keras 

from flask import Flask, redirect, url_for, request, render_template
from keras.models import load_model
from keras.preprocessing import image

from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


app = Flask(__name__)


model = load_model('models/mymodel.h5')

@app.route('/', methods=['GET'])

def index():
    
    return render_template('index.html')

def model_preprocessing(img_path, model):

    img = image.load_img(img_path, color_mode='rgb', target_size=(128, 128))
    img_array = image.img_to_array(img, data_format='channels_last') 
    img_array = np.expand_dims(img_array, axis=0)
    classes = model.predict(img_array)
    
    return classes





@app.route('/predict', methods=['POST'])

def result():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploaded-image', secure_filename(f.filename))
        f.save(file_path)
        
        classes = model_preprocessing(file_path, model)
        return classifier(classes[0])
     

def classifier(classes):
    if classes[0]>0:
        output="It's a Daisy!"
    elif classes[1]>0:
        output="It's a Dandelion!"
    elif classes[2]>0:
        output="It's a Rose!"
    elif classes[3]>0:
        output="It's a Sunflower!"
    elif classes[4]>0:
        output="It's a Tulip!"
    return output
    
    
if __name__ == '__main__':
    app.run(debug=True)