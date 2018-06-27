# 操作图像
from PIL import Image

# 打开一个jpg图像
im = Image.open('thumbnial.jpg')
# 获取图像尺寸
w, h = im.size
print('Orinal image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnial.jpg', 'jpeg')