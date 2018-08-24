import csv
import numpy as np


def read_input(filename):
	with open(filename) as file:
		reader = csv.reader(file)
		int_converter = [[float(f) for f in l] for l in list(reader)[1:]]
		return np.array([list(r) for r in int_converter])


def read_column(filename, column_index, start_row=0):
	with open(filename) as file:
		reader = csv.reader(file)
		return np.array([float(r[column_index]) for r in list(reader)[start_row:]])


def main():
	d_train = np.delete(read_input("processed_train.csv"), 0, 1)  # Remove the 'Survived' column
	d_train_labels = read_column("train.csv", 1, 1)
	train_len = len(d_train)
	permut = np.random.permutation(train_len)
	d_train = d_train[permut]
	d_train_labels = d_train_labels[permut]
	d_val = d_train[0:train_len // 4]
	d_val_labels = d_train_labels[0:train_len // 4]
	d_train = d_train[train_len // 4:train_len]
	d_train_labels = d_train_labels[train_len // 4:train_len]
	print("Data read")


if __name__ == "__main__":
	main()
