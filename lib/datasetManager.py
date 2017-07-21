import os
import pickle

import errno
import numpy as np
from PIL import Image
from random import shuffle


def get_dataset(slices_path, dataset_path, nb_per_class, slice_size, val_ratio, test_ratio, mode):

    dataset_name = str(nb_per_class) + "_" + str(slice_size)

    if not os.path.isfile("{}train_X_{}.p".format(dataset_path, dataset_name)):
        print("Creating dataset ...")
        create_dataset(slices_path, dataset_path, nb_per_class, slice_size, val_ratio, test_ratio)
    else:
        print("Using existing dataset.")

    train_X = pickle.load(open("{}train_X_{}.p".format(dataset_path, dataset_name), "rb"))
    train_y = pickle.load(open("{}train_y_{}.p".format(dataset_path, dataset_name), "rb"))
    validation_X = pickle.load(open("{}validation_X_{}.p".format(dataset_path, dataset_name), "rb"))
    validation_y = pickle.load(open("{}validation_y_{}.p".format(dataset_path, dataset_name), "rb"))
    print("Dataset loaded!")
    return train_X, train_y, validation_X, validation_y


def create_dataset(input_path, output_path, nb_per_class, slice_size, val_ratio, test_ratio):
    data = []

    genres = os.listdir(input_path)

    for i, genre in enumerate(genres):
        genre_dir = input_path + genre +'/'
        files = os.listdir(genre_dir)
        shuffle(files)
        files = files[:nb_per_class]
        print("--------------------------------------------------------------------")
        for file in files:
            file_dir = genre_dir + file
            print("Processing ", file_dir)
            im = Image.open(file_dir)
            imr = im.resize((int(slice_size), int(slice_size)), resample=Image.ANTIALIAS)
            imgData = np.asarray(imr, dtype=np.uint8).reshape(int(slice_size), int(slice_size), 1)
            imgData = imgData / 255.


            #Label
            label = [0 for genre in range(len(genres))]
            label[i] = 1
            data.append((imgData, label))

    shuffle(data)
    x, y = zip(*data)

    # Split data
    validation_nb = int(len(x) * val_ratio)
    test_nb = int(len(x) * test_ratio)
    train_nb = len(x) - (validation_nb + test_nb)


    # Prepare for Tflearn at the same time
    train_X = np.array(x[:train_nb]).reshape([-1, slice_size, slice_size, 1])
    train_y = np.array(y[:train_nb])
    validation_X = np.array(x[train_nb:train_nb + validation_nb]).reshape([-1, slice_size, slice_size, 1])
    validation_y = np.array(y[train_nb:train_nb + validation_nb])
    test_X = np.array(x[-test_nb:]).reshape([-1, slice_size, slice_size, 1])
    test_y = np.array(y[-test_nb:])
    print("Dataset created!")


    # Create path for dataset if not existing
    if not os.path.exists(os.path.dirname(output_path)):
        try:
            os.makedirs(os.path.dirname(output_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    # SaveDataset
    print("Saving dataset... ")
    dataset_name = str(nb_per_class) + "_" + str(slice_size)
    pickle.dump(train_X, open("{}train_X_{}.p".format(output_path, dataset_name), "wb"))
    pickle.dump(train_y, open("{}train_y_{}.p".format(output_path, dataset_name), "wb"))
    pickle.dump(validation_X, open("{}validation_X_{}.p".format(output_path, dataset_name), "wb"))
    pickle.dump(validation_y, open("{}validation_y_{}.p".format(output_path, dataset_name), "wb"))
    pickle.dump(test_X, open("{}test_X_{}.p".format(output_path, dataset_name), "wb"))
    pickle.dump(test_y, open("{}test_y_{}.p".format(output_path, dataset_name), "wb"))
    print("Dataset saved!")

