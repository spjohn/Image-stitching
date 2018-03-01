# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:54:48 2018

@author: VRIPLAB4
"""
from PIL import Image
import numpy as np
from skimage.transform import AffineTransform
from numpy.linalg import inv
from scipy.misc import toimage

#p1=np.array([646,263])
#p2=np.array([411,251])
#p3=np.array([526,195])
#
#P1=np.array([418,321])
#P2=np.array([188,304])
#P3=np.array([307,252])
#
#T=np.array([[p1[0],p1[1],1,0,0,0],
#            [0,0,0,p1[0],p1[1],1],
#            [p2[0],p2[1],1,0,0,0],
#            [0,0,0,p2[0],p2[1],1],
#            [p3[0],p3[1],1,0,0,0],
#            [0,0,0,p3[0],p3[1],1]])
#p=np.array([P1[0],P1[1],P2[0],P2[1],P3[0],P3[1]])
#
#Tinv=inv(T)
#res=np.dot(Tinv,p)
#
#rmat=np.reshape(res,(2,3))
#
#im=Image.open('Image1.jpg')
#size=im.size
#
#newmat=np.zeros((size[0]+258,size[1],3))
#
#for i in range(0,size[0]-1):
#    for j in range(0,size[1]-1):
#        a=im.getpixel((i,j))
#        hc=np.array([i,j,1])
#        newhc=np.dot(rmat,hc)
#        if(newhc[0]>0 and newhc[1]<size[1]-1 and newhc[1]>0 and newhc[0]<size[0]+258-1):
#            newmat[newhc[0],newhc[1]]=a
#
##toimage(np.transpose(newmat)).show()
#toimage(np.transpose(newmat)).save('affine.png')
#---------------------------------------------------------------------
P1=np.array([646,263])
P2=np.array([411,251])
P3=np.array([526,195])

p1=np.array([418,321])
p2=np.array([188,304])
p3=np.array([307,252])

T1=np.array([[p1[0],p1[1],1,0,0,0],
            [0,0,0,p1[0],p1[1],1],
            [p2[0],p2[1],1,0,0,0],
            [0,0,0,p2[0],p2[1],1],
            [p3[0],p3[1],1,0,0,0],
            [0,0,0,p3[0],p3[1],1]])
p1=np.array([P1[0],P1[1],P2[0],P2[1],P3[0],P3[1]])

Tinv1=inv(T1)
res1=np.dot(Tinv1,p1)

rmat1=np.reshape(res1,(2,3))
im2=Image.open('Image2.jpg')
size=im2.size

newmat1=np.zeros((size[0]+258,size[1],3))

for i in range(0,size[0]-1):
    for j in range(0,size[1]-1):
        a=im2.getpixel((i,j))
        hc=np.array([i,j,1])
        newhc=np.dot(rmat1,hc)
        if(newhc[0]>0 and newhc[1]<size[1]-1 and newhc[1]>0 and newhc[0]<size[0]+258-1):
            newmat1[np.int(newhc[0]),np.int(newhc[1])]=a
toimage(np.transpose(newmat1)).show()
toimage(np.transpose(newmat1)).save('affine1.png')
#lab3-----------------------------------------------------------------
#q=np.zeros((600,1058,3))
#im2=Image.open('Image2.jpg')
#im2.show()
#size=im2.size
#
#im3=Image.open('affine.png')
#
#
#for i in range(0,600):
#    for j in range(0,800):
#     #   a=np.array([i,j,1])
#      #  a1=np.dot(rmat,a)
#      #  ind1=np.ceil(np.abs(a1[0]))
#      #  ind2=np.ceil(np.abs(a1[1]))
#        b=im3.getpixel((j,i))
#        q[i][j]=b
#for i in range(0,600):
#    for j in range(258,800):
#        a=im2.getpixel((j,i))
#        q[i][j+258]=a
#
#toimage(q).show()
#toimage(q).save('Stitched.png')
#-----------------------------------------
q1=np.zeros((600,1058,3))
im2=Image.open('Image1.jpg')
#im2.show()
size=im2.size

im4=Image.open('affine1.png')


for i in range(0,600):
    for j in range(0,1058):
        b=im4.getpixel((j,i))
        q1[i][j]=b
for i in range(0,600):
    for j in range(0,258):
        a=im2.getpixel((j,i))
        q1[i][j]=a

toimage(q1).show()
toimage(q1).save('Stitched1.png')