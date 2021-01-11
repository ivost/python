from time import sleep

import lmdb
import pickle
import numpy as np
from PIL import Image
import csv
from timeit import timeit
from pathlib import Path


class StoredImage:
    def __init__(self, image, label):
        self.channels = image.shape[2]
        self.size = image.shape[:2]
        self.image = image.tobytes()
        self.label = label

    def get_image(self):
        """ Returns the image as a numpy array. """
        image = np.frombuffer(self.image, dtype=np.uint8)
        return image.reshape(*self.size, self.channels)


keep_aspect = True
show_image = False
base_width = 224
base_height = 224
keep_aspect = False
im_mode = 'RGB'

disk_dir = Path("data/disk/")
lmdb_dir = Path("data/lmdb/")
hdf5_dir = Path("data/hdf5/")


def store_single_lmdb(image, image_id, label):
    """ Stores a single image to a LMDB.
        Parameters:
        ---------------
        image       image array, (h, w, 3) to be stored
        image_id    integer unique ID for image
        label       image label
    """
    map_size = image.nbytes * 10

    # Create a new LMDB environment
    env = lmdb.open(str(lmdb_dir / f"single_lmdb"), map_size=map_size)

    # Start a new write transaction
    with env.begin(write=True) as txn:
        # All key-value pairs need to be strings
        value = StoredImage(image, label)
        key = f"{image_id:08}"
        txn.put(key.encode("ascii"), pickle.dumps(value))
    env.close()


def read_single_lmdb(image_id):

    """ Stores a single image to LMDB.
        Parameters:
        ---------------
        image_id    integer unique ID for image

        Returns:
        ----------
        image       numpy image array
        label       associated meta data, int label
    """

    # Open the LMDB environment
    env = lmdb.open(str(lmdb_dir / f"single_lmdb"), readonly=True)

    # Start a new read transaction
    with env.begin() as txn:
        # Encode the key the same way as we stored it
        data = txn.get(f"{image_id:08}".encode("ascii"))
        im = pickle.loads(data)
        # Retrieve the relevant bits
        image = im.get_image()
        label = im.label

    env.close()
    return image, label


def main():
    disk_dir.mkdir(parents=True, exist_ok=True)
    lmdb_dir.mkdir(parents=True, exist_ok=True)
    hdf5_dir.mkdir(parents=True, exist_ok=True)
    # image = Image.open(args.input).convert('RGB').resize(size, Image.ANTIALIAS)
    infile = "./data/images/image1.jpg"
    with Image.open(infile) as im:
        print(f"Reading {infile}, format: {im.format}, size: {im.size}, mode: {im.mode}")
        if keep_aspect:
            ratio = (base_width / float(im.size[0]))
            h = int((float(im.size[1]) * float(ratio)))
            print(f"Resizing {100*ratio}%, w: {base_width},  h: {h}")
            im = im.resize((base_width, h), Image.ANTIALIAS)
        else:
            print(f"Resizing to {base_width}, {base_height}")
            im = im.resize((base_width, base_height), Image.ANTIALIAS)

        if show_image:
            im.show()

        if im.mode != im_mode:
            im = im.convert(im_mode)
        ima = np.asarray(im, dtype=np.float32) / 255
        print(f"array shape {ima.shape}")

        # sleep(1)
        im_id = 3
        store_single_lmdb(ima, im_id, "dog")

        a, lab = read_single_lmdb(im_id)
        print(f"label {lab}")


if __name__ == '__main__':
    main()
