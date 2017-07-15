import os


def get_dataset(dataset_path, nb_per_class, slice_size, val_ratio):

    dataset_name = str(nb_per_class) + str(slice_size) + str(val_ratio)

    if os.path.isfile(dataset_path + "train_x_" + dataset_name):
        return


'''

'''

create_dataset
