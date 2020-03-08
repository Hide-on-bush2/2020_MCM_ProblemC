# import tensorflow as tf
import numpy as np
import tensorflow.compat.v1 as tf

#添加层
def add_layer(inputs, in_size, out_size, activation_function=None):
	Weights= tf.Variable(tf.random_normal([in_size, out_size]))
	biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
	Wx_plus_b = tf.matmul(inputs, Weights) + biases
	if activation_function is None:
		outputs = Wx_plus_b
	else:
		outputs = activation_function(Wx_plus_b)
	return outputs

def neural_network(data):
	tf.compat.v1.disable_v2_behavior()
	#训练的数据
	x_data = data[["score", "star_rating", "helpful_rating"]].values
	y_data = data[["export"]].values
	
	#定义结点准备接受数据
	xs = tf.placeholder(tf.float32, [None, 3])
	ys = tf.placeholder(tf.float32, [None, 1])

	#定义神经层：隐藏层和预测层
	l1 = add_layer(xs, 3, 10, activation_function=tf.nn.relu)
	prediction = add_layer(l1, 10, 1, activation_function=None)

	#定义loss表达式
	loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

	#选择optimizer使loss达到最小
	train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

	#对所有变量进行初始化
	init = tf.initialize_all_variables()
	sess = tf.Session()
	sess.run(init)

	#迭代1000次学习
	for i in range(1000):
		sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
		if i % 50 == 0:
			print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))
	saver = tf.train.Saver()
	saver.save(sess, "./neural_model/neural")

	return sess

# def load_model():
# 	with tf.Session() as sess:    
# 	    saver = tf.train.import_meta_graph('./neural_model/neural.meta')
# 	    saver.restore(sess,tf.train.latest_checkpoint('./neural_model'))
# 	    print(sess.run([0.9, 5, 1]))






