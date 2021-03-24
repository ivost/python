

pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime

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

on Mac

./run.sh
tflite interpreter
0.919720: 653:military uniform
0.017762: 907:Windsor tie
0.007507: 668:mortarboard
0.005419: 466:bulletproof vest
0.003828: 458:bow tie, bow-tie, bowtie
time: 34.587ms

tflite_runtime interpreter
0.919721: 653:military uniform
0.017762: 907:Windsor tie
0.007507: 668:mortarboard
0.005419: 466:bulletproof vest
0.003828: 458:bow tie, bow-tie, bowtie
time: 43.132ms


CONVERSION
https://www.tensorflow.org/lite/convert

https://www.tensorflow.org/guide/saved_model


usage: tflite_convert [-h] --output_file OUTPUT_FILE
                      [--saved_model_dir SAVED_MODEL_DIR | --keras_model_file KERAS_MODEL_FILE]
                      [--enable_v1_converter]
                      [--experimental_new_converter [EXPERIMENTAL_NEW_CONVERTER]]


tflite_convert \
  --saved_model_dir=./mobilenet_v1_1.0_224/ \
  --output_file=./mobilenet.tflite
  

  



