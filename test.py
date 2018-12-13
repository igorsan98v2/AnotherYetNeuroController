from PIL import Image
import numpy as np
import os
import time
current_milli_time = lambda: int(round(time.time() * 1000))


image = Image.open("pic0.bmp")
print(image)
width,height = image.size
print("height %d" %height)
#print(image.__array_interface__['data'])
  

imgArr=list(image.__array_interface__['data'])
#otherArr= np.ndarray(imgArr).rashape(shape=(188*3,205))#а что если считаь количество одинаковых цветов с соседом слева
print("len arr %d,pix size: %d" % (len(imgArr)/(height*3),width))

#первые 20 пикселей

       
#print("progress:%d %.2f%%" %(progress, (progress/205.0)*100.0) )

npArr= np.reshape(imgArr,(height,width,3))
print((npArr[0][0]==[0,0,0]))

progress=0
for i in range(height):
   if(npArr[i][9][0]==228):
       progress=i
       break

print("progress:%.2f%%" % ((height-progress)/height)*100)
"""for i in range(width*3):
   print(imgArr[i],end=" ")
   if((i+1)%3==0 and i>0):
       print(end="|")"""
