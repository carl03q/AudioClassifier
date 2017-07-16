import argparse
import os
import pickle

from keras.models import load_model

parser = argparse.ArgumentParser()

# Opciones
parser.add_argument("--dataset", help="Dataset path. Default is ./Data/Dataset/", default='./Data/Dataset/')
parser.add_argument("--postfix", help="Dataset postfix. If not defined take first on dataset dir.", default='')

args = parser.parse_args()

dataset_path = args.dataset
postfix = args.postfix


print("---- Configuration ----")
print("Dataset path: {}".format(dataset_path))

if not postfix:
    files = [filename for filename in os.listdir(dataset_path) if filename.startswith("test_")]
else:
    files = ["test_X_"+postfix, "test_y_"+postfix]

if files:
    test_X = pickle.load(open(files[0], "rb"))
    test_y = pickle.load(open(files[1], "rb"))

    print("Loading weights...")
    model = load_model('music.h5')
    print("Weights loaded!")
    testAccuracy = model.evaluate(test_X, test_y)
    print("Test accuracy: {}".format(testAccuracy[0]))

else:
    print("Dataset not found.")
