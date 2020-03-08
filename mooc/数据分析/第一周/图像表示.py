from PIL import  Image
import numpy as np
im  = np.array(Image.open('image.png'))
print(im.shape,im.dtype)

