# import PIL
#功能1  图像归档  ：对图像进行批处理、生成图像预览、图像格式转换
#功能2  图像处理  ：图像基本处理、像素处理、颜色处理

#PIL中有21个模块，这里主要介绍3个

#  -------------1>>Image类
from PIL import Image

# ----------基础-----------------
#图像读取  open()
# im = Image.open('sdq.jpg')

#Image对象的常用属性
# print(im.format,im.size,im.mode)
#mode -- 图像的色彩模式
#L -- 灰度图像 ；RGB -- 真彩色图像 ； CMYK -- 出版图像
#CMYK -- (青，品红，黄，定位套板色（黑）)  印刷时使用此种色彩模式

#读取序列类图像文件 -- GIF FLI FLC TIFF  -->>即动态图像？？？
#seek（frame） --  跳转并返回图像的指定帧  tell() -- 返回当前帧的序号

#----------------------------------

#-----------动态图像---------------
#打开图像默认为第一帧
# im = Image.open('hhh.gif')
# try:
# #保存第一帧图像
#     im.save('hhh/picframe{:02d}.png'.format(im.tell()))
#     while True:
#         im.seek(im.tell() + 1)
#         im.save('hhh/picframe{:02d}.png'.format(im.tell()))
# except:
#     print('处理结束')

#-------------缩略图,转换格式----------
# im = Image.open('sdq.jpg')
# im.thumbnail((300,300))
# im.save('sdq/little_sdq.png')

#-------------图像缩放，旋转-------------生成副本
im = Image.open('serach.icon.png')
# im1 = im.rotate(180)
im2 = im.resize((15,15))
# im1.save('sdq/rotate_sdq.jpg')
im2.save('sdq/resize_serach.png')

#---------------------图像像素、通道处理-----------
#通道处理 split() -- 提取图像的每个颜色通道，返回图像副本
#        merge(mode,bands) -- 合并通道，mode-色彩模式，bands-新的色彩通道

# im = Image.open('sdq.jpg')
# r,g,b, = im.split()
# om = Image.merge('RGB',(g,b,r))
# om.save('sdq/change_rgb_sdq.jpg')

#对每个像素点进行处理，需要通过函数实现，采用point()、lambda 函数
#point(func) -- 根据func函数对每个元素进行运算，返回图像副本
# im = Image.open('nc.jpeg')
# r,g,b = im.split()
# newg = g.point(lambda i:i*0.9)  # 将G通道颜色变为原来的0.9倍
# newb = b.point(lambda i:i<100)  # 选择G通道值低于100的像素点
# om = Image.merge(im.mode , (r,newg,newb))
# om.save('handle_point_nc.jpeg')   #效果：去掉光线 ????

#-------------------2>>ImageFilter类-----过滤图像
#使用Image.filter()方法调用Imagefilter的方法
# from PIL import ImageFilter
# im = Image.open('nc.jpeg')
# om = im.filter(ImageFilter.CONTOUR)
# om.save('nc/imagefilter_nc.jpeg')  #效果：轮廓处理，更加抽象

#-------------------3>>ImageEnhance类--------加强图像
#对比度 -- Contrast(im)  -->>  enhance(times)
# from PIL import ImageEnhance
# im = Image.open('nc.jpeg')
# om = ImageEnhance.Contrast(im)
# om.enhance(20).save('nc/imageEnhance_nc.jpeg')