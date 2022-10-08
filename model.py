import numpy as np
#import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
#from keras.preprocessing import *
import os


def modelLoad():
    return keras.models.load_model('model_92.h5')


def modelPrediction(name):
    model = modelLoad()
    test_image = image.load_img(name, target_size=(384,384))
    imagee = test_image
    isim = os.path.split(name)[1]
        # Predict artist
    test_image = image.img_to_array(test_image)
    test_image /= 255.
    test_image = np.expand_dims(test_image, axis=0)
    
    prediction = model.predict(test_image)
    
    
    prediction_probability = np.amax(prediction)
    prediction_idx = np.argmax(prediction)

    
    labels = {0: 'Vincent_van_Gogh',
              1: 'Edgar_Degas',
              2: 'Pablo_Picasso',
              3: 'Pierre-Auguste_Renoir',
              4: 'Albrecht_Dürer',
              5: 'Paul_Gauguin',
              6: 'Francisco_Goya',
              7: 'Rembrandt',
              8: 'Alfred_Sisley',
              9: 'Titian',
              10: 'Marc_Chagall'}
    
    pre_artist = labels[prediction_idx].replace('_', ' ')
    pre_probability = prediction_probability*100


    name = ""
    for i in isim:
        if i ==".":
            break
        else:
            name += i
    
    return (name.replace('_', ' '), pre_artist, pre_probability)
#(384, 384)