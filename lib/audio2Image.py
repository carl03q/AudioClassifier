import os


def convert_to_spectrogram(input_dir, output_dir):
    if os.path.isdir(input_dir):
        os.makedirs(output_dir, exist_ok=True)

        print("\nCreating spectrograms ...")

        '''
        Alexi's Code
        '''

        print("Spectrogram successfully created ...")
    else:
        print("\n***Spectrogram images not created***")
        print("Dir {} not found.".format(input_dir))
        return False

    return True


def convert_to_slices(input_dir, output_dir):
    if os.path.isdir(input_dir):
        os.makedirs(output_dir, exist_ok=True)

        print("\nChopping spectrograms into slices ...")

        '''
        Beckford's Code
        '''

        print("Slices successfully created ...")
    else:
        print("\n***Slices images not created***")
        print("Dir {} not found.".format(input_dir))
        return False

    return True
