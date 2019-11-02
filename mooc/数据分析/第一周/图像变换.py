from PIL import Image
import numpy as np

#原图像的数组表示
# a = np.array(Image.open('image.png'))
a = np.array(Image.open('image.png').convert('L'))

#打印原数组的size，type
print(a.shape,a.dtype)
print(a)

#新的数组
b = 255 - a

#再生成图像对象
im = Image.fromarray(b.astype('uint8'))

#二进制保存图像
im.save('image-black.png')