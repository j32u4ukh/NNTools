import tensorflow as tf


def addLayer(inputs, out_size, activation=None):
    Weights = tf.Variable(tf.random_normal([int(inputs.shape[1]), out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
    if activation is None:
        outputs = Wx_plus_b
    else:
        outputs = activation(Wx_plus_b)

    return outputs
