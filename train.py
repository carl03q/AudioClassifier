import argparse
from lib import datasetManager

parser = argparse.ArgumentParser()

# Opciones
parser.add_argument("--val-ratio", help="Validation ratio, only needed on train mode. Default at .3", default='.3')
parser.add_argument("--test-ratio", help="Test ratio, only needed on test mode. Default at .1", default='.1')
parser.add_argument("--source", help="Source path. Default is ./Data/Slices/", default='./Data/Slices/')
parser.add_argument("--dataset", help="Dataset path. Default is ./Data/Dataset/", default='./Data/Dataset/')
parser.add_argument("--nb-per-class", help="Number of images per class. Default is 200", default='200')
parser.add_argument("--img-size", help="Images dimensions. Default 128", default='128')

args = parser.parse_args()

val_ratio = args.val_ratio
test_ratio = args.test_ratio
source_path = args.source
datasetPath = args.dataset
nb_per_class = args.nb_per_class
img_size = args.img_size

print("---- Configuration ----")
print("Validation ratio: {}".format(val_ratio))
print("Test ratio: {}".format(test_ratio))
print("Source images path: {}".format(source_path))
print("Dataset path: {}".format(datasetPath))
print("Number of images per class: {}".format(nb_per_class))
print("Images dimensions: {}".format(nb_per_class))

datasetManager.get_dataset(source_path, datasetPath, nb_per_class, img_size, val_ratio, test_ratio, "train")
