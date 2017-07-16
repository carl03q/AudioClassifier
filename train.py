import argparse
import os


from lib import datasetManager
import modelGenerator
from keras.callbacks import ModelCheckpoint

parser = argparse.ArgumentParser()

# Opciones
parser.add_argument("--val-ratio", help="Validation ratio, only needed on train mode. Default at .3", default='.3')
parser.add_argument("--test-ratio", help="Test ratio, only needed on test mode. Default at .1", default='.1')
parser.add_argument("--source", help="Source path. Default is ./Data/Slices/", default='./Data/Slices/')
parser.add_argument("--dataset", help="Dataset path. Default is ./Data/Dataset/", default='./Data/Dataset/')
parser.add_argument("--nb-per-class", help="Number of images per class. Default is 1000", default='1000')
parser.add_argument("--img-size", help="Images dimensions. Default 128", default='128')
parser.add_argument("--nb-epochs", help="Number of epochs to be executed. Default 20", default='20')
parser.add_argument("--batch-size", help="Size of each epoch, tweak this value if you have memory issues. Default 32", default='32')

args = parser.parse_args()

val_ratio = float(args.val_ratio)
test_ratio = float(args.test_ratio)
source_path = args.source
datasetPath = args.dataset
nb_per_class = int(args.nb_per_class)
img_size = int(args.img_size)
nb_epochs = int(args.nb_epochs)
batch_size = int(args.batch_size)

print("---- Configuration ----")
print("Validation ratio: {}".format(val_ratio))
print("Test ratio: {}".format(test_ratio))
print("Source images path: {}".format(source_path))
print("Dataset path: {}".format(datasetPath))
print("Number of images per class: {}".format(nb_per_class))
print("Images dimensions: {}".format(img_size))
print("\n--- Training setup ---")
print("Number of epochs: {}".format(nb_epochs))
print("Size of batch: {}".format(batch_size))

train_X, train_y, validation_X, validation_y = datasetManager.get_dataset(source_path, datasetPath, nb_per_class, img_size, val_ratio, test_ratio, "train")

classes = os.listdir(source_path)
nb_classes = len(classes)


model = modelGenerator.create_model(int(nb_classes), int(img_size))
model.summary()



# checkpoint
filepath="weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]


print("Training the model...")
model.fit(train_X, train_y,
          epochs=nb_epochs,
          batch_size=batch_size,
          shuffle=True,
          validation_data=(validation_X, validation_y),
          #validation_split=0.33,
          callbacks=callbacks_list)

print("Model trained!")


print("Saving the weights...")
model.save_weights('music.h5')
print("Weights saved!")