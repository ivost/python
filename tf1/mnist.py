from __future__ import print_function

import matplotlib.pyplot as plt
import os
import urllib
import tensorflow as tf
import numpy as np
import struct
import time

IMAGE_SIZE = 28
PIXEL_DEPTH = 255
NUM_LABELS = 10
# dead url
SOURCE_URL = 'http://yann.lecun.com/exdb/mnist/'
WORK_DIRECTORY = "/tmp/mnist-data"
data_dir = '/Users/stoyaiv/mnist/data/'
train_data_filename = data_dir + 'train-images-idx3-ubyte'
train_labels_filename = data_dir + 'train-labels-idx1-ubyte'
test_data_filename = data_dir + 't10k-images-idx3-ubyte'
test_labels_filename = data_dir + 't10k-labels-idx1-ubyte'
TRAIN_SIZE = 60000
TEST_SIZE = 10000
VALIDATION_SIZE = 5000
sanity_show = False


def maybe_download(filename):
    """A helper to download the data files if not present."""
    if not os.path.exists(WORK_DIRECTORY):
        os.mkdir(WORK_DIRECTORY)
    filepath = os.path.join(WORK_DIRECTORY, filename)
    if not os.path.exists(filepath):
        print('Downloading', SOURCE_URL + filename)
        filepath, _ = urllib.urlretrieve(SOURCE_URL + filename, filepath)
        statinfo = os.stat(filepath)
        print('Successfully downloaded', filename, statinfo.st_size, 'bytes.')
    else:
        print('Already downloaded', filename)
    return filepath

# def download_mnist():
#     train_data_filename = maybe_download('train-images-idx3-ubyte.gz')
#     train_labels_filename = maybe_download('train-labels-idx1-ubyte.gz')
#     test_data_filename = maybe_download('t10k-images-idx3-ubyte.gz')
#     test_labels_filename = maybe_download('t10k-labels-idx1-ubyte.gz')

#download_mnist()

def show_mnist_data(image):
    # Print the first few values of image.
    # print('First 10 pixels:', image[:10])

    # We'll show the image and its pixel value histogram side-by-side.
    _, (ax1, ax2) = plt.subplots(1, 2)

    # To interpret the values as a 28x28 image, we need to reshape
    # the numpy array, which is one dimensional.
    ax1.imshow(image.reshape(IMAGE_SIZE, IMAGE_SIZE), cmap=plt.cm.Greys)
    ax2.hist(image, bins=20, range=[0, 255])
    plt.show()


def peek_mnist_data(file_path):
    """
    Unpack mnist data file using the documented format:
    [offset] [type]          [value]          [description]
    0000     32 bit integer  0x00000803(2051) magic number
    0004     32 bit integer  60000            number of images
    0008     32 bit integer  28               number of rows
    0012     32 bit integer  28               number of columns
    0016     unsigned byte   ??               pixel
    0017     unsigned byte   ??               pixel
    ........
    xxxx     unsigned byte   ??               pixel
    Pixels are organized row-wise. Pixel values are 0 to 255.
    0 means background (white), 255 means foreground (black).
    """
    with open(file_path, "rb") as f:
        # Print the header fields.
        for field in ['magic number', 'image count', 'rows', 'columns']:
            # struct.unpack reads the binary data provided by f.read.
            # The format string '>i' decodes a big-endian integer, which
            # is the encoding of the data.
            print(field, struct.unpack('>i', f.read(4))[0])

        # Read the first 28x28 set of pixel values.
        # Each pixel is one byte, [0, 255], a uint8.
        buf = f.read(IMAGE_SIZE * IMAGE_SIZE)
        image = np.frombuffer(buf, dtype=np.uint8)
        show_mnist_data(image)
        return image

def peek_mnist_labels(file_path):
    """
    unpack MNIST label file.
    The format here is similar: a magic number followed by a count followed by the labels as
    uint8 values. In more detail:
    [offset] [type]          [value]          [description]
    0000     32 bit integer  0x00000801(2049) magic number (MSB first)
    0004     32 bit integer  10000            number of items
    0008     unsigned byte   ??               label
    0009     unsigned byte   ??               label
    ........
    xxxx     unsigned byte   ??               label    """
    with open(file_path, "rb") as f:
        # Print the header fields.
        for field in ['magic number', 'label count']:
            print(field, struct.unpack('>i', f.read(4))[0])

        print('First label:', struct.unpack('B', f.read(1))[0])


