"""Downsize all images in a directory and saves them in another with ImageMagick."""
from os import listdir
from os.path import isfile, join
import re
import subprocess

dir_from = input("Downsize images from: ")
dir_to = input("To: ")
extension = input("Extension of images(without a dot): ")
dimension = input("Resulting width: ") + 'x' + input("Resulting height:") + "!"  # Escaped exclamation to make ImageMagick convert to the exact dimension instead of keeping the aspect ratio.

images = [join(dir_from, i).replace('\\', '\\\\') for i in listdir(dir_from) if isfile(join(dir_from, i)) and re.match(".*\." + extension, i, re.IGNORECASE)]  # TODO: support multiple extensions at once
for index, image in enumerate(images):
	print(image)
	subprocess.run(["magick", "convert", image, "-resize", dimension, join(dir_to, f"{index}.jpg")])
