"""Splits a dataset, each sample of which is stored in a separate file, into train, test and validation sets and moves them into their respective subdirectories.
All files must be in one directory"""
# TODO: Generalize
from os.path import exists, isfile, join
import numpy as np
import os
import random

parent_dir = input("The directory the files are in: ")
ratios = [float(x) / 100 for x in input("Train/validation/test percentage(separated by a space): ").split()]
ratio_cumsum = np.insert(np.cumsum(ratios), 0, 0, axis=0)

files = [f for f in os.listdir(parent_dir) if isfile(join(parent_dir, f))]
random.shuffle(files)  # TODO: Use a better method

for i, s in enumerate(["train", "validation", "test"]):
	subdir = join(parent_dir, s)
	if not exists(subdir):
		os.mkdir(subdir)
	for f in files[int(round(len(files) * ratio_cumsum[i])):int(round(len(files) * ratio_cumsum[i + 1]))]:
		print(f"renamed {join(parent_dir, f)} to {join(subdir, f)}")
		os.rename(join(parent_dir, f), join(subdir, f))
