#from tensorflow import keras
#from tensorflow.keras.utils import Sequence
#import tensorflow as tf
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


model=keras.models.load_model('..\best_models/try4')

for test_x_name,test_y_name in zip(os.listdir('..\data/test_x/test_x/'),os.listdir('..\data/test_y/test_y/')):
    test_x_path= "..\data/test_x/test_x/"+test_x_name
    test_y_path= "..\data/test_y/test_y/"+test_y_name

    test_x=cv2.imread(test_x_path)
    test_y=cv2.imread(test_y_path)
    prediction=model.predict(cv2.resize(test_x,(128,128) ) )
    cv2.resize(prediction,(200,200))
    final=cv2.hconcat([test_x,test_y,prediction])

    write_name='..\eval/deblur/'+test_x_name
    cv2.imwrite(write_name,final)



