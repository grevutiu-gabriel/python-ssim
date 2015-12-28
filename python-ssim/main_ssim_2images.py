'''
File main_single_image.py
Created on 21 nov. 2011
@author: Antoine Vacavant, ISIT lab, antoine.vacavant_AT_iut.u-clermont1.fr, http://isit.u-clermont1.fr/~anvacava
'''

#Possible use of matplotlib from http://http://matplotlib.sourceforge.net/
from pylab import * 
import matplotlib.pyplot as plt

#More imports
import Image
import numpy
import ImageOps

#ssim.py to compute SSIM
import ssim

'''
Get 2D matrix from an image file, possibly displayed with matplotlib 
@param path: Image file path on HD
@return A 2D matrix
''' 
def build_mat_from_grayscale_image(path):
    img=Image.open(str(path))
    img=ImageOps.grayscale(img)
    imgData=img.getdata()
    imgTab=numpy.array(imgData)
    w,h=img.size
    imgMat=numpy.reshape(imgTab,(h,w))
    
    return imgMat

'''
Main program
'''
if __name__ == '__main__':

    #First image 
    imgRefMat=build_mat_from_grayscale_image("einstein.gif")
    (w,h) = (imgRefMat.shape[0],imgRefMat.shape[1])
    
    #First subplot
    figure()
    subplot(121)
    plt.imshow(imgRefMat, cmap=cm.gray, hold=True)
    
    #Second image
    imgOutMat=build_mat_from_grayscale_image("impulse.gif")
    
    #Second subplot
    subplot(122)
    plt.imshow(imgOutMat, cmap=cm.gray, hold=True)
    plt.show()
    
    #Compute SSIM
    cSSIM=ssim.compute_ssim(imgRefMat,imgOutMat)
    
    print "SSIM=", cSSIM
