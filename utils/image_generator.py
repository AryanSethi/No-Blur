from tensorflow.keras.utils import Sequence
import numpy as np
import os
import cv2

class DataGenerator(Sequence):

    def __init__(self, base_dir, base_dir2, output_size, shuffle=False, batch_size=10):
        self.base_dir = base_dir
        self.base_dir2 = base_dir2
        self.output_size = output_size
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.all_x = os.listdir(base_dir)
        self.all_y = os.listdir(base_dir2)
        self.on_epoch_end()

    def on_epoch_end(self):
        self.indices = np.arange(len(self.all_x))
        if self.shuffle:
            np.random.shuffle(self.indices)

    def __len__(self):
        return int(len(self.all_x) / self.batch_size)

    def __getitem__(self, idx):
        X = np.empty((self.batch_size, *self.output_size, 3))
        Y = np.empty((self.batch_size, *self.output_size, 3))

        indices = self.indices[idx * (self.batch_size): (idx + 1) * (self.batch_size)]

        for i, j in enumerate(indices):
            img_path = os.path.join(self.base_dir, self.all_x[j])
            img_path2 = os.path.join(self.base_dir2, self.all_y[j])

            img = cv2.imread(img_path)
            img = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), self.output_size)
            img2 = cv2.imread(img_path2)
            img2 = cv2.resize(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), self.output_size)
            #       print(img_path,img_path2)

            X[i,] = img
            Y[i,] = img2
        X = X.astype('float32') / 255
        Y = Y.astype('float32') / 255

        return X, Y