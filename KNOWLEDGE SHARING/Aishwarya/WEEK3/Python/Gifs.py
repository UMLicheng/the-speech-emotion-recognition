#!/usr/bin/env python
# coding: utf-8

# In[7]:



# Reading an animated GIF file using Python Image Processing Library - Pillow

from PIL import Image

from PIL import GifImagePlugin
 
imageObject = Image.open("C:/Users/Dell/Downloads/DTWSpeech-master/sounds/AishCatSurprise1.gif")
for frame in range(0,imageObject.n_frames):

    imageObject.seek(frame)
    imageObject.show()
 


# In[ ]:




