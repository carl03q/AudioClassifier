import argparse
from lib import datasetManager

parser = argparse.ArgumentParser()

#Opciones
parser.add_argument("--val-ratio", help="Validation ratio, only needed on train mode. Default at .3", default='.3')
parser.add_argument("--test-ratio", help="Test ratio, only needed on test mode. Default at .1", default='.1')

args = parser.parse_args()

validationRatio = args.val_ratio
testRatio = args.test_ratio

print("---- Configuración ----")
print("Validation ratio: {}".format(validationRatio))
print("Test ratio: {}".format(testRatio))

datasetManager.get_dataset()
