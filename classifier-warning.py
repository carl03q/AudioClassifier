
import numpy as np
import argparse
import os
import shutil

from keras.models import load_model
from PIL import Image
from lib import audio2Image


parser = argparse.ArgumentParser()

# Opciones
parser.add_argument("--audio", help="MP3 file.")

args = parser.parse_args()

audio_name = args.audio


print("---- Configuration ----")
print("Audio file: {}".format(audio_name))


def predict_image(model, image_name, image_size):

    img = Image.open(image_name)
    img = img.resize((image_size, image_size), resample=Image.ANTIALIAS)
    imgData = np.asarray(img, dtype=np.uint8).reshape(1, image_size, image_size, 1)
    imgData = imgData / 255.

    prediction = model.predict([imgData])
    return prediction

# Call model
model = load_model('music.h5')
input_size = 128

# Create temporal dirs
tmp_dir = "./tmp/"
if os.path.isdir(tmp_dir):
   shutil.rmtree(tmp_dir)

os.makedirs(tmp_dir, exist_ok=True)
raw_dir = tmp_dir+'Raw/'
spec_dir = tmp_dir+'Spectrograms/'
img_dir = tmp_dir+'Slices/'

os.makedirs(raw_dir, exist_ok=True)
os.makedirs(spec_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)
os.makedirs(raw_dir+'unknown/', exist_ok=True)
# Copy song to temporal dir
shutil.copy2(audio_name, raw_dir+'unknown/')

# Convert audio to spectrogram
audio2Image.convert_to_spectrogram(raw_dir, spec_dir)
audio2Image.convert_to_slices(spec_dir, img_dir)



files = os.listdir(img_dir+'unknown/')

# Make predictions on each image on slice directory
predictions = []
for file in files:
    image_name = img_dir+'unknown/' + file
    prediction = predict_image(model, image_name, input_size)
    predictions.append(prediction)

predictions = np.array(predictions)


source_path = "./_Data/Slices/"
classes = os.listdir(source_path)
nb_classes = len(classes)

confidence_values = []
print("Confidence Values: ")
for i in range(nb_classes):
    confidence_values.append(np.asarray(predictions[:, 0, i]))
    print(confidence_values[i])

for i in range(nb_classes):
    print("{}: {}".format(classes[i], confidence_values[i].mean()))



