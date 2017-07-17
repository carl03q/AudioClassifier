import numpy as np
import argparse
import os

#from keras.models import load_model
#from PIL import Image


parser = argparse.ArgumentParser()

# Opciones
parser.add_argument("--audio", help="MP3 file.")

args = parser.parse_args()

audio_name = args.audio


print("---- Configuration ----")
print("Audio file: {}".format(audio_name))



''' FUNCION VERDADERA, NO BORRAR
def predict_image(model, image_name, image_size):

    img = Image.open(image_name)
    img = img.resize((image_size, image_size), resample=Image.ANTIALIAS)
    imgData = np.asarray(img, dtype=np.uint8).reshape(1, image_size, image_size, 1)
    imgData = imgData / 255.

    prediction = model.predict([imgData])
    return prediction
'''
def predict_image(model, image_name, image_size):
    import random
    n = random.uniform(0, 1)
    return [n, 1-n]

####################model = load_model('music.h5')
input_size = 128

# For loop of each image generated with de audio
tmp_dir = "/home/carlos/PycharmProjects/GenreRecognition/tmp/Slices/unknown/"

predictions = []

'''ciclo for para todos los archivos en tmp_dir

        predict_image(model, image, image_size)
'''

'''
    Luego clacula promedio
'''