import os
import pickle


def get_dataset(slices_path, dataset_path, nb_per_class, slice_size, val_ratio, test_ratio, mode):

    dataset_name = str(nb_per_class) + str(slice_size)

    if not os.path.isfile(dataset_path + "train_x_" + dataset_name):
        print("Creating dataset ...")
        create_dataset(slices_path, dataset_path, nb_per_class, slice_size, val_ratio, test_ratio)
    else:
        print("Using existing dataset.")

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



def create_dataset(input_path, output_path, nb_per_class, slice_size, val_ratio, test_ratio):
    '''
    Chaly
    input path es para imagenes, outputpath es para donde guardar el dataset

    Debes crear una funcion que utilizando path
    luego lee las imagenes, te puede servir os.listdir

    Eso te mostrará los folder ['jazz', 'dubstep']
    luego puedes concatenar path y lo que sale en el arreglo
    para que te quede algo como ./Data/Slices/jazz y le aplicas lisdir otra vez
    eso te mostrara todos los archivos de imagenes

    la vaina es que al final debes leer todas esas imagenes en un arreglo
    un buen metodo es utilizar un for a ese arreglo y dentro

    Image.open('direccion de la imagen') #Image es parte de libreria PIL

    a Cada imagen debes hacerle un proceso
    1. .resize(slice_size, slice_size, resample=Image.ANTIALIAS)
    2. normalizar -> dividir entre 255 -> img/255.0

    3. onehot encode (etiquetar las imagenes ->
    label = [0 for _ in range(len(cantidad de generos)]
    label[# de genero de la imagen] = 1

    supongamos que tenemos dubstep y jazz, dubstep sería 0 y jazz 1

    label = [0 for _ in range(len(cantidad de generos)]
    esto daría [0,0] xq son 2 generos creara un arreglo de 0 para un rango de 2

    si estas evaluando las imagenes de jazz
    label [1] = 1  ....jazz es el genero segundo , tiene indice 1
    label -> queda como [0,1]

    al final tengas dos arreglos
    uno X para las imagenes
    y uno Y para las etiquetas

    X.append(img)
    y.append(label)

    #casi terminas, ultimo paso
    en machine learning siempre necesitas separar tus datos
    en conjuntos, uno para entrenar, validar y testear

    arriba  yo te doy un ratio  de validacion y uno de test, lo que sobra es para training
    que debes hacer, debes repartir el arreglo X en cada set ejemplo

    #por cierto, necesitas convertir el arreglo a  numpy

    cantidad_validacion = int(len(X) * validationRatio)    si tengo 1000 imagenes * 0.3 = 300
    cantidad_testing =                                     si tengo 1000 imagenes * 0.1 = 100

    cantidad_entrenamiento = len(X) - cantidad_validacion - cantidad_testing      1000-300-100 + 600
    train_X = np.array( X[:cantidad_entrenamiento] )     si tengo 1000 imagenes le digo que agarre las primeras 600 imagenes
    train_y = np.array( y[...])

    train_X.reshape([-1, sliceSize, sliceSize, 1]) //necesario para tensorflow, cambia estructura de la matriz

    y haces lo mismo para validation y testing... pero alla es más complicado que las 600 primeras
    seria algo mas como de la 600 a la 900  validacion

    POR ULTIMO GRABARLOS
    pickle.dump(train_X, open("{}train_X_{}.p".format(datasetPath, datasetName), "wb"))
    pickle.dump(train_y, open("{}train_y_{}.p".format(datasetPath, datasetName), "wb"))
    pickle.dump(validation_X, open("{}validation_X_{}.p".format(datasetPath, datasetName), "wb"))
    pickle.dump(validation_y, open("{}validation_y_{}.p".format(datasetPath, datasetName), "wb"))
    pickle.dump(test_X, open("{}test_X_{}.p".format(datasetPath, datasetName), "wb"))
    pickle.dump(test_y, open("{}test_y_{}.p".format(datasetPath, datasetName), "wb"))
'''
    
       #codigo que trabajara con los directorios
    #path variable en donde se asignara el path de las imaegenes
    genres = os.listdir(input_path)
    
    for genre in genres:
        genre_dir = input_path + genre
    
    print(genre_dir)     
    return (genres)
    
    return path


