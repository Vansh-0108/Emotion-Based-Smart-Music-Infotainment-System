from keras.models import model_from_json
# from keras_preprocessing.image import load_img
# import numpy as np
from pathlib import Path

############################################################################################
############################################################################################

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
json_file = open(BASE_DIR/"emotiondetector.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights(BASE_DIR/"emotiondetector.h5")

def ef(image):
    # img = load_img(image,grayscale =  True )
    # feature = np.array(img)
    feature = image.reshape(1,48,48,1)
    return feature/255.0

label = ['angry','disgust','fear','happy','neutral','sad','surprise']


def predict_func (image):
    print(BASE_DIR)
    img = ef(image)
    pred = model.predict(img)
    pred_label = label[pred.argmax()]
    print("model prediction is ",pred_label)
    return pred_label
