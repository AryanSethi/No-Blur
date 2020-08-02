import cv2
import os
import random

source_path= 'all/'
image_number=0
blur_levels=[ [(5,5),5] , [(9,9),0], [(3,3),20], [(5,5),0], [(3,3),20] , [(11,11),0] ]

all_images= os.listdir(source_path)



def random_element():
    element_number = random.randint(0,5)
    return element_number

y1,x1= 0,0
y2,x2=200,200

if not os.path.exists('train_y/image-1.jpg'):
    for image in all_images[:5]:
        img = cv2.imread('all/%s'%image)

        img= cv2.resize(img,(800,600))

        index=random_element()

        for y_range in range(3):
            for x_range in range(4):
                image_name='image'+str(image_number)

                portion=img[y1:y2,x1:x2]
                cv2.imwrite('train_y/%s.jpg'%image_name,portion)
                kernel= blur_levels[index][0]
                intensity= blur_levels[index][1]
                portion_blur= cv2.GaussianBlur(portion,kernel,intensity)
                cv2.imwrite('train_x/%s.jpg'%image_name, portion_blur)
                x1+=200
                x2+=200

                image_number=image_number+1

            y1+=200
            y2+=200
            x1,x2=0,200

        y1, x1 = 0, 0
        y2, x2 = 200, 200




