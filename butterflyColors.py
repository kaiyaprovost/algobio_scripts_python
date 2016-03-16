# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 15:08:22 2016

@author: Kaiya
"""

## part 1

import matplotlib.pyplot as plt  
import numpy as np               
img = plt.imread('C:/Users/Kaiya/Dropbox/Docs for Brian/THESIS/Field Work/FIGURES/box_with_PCA_means_forAOU.png')	#Read in image from bf1.png
plt.imshow(img)			#Load image into matplotlib
plt.show()
height = img.shape[0]
width = img.shape[1]
redImage = np.zeros((height,width,3))
greImage = np.zeros((height,width,3))
bluImage = np.zeros((height,width,3))
blaImage = np.zeros((height,width,3))
for i in range(height):
    print "processing row", i
    for j in range(width): 
         # only red channel
         redImage[i,j,0] = img[i,j,0] ## red channel
         redImage[i,j,1] = 0 ## green channel
         redImage[i,j,2] = 0 ## blue channel
         # only green channel 
         greImage[i,j,0] = 0 ## red channel
         greImage[i,j,1] = img[i,j,1] ## green channel
         greImage[i,j,2] = 0 ## blue channel  
         # only blue channel
         bluImage[i,j,0] = 0 ## red channel
         bluImage[i,j,1] = 0 ## green channel
         bluImage[i,j,2] = img[i,j,2] ## blue channel
         # black and white
         avg = np.mean(img[i,j,0:3])
         blaImage[i,j,0] = avg ## red channel
         blaImage[i,j,1] = avg ## green channel
         blaImage[i,j,2] = avg ## blue channel          
  
plt.imshow(redImage)		#Open window to show image (close to continue)
plt.show() 
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/redScale1.png',redImage)

plt.imshow(greImage)		#Open window to show image (close to continue)
plt.show()
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/greenScale1.png',greImage)

plt.imshow(bluImage)		#Open window to show image (close to continue)
plt.show()
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/blueScale1.png',bluImage)

plt.imshow(blaImage)		#Open window to show image (close to continue)
plt.show()
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/greyScale1.png',blaImage)

## part 2 : butterfly picture threshhold

import matplotlib.pyplot as plt  
import numpy as np               
img = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/bf1.png')	#Read in image from bf1.png
plt.imshow(img)			#Load image into matplotlib
plt.show()
height = img.shape[0]
width = img.shape[1]
butImage = np.zeros((height,width,3))
for i in range(height):
    for j in range(width):
        if np.sum(img[i,j,0:3]) < 2.7:
            butImage[i,j,0] = 0 ## red channel
            butImage[i,j,1] = 0 ## green channel
            butImage[i,j,2] = 0 ## blue channel
        else:
            butImage[i,j,0] = 1
            butImage[i,j,1] = 1
            butImage[i,j,2] = 1        
  
plt.imshow(butImage)		#Open window to show image (close to continue)
plt.show() 
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/whiteOnly1.png',butImage)

## part 3 : butterfly image difs

import matplotlib.pyplot as plt  
import numpy as np               
img1 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/bf1.png')	#Read in image from bf1.png
#plt.imshow(img1)			#Load image into matplotlib
#plt.show()

img2 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/bf2.png')	#Read in image from bf1.png
#plt.imshow(img2)			#Load image into matplotlib
#plt.show()

height1 = img1.shape[0]
width1 = img1.shape[1]

#height2 = img1.shape[0]
#width2 = img1.shape[1]

#if height1 == height2 and width1 == width2:
#    print "MATCH"
#else:
#    print "NO MATCH - CHECK IMAGES"

limit = 0.15

difImage = np.zeros((height1,width1,3))
for i in range(height1):
    for j in range(width1):
        redDif = np.absolute(np.subtract(img1[i,j,0],img2[i,j,0]))
        greDif = np.absolute(np.subtract(img1[i,j,1],img2[i,j,1]))
        bluDif = np.absolute(np.subtract(img1[i,j,2],img2[i,j,2]))
        #print (redDif+greDif+bluDif)/3
        if ((redDif+greDif+bluDif)/3) > (limit):
            difImage[i,j,0:3] = np.asarray([0,0,0])
        else:
            difImage[i,j] = img1[i,j,0:3]
            
        #difImage[i,j] = np.asarray([redDif,greDif,bluDif])        
        #if np.sum(img[i,j,0:3]) < 2.7:
        #    difImage[i,j,0] = 0 ## red channel
        #    difImage[i,j,1] = 0 ## green channel
        #    difImage[i,j,2] = 0 ## blue channel
        #else:
        #    difImage[i,j,0] = 1
        #    difImage[i,j,1] = 1
        #    difImage[i,j,2] = 1        
  
plt.imshow(difImage)		#Open window to show image (close to continue)
plt.show() 
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/difImage2.png',difImage)

## part 4 : CA drought

import matplotlib.pyplot as plt  
import numpy as np               
img2011 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/cali2011.png')	#Read in image from bf1.png
img2013 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/cali2013.png')	#Read in image from bf1.png
img2014 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/cali2014.png')	#Read in image from bf1.png

height1 = img2011.shape[0]
width1 = img2011.shape[1]

limit = 0.05
sno11Image = np.zeros((height1,width1,3))
sno13Image = np.zeros((height1,width1,3))
sno14Image = np.zeros((height1,width1,3))
count11 = 0
count13 = 0
count14 = 0
for i in range(height1):
    print "processing row", i
    for j in range(width1):
        if np.mean(img2011[i,j,0:3]) > (1-limit):
            count11 += 1
            sno11Image[i,j] = img2011[i,j,0:3]
        else:
            sno11Image[i,j,0:3] = np.asarray([0,0,0])

        if np.mean(img2013[i,j,0:3]) > (1-limit):
            count13 += 1
            sno13Image[i,j] = img2013[i,j,0:3]
        else:
            sno13Image[i,j,0:3] = np.asarray([0,0,0])
            
        if np.mean(img2014[i,j,0:3]) > (1-limit):
            count14 += 1
            sno14Image[i,j] = img2014[i,j,0:3]
        else:
            sno14Image[i,j,0:3] = np.asarray([0,0,0])

        #redDif13 = np.absolute(np.subtract(img2011[i,j,0],img2013[i,j,0]))
        #greDif13 = np.absolute(np.subtract(img2011[i,j,1],img2013[i,j,1]))
        #bluDif13 = np.absolute(np.subtract(img2011[i,j,2],img2013[i,j,2]))
        #if ((redDif13+greDif13+bluDif13)/3) <= (limit):
        #    if np.mean(img2011[i,j,0:3]) > (1-limit):
        #        count13 += 1
        #        sno13Image[i,j] = img2011[i,j,0:3]
        #else:
        #    sno13Image[i,j,0:3] = np.asarray([0,0,0])
        #    
        #redDif14 = np.absolute(np.subtract(img2011[i,j,0],img2014[i,j,0]))
        #greDif14 = np.absolute(np.subtract(img2011[i,j,1],img2014[i,j,1]))
        #bluDif14 = np.absolute(np.subtract(img2011[i,j,2],img2014[i,j,2]))
        #if ((redDif14+greDif14+bluDif14)/3) <= (limit):
        #    if np.mean(img2011[i,j,0:3]) > (1-limit):
        #        count14 += 1
        #        sno14Image[i,j] = img2011[i,j,0:3]
        #else:
        #    sno14Image[i,j,0:3] = np.asarray([0,0,0])
plt.imshow(sno11Image)		#Open window to show image (close to continue)
plt.show() 
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/snow11Image1.png',sno11Image)
  
plt.imshow(sno13Image)		#Open window to show image (close to continue)
plt.show() 
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/snow13Image1.png',sno13Image)

plt.imshow(sno14Image)		#Open window to show image (close to continue)
plt.show() 
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/snow14Image1.png',sno14Image)



print "SNOWY PIXELS (5% THRESHHOLD):\n2011\t2013\t2014\n"+str(count11)+"\t"+str(count13)+"\t"+str(count14)
#SNOWY PIXELS (5% THRESHHOLD):
#2011	2013	2014
#100243	30239	13524

print "SNOW AS DIFFERENCES:\n2011\t2013\t2014\n"+str(float(count11*100)/count11)+"\t"+str((count13*100)/float(count11))+"\t"+str((count14*100)/float(count11))
#SNOW AS DIFFERENCES:
#2011	2013	2014
#100.0	30.1656973554	13.4912163443

## part 5: korea

import matplotlib.pyplot as plt  
import numpy as np 
kor1981 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/korea1989.png')
kor2013 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/korea2013.png')

plt.imshow(kor1981)

height = kor1981.shape[0]
width = kor1981.shape[1]

limit = 0.2
korImage = np.zeros((height,width,3))
for i in range(height):
    for j in range(width): 
         ## only red channel
        redDif = np.absolute(np.subtract(kor1981[i,j,0],kor2013[i,j,0]))
        greDif = np.absolute(np.subtract(kor1981[i,j,1],kor2013[i,j,1]))
        if ((redDif+greDif)/2) > (limit) and kor1981[i,j,0] < limit:
            korImage[i,j,0:3] = np.asarray([1,0,0])
        else:
            korImage[i,j] = kor1981[i,j,0:3]

plt.imshow(korImage)		#Open window to show image (close to continue)
plt.show() 
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/korImage3.png',korImage)

## part 6: texas

import matplotlib.pyplot as plt  
import numpy as np 
tex2013 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/TX2013.png')
tex2014 = plt.imread('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/TX2014.png')

height = tex2013.shape[0]
width = tex2013.shape[1]

plt.imshow(tex2014)

texImage = np.zeros((height,width,3))
texImage2 = np.zeros((height,width,3))

green13 = 0 ## 99912
green14 = 0 ## 428066

## need to calculate the amount of green relative to the amount of all colors - green/greyscale?
for i in range(height):
    print "row",i
    for j in range(width): 
        greyscale14 = np.mean(tex2014[i,j,0:3])
        greyscale13 = np.mean(tex2013[i,j,0:3])
        #texImage[i,j,0:3] = np.array([greyscale,greyscale,greyscale])
        #greyGreen = tex2014[i,j,1]-greyscale
        #if greyGreen >= 0:
        #    texImage2[i,j,0:3] = np.array([0,1,0])
        #else:
        #    texImage[i,j,0:3] = np.array([greyscale,greyscale,greyscale])
        if tex2014[i,j,1] > tex2014[i,j,0] and tex2014[i,j,1] > tex2014[i,j,2]:
            texImage2[i,j] = np.array([0,tex2014[i,j,1],0])
            green14 += 1
        else:
            texImage2[i,j] = np.array([greyscale14,greyscale14,greyscale14])
        if tex2013[i,j,1] > tex2013[i,j,0] and tex2013[i,j,1] > tex2013[i,j,2]:
            texImage[i,j] = np.array([0,tex2013[i,j,1],0])
            green13 += 1
        else:
            texImage[i,j] = np.array([greyscale13,greyscale13,greyscale13])

plt.imshow(texImage2)
plt.imshow(texImage)

plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/texImage1.png',texImage)
plt.imsave('C:/Users/Kaiya/Documents/Columbia/Classes/Algo Bio/texImage2.png',texImage2)