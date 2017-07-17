import numpy as np
import argparse
import os
import shutil

# from keras.models import load_model
# from PIL import Image
from lib import audio2Image


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


# Call model
# model = load_model('music.h5')
input_size = 128


tmp_dir = "./tmp/"
#if os.path.isdir(tmp_dir):
#   shutil.rmtree(tmp_dir)

os.makedirs(tmp_dir, exist_ok=True)
raw_dir = tmp_dir+'Raw/'
spec_dir = tmp_dir+'Spectrograms/'
img_dir = tmp_dir+'Slices/'

os.makedirs(raw_dir, exist_ok=True)
os.makedirs(spec_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

shutil.copy2(audio_name, raw_dir)

# Convert audio to spectrogram
audio2Image.convert_to_spectrogram(raw_dir, spec_dir)
audio2Image.convert_to_slices(spec_dir, img_dir)



predictions = []

'''ciclo for para todos los archivos en tmp_dir

        predict_image(model, img_dir, image_size)
'''

'''
    Luego clacula promedio
'''

#shutil.rmtree(tmp_dir)