def extract_data(file_path, num_images):
    """Extract the images into a 4D tensor [image index, y, x, channels].

    For MNIST data, the number of channels is always 1.

    Values are rescaled from [0, 255] down to [-0.5, 0.5].
    """
    print('Extracting', file_path)
    with open(file_path, "rb") as f:
        # Skip the magic number and dimensions; we know these values.
        f.read(16)

        buf = f.read(IMAGE_SIZE * IMAGE_SIZE * num_images)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        data = (data - (PIXEL_DEPTH / 2.0)) / PIXEL_DEPTH
        data = data.reshape(num_images, IMAGE_SIZE, IMAGE_SIZE, 1)
        if sanity_show:
            # sanity - first 2 images
            # print('data shape', data.shape)
            _, (ax1, ax2) = plt.subplots(1, 2)
            ax1.imshow(data[0].reshape(IMAGE_SIZE, IMAGE_SIZE), cmap=plt.cm.Greys);
            ax2.imshow(data[1].reshape(IMAGE_SIZE, IMAGE_SIZE), cmap=plt.cm.Greys);
            plt.show()

        return data


def extract_labels(file_path, num_images):
    """Extract the labels into a 1-hot matrix [image index, label index]."""
    print('Extracting', file_path)
    with open(file_path, "rb") as f:
        # Skip the magic number and count; we know these values.
        f.read(8)
        buf = f.read(1 * num_images)
        labels = np.frombuffer(buf, dtype=np.uint8)
        # Convert to dense 1-hot representation.
        vectors = (np.arange(NUM_LABELS) == labels[:, None]).astype(np.float32)
        # first 2 are 5, 0 (train) and 7, 2 (test)
        if sanity_show:
            print('labels shape', vectors.shape)
            print('First label vector', vectors[0])
            print('Second label vector', vectors[1])

        return vectors

#peek_mnist_data(train_data_filename)
#peek_mnist_labels(train_labels_filename)

#peek_mnist_data(test_data_filename)
#peek_mnist_labels(test_labels_filename)

train_data = extract_data(train_data_filename, TRAIN_SIZE)

test_data = extract_data(test_data_filename, TEST_SIZE)

train_labels = extract_labels(train_labels_filename, TRAIN_SIZE)

test_labels = extract_labels(test_labels_filename, TEST_SIZE)

validation_data = train_data[:VALIDATION_SIZE, :, :, :]
validation_labels = train_labels[:VALIDATION_SIZE]
train_data = train_data[VALIDATION_SIZE:, :, :, :]
train_labels = train_labels[VALIDATION_SIZE:]

train_size = train_labels.shape[0]

print('Validation shape', validation_data.shape)
print('Train size', train_size)

"""
Defining the model
Now that we've prepared our data, we're ready to define our model.
The comments describe the architecture, which fairly typical of models that process image data. The raw input passes through several convolution and max pooling layers with rectified linear activations before several fully connected layers and a softmax loss for predicting the output class. During training, we use dropout.
We'll separate our model definition into three steps:
Defining the variables that will hold the trainable weights.
Defining the basic model graph structure described above. And,
Stamping out several copies of the model graph for training, testing, and validation.
We'll start with the variables.
"""
# We'll bundle groups of examples during training for efficiency.
# This defines the size of the batch.
BATCH_SIZE = 60
# We have only one channel in our grayscale images.
NUM_CHANNELS = 1
# The random seed that defines initialization.
SEED = 42

# This is where training samples and labels are fed to the graph.
# These placeholder nodes will be fed a batch of training data at each
# training step, which we'll write once we define the graph structure.
train_data_node = tf.placeholder(
  tf.float32,
  shape=(BATCH_SIZE, IMAGE_SIZE, IMAGE_SIZE, NUM_CHANNELS))
train_labels_node = tf.placeholder(tf.float32,
                                   shape=(BATCH_SIZE, NUM_LABELS))

# For the validation and test data, we'll just hold the entire dataset in
# one constant node.
validation_data_node = tf.constant(validation_data)
test_data_node = tf.constant(test_data)

