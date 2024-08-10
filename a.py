from PIL import Image

# 打开要翻转的图片
path = './img/55.jpg'
image = Image.open(path)

# 将图像顺时针旋转90度
rotated_image = image.rotate(-90, expand=True)

# 保存翻转后的图片
rotated_image.save(path)
