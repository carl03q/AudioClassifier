import os
from subprocess import Popen, PIPE, STDOUT
from PIL import Image


currentPath = os.path.dirname(os.path.realpath(__file__))[:-3]


def convert_to_spectrogram(input_dir, output_dir):
    if os.path.isdir(input_dir):
        os.makedirs(output_dir, exist_ok=True)

        print("\nCreating spectrograms ...")

        genres = os.listdir(input_dir)
        for genre in genres:
            genre_dir = input_dir + genre + '/'
            spec_dir = output_dir + genre + '/'

            os.makedirs(os.path.dirname(spec_dir), exist_ok=True)
            print("Converting " + genre_dir + '...')
            pixels_per_second = "50"
            command = "a=0;" \
                      "for file in "+genre_dir+"*.mp3; do " \
                        "a=$((a+1));" \
                        "out_name="+spec_dir+"$a.png;" \
                        'sox "$file" -n spectrogram -Y 130 -X '+pixels_per_second+' -l -r -m -o $out_name;'\
                        "echo $file; echo $out_name;"\
                      "done"
            p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True, cwd=currentPath)
            output, errors = p.communicate()
            if errors:
                print(errors)

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

        genres = os.listdir(input_dir)
        for genre in genres:
            genre_dir = input_dir + genre + '/'
            slice_dir = output_dir + genre + '/'
            files = os.listdir(genre_dir)

            os.makedirs(os.path.dirname(slice_dir), exist_ok=True)

            for idx_song, file in enumerate(files):
                dirImage = genre_dir + file


                with Image.open(dirImage) as img:
                    print(dirImage)
                    minWidth =0
                    maxWidth =128
                    n = int (img.size[0]/128)
                    height = img.size[1]
                    for idx_spec in range(n):
                        newImg = img.crop((minWidth,0,maxWidth,height))
                        savestring = slice_dir+"/"+str(idx_song)+"_"+str(idx_spec)+".png"
                        newImg.save(savestring)
                        minWidth+=128
                        maxWidth+=128

        print("Slices successfully created ...")

    else:
        print("\n***Slices images not created***")
        print("Dir {} not found.".format(input_dir))
        return False

    return True