# The variables below hold all the trainable weights. For each, the
# parameter defines how the variables will be initialized.
conv1_weights = tf.Variable(
  tf.truncated_normal([5, 5, NUM_CHANNELS, 32],  # 5x5 filter, depth 32.
                      stddev=0.1,
                      seed=SEED))
conv1_biases = tf.Variable(tf.zeros([32]))
conv2_weights = tf.Variable(
  tf.truncated_normal([5, 5, 32, 64],
                      stddev=0.1,
                      seed=SEED))
conv2_biases = tf.Variable(tf.constant(0.1, shape=[64]))
fc1_weights = tf.Variable(  # fully connected, depth 512.
  tf.truncated_normal([IMAGE_SIZE // 4 * IMAGE_SIZE // 4 * 64, 512],
                      stddev=0.1,
                      seed=SEED))
fc1_biases = tf.Variable(tf.constant(0.1, shape=[512]))
fc2_weights = tf.Variable(
  tf.truncated_normal([512, NUM_LABELS],
                      stddev=0.1,
                      seed=SEED))
fc2_biases = tf.Variable(tf.constant(0.1, shape=[NUM_LABELS]))


def model(data, train=False):
    """
    Now that we've defined the variables to be trained, we're ready to wire them
    together into a TensorFlow graph.
    We'll define a helper to do this, model, which will return copies of the graph suitable for training and testing. Note the train argument, which controls whether or not dropout is used in the hidden layer.
    (We want to use dropout only during training.)
    The Model definition.
    """
    # 2D convolution, with 'SAME' padding (i.e. the output feature map has
    # the same size as the input). Note that {strides} is a 4D array whose
    # shape matches the data layout: [image index, y, x, depth].
    conv = tf.nn.conv2d(data,
                        conv1_weights,
                        strides=[1, 1, 1, 1],
                        padding='SAME')

    # Bias and rectified linear non-linearity.
    relu = tf.nn.relu(tf.nn.bias_add(conv, conv1_biases))

    # Max pooling. The kernel size spec ksize also follows the layout of
    # the data. Here we have a pooling window of 2, and a stride of 2.
    pool = tf.nn.max_pool(relu,
                          ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1],
                          padding='SAME')
    conv = tf.nn.conv2d(pool,
                        conv2_weights,
                        strides=[1, 1, 1, 1],
                        padding='SAME')
    relu = tf.nn.relu(tf.nn.bias_add(conv, conv2_biases))
    pool = tf.nn.max_pool(relu,
                          ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1],
                          padding='SAME')

    # Reshape the feature map cuboid into a 2D matrix to feed it to the
    # fully connected layers.
    pool_shape = pool.get_shape().as_list()
    reshape = tf.reshape(
        pool,
        [pool_shape[0], pool_shape[1] * pool_shape[2] * pool_shape[3]])

    # Fully connected layer. Note that the '+' operation automatically
    # broadcasts the biases.
    hidden = tf.nn.relu(tf.matmul(reshape, fc1_weights) + fc1_biases)

    # Add a 50% dropout during training only. Dropout also scales
    # activations such that no rescaling is needed at evaluation time.
    if train:
        hidden = tf.nn.dropout(hidden, 0.5, seed=SEED)
    return tf.matmul(hidden, fc2_weights) + fc2_biases


def error_rate(predictions, labels):
    import numpy
    """Return the error rate and confusions."""
    correct = numpy.sum(numpy.argmax(predictions, 1) == numpy.argmax(labels, 1))
    total = predictions.shape[0]

    error = 100.0 - (100 * float(correct) / float(total))

    confusions = numpy.zeros([10, 10], numpy.float32)
    bundled = zip(numpy.argmax(predictions, 1), numpy.argmax(labels, 1))
    for predicted, actual in bundled:
        confusions[predicted, actual] += 1

    return error, confusions

