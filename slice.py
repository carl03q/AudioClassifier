import argparse
from lib import audio2Image

parser = argparse.ArgumentParser()

# Options
parser.add_argument("--slice-dim", help="Slice size. Default at 128", default='128')
parser.add_argument("--raw-dir", help="Raw mp3's files directory. Default ./Data/Raw/", default='./Data/Raw/')
parser.add_argument("--spec-dir", help="Spectrogram's files directory. Default ./Data/Spectrograms/",
                    default='./Data/Spectrograms/')
parser.add_argument("--slices-dir", help="Slice's files directory. Default ./Data/Slices/", default='./Data/Slices/')

args = parser.parse_args()

sliceDim = args.slice_dim
rawPath = args.raw_dir
specPath = args.spec_dir
slicesPath = args.slices_dir

print("---- Configuration ----")
print("Slice dimension: {}".format(sliceDim))
print("Raw mp3 directory: {}".format(rawPath))
print("Spectrogram directory: {}".format(specPath))
print("Slices directory: {}".format(slicesPath))

audio2Image.convert_to_spectrogram(rawPath, specPath)
audio2Image.convert_to_slices(specPath, slicesPath)
