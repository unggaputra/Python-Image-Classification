from flask import Flask, render_template, request
import joblib
import numpy as np
import time
from werkzeug.utils import secure_filename
import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img, ImageDataGenerator

app = Flask(__name__, template_folder='app/templates')
app.config['UPLOAD_FOLDER'] = 'uploads'
allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
model = load_model('model/model.h5')  # Ganti dengan path yang sesuai
target_size = (224, 224)  # Sesuaikan dengan ukuran input model
class_labels = ['Rock', 'Paper', 'Scissors']

def preprocess_image(image_path):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            if 'file' in request.files:
                file = request.files['file']
                if file and file.filename != '':
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)

                    # Preprocess gambar
                    preprocessed_img = preprocess_image(file_path)

                    # Lakukan prediksi
                    start_time = time.time()
                    prediction = model.predict(preprocessed_img)[0]
                    end_time = time.time()

                    predicted_label = class_labels[np.argmax(prediction)]
                    accuracy = max(prediction)

                    prediction_time = end_time - start_time

                    return render_template('result.html', predicted_label=predicted_label, accuracy=accuracy, prediction_time=prediction_time, image_path=file_path)
            else:
                return "No file provided."
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)