"""
Having defined the basic structure of the graph, we're ready to stamp out multiple copies
for training, testing, and validation.
Here, we'll do some customizations depending on which graph we're constructing. train_prediction holds the training
graph, for which we use cross-entropy loss and weight regularization. We'll adjust the learning rate
during training -- that's handled by the exponential_decay operation, which is itself an argument to
the MomentumOptimizer that performs the actual training.
The vaildation and prediction graphs are much simpler the generate -- we need only to
create copies of the model with the validation and test inputs and a softmax classifier as the output.
"""
# Training computation: logits + cross-entropy loss.
logits = model(train_data_node, True)
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
  labels=train_labels_node, logits=logits))

# L2 regularization for the fully connected parameters.
regularizers = (tf.nn.l2_loss(fc1_weights) + tf.nn.l2_loss(fc1_biases) +
                tf.nn.l2_loss(fc2_weights) + tf.nn.l2_loss(fc2_biases))
# Add the regularization term to the loss.
loss += 5e-4 * regularizers

# Optimizer: set up a variable that's incremented once per batch and
# controls the learning rate decay.
batch = tf.Variable(0)
# Decay once per epoch, using an exponential schedule starting at 0.01.
learning_rate = tf.train.exponential_decay(
  0.01,                # Base learning rate.
  batch * BATCH_SIZE,  # Current index into the dataset.
  train_size,          # Decay step.
  0.95,                # Decay rate.
  staircase=True)
# Use simple momentum for the optimization.
optimizer = tf.train.MomentumOptimizer(learning_rate,
                                       0.9).minimize(loss,
                                                     global_step=batch)

# Predictions for the minibatch, validation set and test set.
train_prediction = tf.nn.softmax(logits)
# We'll compute them only once in a while by calling their {eval()} method.
validation_prediction = tf.nn.softmax(model(validation_data_node))
test_prediction = tf.nn.softmax(model(test_data_node))

print('Running')

#Now that we have the training, test, and validation graphs, we're ready to actually go through
# the training loop and periodically evaluate loss and error.

# Create a new interactive session that we'll use in
# subsequent code cells.
s = tf.InteractiveSession()

# Use our newly created session as the default for
# subsequent operations.
s.as_default()

# Initialize all the variables we defined above.
tf.global_variables_initializer().run()

BATCH_SIZE = 60

# Now we're ready to perform operations on the graph. Let's start with one round of training.
# We're going to organize our training steps into batches for efficiency;
# i.e., training using a small set of examples at each step rather than a single example.
# Grab the first BATCH_SIZE examples and labels.
batch_data = train_data[:BATCH_SIZE, :, :, :]
batch_labels = train_labels[:BATCH_SIZE]

# This dictionary maps the batch data (as a numpy array) to the
# node in the graph it should be fed to.
feed_dict = {train_data_node: batch_data,
             train_labels_node: batch_labels}

# Run the graph and fetch some of the nodes.
_, l, lr, predictions = s.run(
  [optimizer, loss, learning_rate, train_prediction],
  feed_dict=feed_dict)

#print(predictions[0])

# Train over the first 1/4th of our training set.
steps = train_size // BATCH_SIZE

start = time.clock()
start0 = time.clock()
#start = time.perf_counter()

for step in range(steps):
    # Compute the offset of the current minibatch in the data.
    # Note that we could use better randomization across epochs.
    offset = (step * BATCH_SIZE) % (train_size - BATCH_SIZE)
    batch_data = train_data[offset:(offset + BATCH_SIZE), :, :, :]
    batch_labels = train_labels[offset:(offset + BATCH_SIZE)]
    # This dictionary maps the batch data (as a numpy array) to the
    # node in the graph it should be fed to.
    feed_dict = {train_data_node: batch_data,
                 train_labels_node: batch_labels}
    # Run the graph and fetch some of the nodes.
    _, l, lr, predictions = s.run(
        [optimizer, loss, learning_rate, train_prediction],
        feed_dict=feed_dict)

    # Print out the loss periodically.
    if step % 100 == 0:
        error, _ = error_rate(predictions, batch_labels)
        elapsed = time.clock() - start
        print('Step %d of %d, elapsed %.2f sec' % (step, steps, elapsed))
        print('Mini-batch loss: %.5f Error: %.5f Learning rate: %.5f' % (l, error, lr))
        print('Validation error: %.1f%%' % error_rate(
            validation_prediction.eval(), validation_labels)[0])
        start = time.clock()

print("TOTAL", time.clock() - start0, "sec")
