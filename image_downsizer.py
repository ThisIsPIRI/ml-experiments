"""Downsize all images in a directory and saves them in another with ImageMagick."""
from os import listdir
from os.path import isfile, join
import re
import subprocess

dir_from = input("Downsize images from: ")
dir_to = input("To: ")
extension = input("Extension of images(without a dot): ")
hor, ver = [int(x) for x in input("Resulting width and height(separated by a space):").split()]

images = [i for i in listdir(dir_from) if isfile(join(dir_from, i)) and re.match(".*\." + extension, i, re.IGNORECASE)]  # TODO: support multiple extensions at once
