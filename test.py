import argparse
import os
import pickle

from keras.models import load_model

parser = argparse.ArgumentParser()

# Opciones
parser.add_argument("--dataset", help="Dataset path. Default is ./Data/Dataset/", default='./Data/Dataset/')
parser.add_argument("--postfix", help="Dataset postfix. Default is '1000_128'.", default='1000_128')

args = parser.parse_args()

dataset_path = args.dataset
postfix = args.postfix


print("---- Configuration ----")
print("Dataset path: {}".format(dataset_path))
print("Postfix: {}".format(postfix))

files = ["{}test_X_{}.p".format(dataset_path, postfix),
         "{}test_y_{}.p".format(dataset_path, postfix)]

if files:
    test_X = pickle.load(open(files[0], "rb"))
    test_y = pickle.load(open(files[1], "rb"))

    print("Loading weights...")
    model = load_model('music.h5')
    print("Weights loaded!")
    testAccuracy = model.evaluate(test_X, test_y)

    print("Test accuracy: %.2f %%" % (testAccuracy[1] * 100))


else:
    print("Dataset not found.")
