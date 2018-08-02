import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def main():
	IMG_NUM = 2256
	images = np.empty(IMG_NUM, dtype=np.ndarray)
	for i in range(IMG_NUM):
		images[i] = plt.imread(f"C:\CloudData\{i}.jpg", format="jpeg")
	print(images)


if __name__ == "__main__":
	main()
