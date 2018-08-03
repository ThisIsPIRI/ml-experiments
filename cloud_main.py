import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def main():
	IMG_NUM = 2256
	d_images = np.empty(IMG_NUM, dtype=np.ndarray)
	for i in range(IMG_NUM):
		d_images[i] = plt.imread(f"C:\CloudData\{i}.jpg", format="jpeg")
	t_images = tf.placeholder(dtype=tf.float32)
	dataset = tf.data.Dataset.from_tensors(t_images)


if __name__ == "__main__":
	main()
