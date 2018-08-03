"""Moves all files in all subdirectories to their parent directory."""
# TODO: Generalize
from os.path import exists, isdir, isfile, join
import numpy as np
import os
import random

parent_dir = input("The directory the subdirectories are in: ")

for subdir in [join(parent_dir, d) for d in os.listdir(parent_dir) if isdir(join(parent_dir, d))]:
	print(subdir)
	print(os.listdir(subdir))
	for f in [file for file in os.listdir(subdir) if isfile(join(subdir, file))]:
		print(f"renamed {join(subdir, f)} to {join(parent_dir, f)}")
		os.rename(join(subdir, f), join(parent_dir, f))
