import numpy as np
import cv2
import os


def run1():
    imgs = os.listdir("/home/jason/Data/ACGPN/Data_preprocessing/test_label/")
    dye = np.random.rand(30, 3) * 255

    for file in imgs:
        p = cv2.imread("/home/jason/Data/ACGPN/Data_preprocessing/test_label/" + file, 0)
        q = np.unique(p)
        img1 = np.zeros([256, 192, 3])
        img2 = np.zeros([256, 192, 3])
        for i in q:
            if i > 0:
                if i!= 11 and i != 13:
                    img1[p==i]=dye[i]

                if i == 11 or i == 13:
                    img2[p == i] = dye[i]
        cv2.imwrite("/home/jason/Data/ACGPN/Data_preprocessing/origin/"+file,img1)
        cv2.imwrite("/home/jason/Data/ACGPN/Data_preprocessing/result/" + file, img2)


img = cv2.imread("/home/jason/Data/ACGPN/Data_preprocessing/test_img/002502_0.jpg")
img = cv2.Canny(img,75,175)
cv2.imwrite("/home/jason/Data/ACGPN/Data_preprocessing/result.png",img)
run1()
# img1 = cv2.imread("/home/jason/Data/ACGPN/Data_preprocessing/result1.png")
# img2 = cv2.imread("/home/jason/Data/ACGPN/Data_preprocessing/result2.png")
# img3 = cv2.imread("/home/jason/Data/ACGPN/Data_preprocessing/result3.png")
# img = np.concatenate([img1,img2,img3],0)
# cv2.imwrite("/home/jason/Data/ACGPN/Data_preprocessing/result.png",img)
