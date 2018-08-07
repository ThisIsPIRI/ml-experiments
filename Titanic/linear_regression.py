import numpy as np
import random
import tensorflow as tf

parameters = None


def train(d_train, d_labels):
	"""Trains a linear regression model.
	d_train:
	d_labels: A 1-dimensional array."""
	global parameters
	t_train = tf.placeholder(tf.float32)
	parameters = tf.transpose(tf.expand_dims(tf.Variable(np.array([random.random() for i in range(d_train.shape[1])]), dtype=tf.float32), 0))
	result = tf.matmul(t_train, parameters)
	loss = tf.losses.sigmoid_cross_entropy(d_labels, result)
	optimizer = tf.train.AdamOptimizer().minimize(loss)
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		for i in range(100):
			sess.run(optimizer, feed_dict={t_train: d_train})


def predict(d_to_predict):
	if parameters is None:
		return  # TODO: Load parameters from disk
	t_to_predict = tf.placeholder(tf.float32)

	result = tf.matmul(t_to_predict, parameters)
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		return sess.run(result, feed_dict={t_to_predict: d_to_predict})