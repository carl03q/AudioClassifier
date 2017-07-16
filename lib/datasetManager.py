import os
import pickle
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

    '''
    if mode == "train":
        train_X = pickle.load(open("{}train_X_{}.p".format(dataset_path, dataset_name), "rb"))
        train_y = pickle.load(open("{}train_y_{}.p".format(dataset_path, dataset_name), "rb"))
        validation_X = pickle.load(open("{}validation_X_{}.p".format(dataset_path, dataset_name), "rb"))
        validation_y = pickle.load(open("{}validation_y_{}.p".format(dataset_path, dataset_name), "rb"))
        print("Dataset loaded!")
        return train_X, train_y, validation_X, validation_y

    elif mode == "test":
        test_X = pickle.load(open("{}test_X_{}.p".format(dataset_path, dataset_name), "rb"))
        test_y = pickle.load(open("{}test_y_{}.p".format(dataset_path, dataset_name), "rb"))
        print("Dataset loaded!")
        return test_X, test_y
    else:
        print("ERROR: {} is no valid mode.".format(mode))
        return
    '''


def create_dataset(input_path, output_path, nb_per_class, slice_size, val_ratio, test_ratio):
    x = []
    y = []

    genres = os.listdir(input_path)
    for i, genre in enumerate(genres):
        genre_dir = input_path + genre +'/'
        files = os.listdir(genre_dir)
        shuffle(files)
        print("--------------------------------------------------------------------")
        for file in files:
            file_dir = genre_dir + file
            print("Processing ", file_dir)
            im = Image.open(file_dir)
            imr = im.resize((int(slice_size), int(slice_size)), resample=Image.ANTIALIAS)
            imgData = np.asarray(imr, dtype=np.uint8).reshape(int(slice_size), int(slice_size), 1)
            imgData = imgData / 255.
            x.append(imgData)

            #Label
            label = [0 for genre in range(len(genres))]
            label[i] = 1
            y.append(label)

    


