

https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/examples/python/


# Get photo

wget https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/examples/label_image/testdata/grace_hopper.bmp 

# Get model
wget https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224.tgz 

# Get labels
wget https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_1.0_224_frozen.tgz  | tar xzv -C /tmp  mobilenet_v1_1.0_224/labels.txt

python3 label_image.py \
  --model_file ./model/mobilenet_v1_1.0_224.tflite \
  --label_file ./model/labels.txt \
  --image ./grace_hopper.bmp

