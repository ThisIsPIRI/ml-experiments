import csv
import numpy as np

import linear_regression


def main():
	with open("processed_train.csv") as f_train:
		reader = csv.reader(f_train)
		int_converter = [[float(f) for f in l] for l in list(reader)[1:]]
		d_train = np.array([list(r) for r in int_converter])
		# TODO: read labels
	linear_regression.train(d_train, d_labels)


if __name__ == "__main__":
	main()
