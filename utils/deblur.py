from tensorflow import keras
import tensorflow as tf
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from utils import image_generator as ig


testing  = ig.DataGenerator('..\data/test_x/test_x','..\data/test_y/test_y',(128,128), batch_size=10, shuffle=False)

model= keras.models.load_model('../best_models/try5')   ################################################
name=0
for batch in range(150):
    testx, testy = testing[batch]
    predictions = model.predict(testx)
    i=0
    for prediction in predictions:
        prediction = cv2.resize(prediction*255,(300,300))
        prediction = cv2.cvtColor(prediction.astype(np.uint8),cv2.COLOR_RGB2BGR)

        test_x_image = cv2.resize(testx[i]*255,(300,300))
        test_x_image = test_x_image.astype(np.uint8)
        test_x_image = cv2.cvtColor(test_x_image, cv2.COLOR_RGB2BGR)

        test_y_image = cv2.resize(testy[i]*255,(300,300))
        test_y_image = test_y_image.astype(np.uint8)
        test_y_image = cv2.cvtColor(test_y_image, cv2.COLOR_RGB2BGR)

        final= cv2.hconcat([test_x_image,test_y_image,prediction])
        write_name = '..\eval/deblur/try3/' + 'd-'+str(name)+'-'+str(i)+'.jpg'   ###################################
        cv2.imwrite(write_name, final)
        i+=1
    name+=1










