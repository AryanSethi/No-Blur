import os
import shutil
import tensorflow

train_x_path= 'data/train_x'
train_y_path= 'data/train_y'

train_x_files= os.listdir(train_x_path)
train_y_files= os.listdir(train_y_path)

for x_image in train_x_files[10001:13001]:
    shutil.move('data/train_x/%s'%x_image,'data/valid_x')

for y_image in train_y_files[10001:13001]:
    shutil.move('data/train_y/%s'%y_image,'data/valid_y')



