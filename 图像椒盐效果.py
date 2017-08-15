import cv2
import numpy as np

import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('ti.jpg')


img2=cv2.merge([b//3,g//3,r//3])
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def salt(img,n):
    for k in range(n):
        i=int(np.random.random()*img.shape[0])
        j=int(np.random.random()*img.shape[1])
        if img.ndim==3:
            img[i,j,:]=255
        else:
            img[i,j]=0
salt(img,100)
salt(img3,200)
b,g,r=cv2.split(img)
c=np.zeros(img.shape,dtype=img.dtype)
c[:,:,:]=img[:,:,:]

cv2.imshow('img',img)
cv2.imshow('img3',img3)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
cv2.imshow('c',c)
cv2.waitKey(0)
cv2.destroyAllWindows()