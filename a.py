from PIL import Image

# 打开要翻转的图片
for i in range(1, 57):
    path = f'./img/{i}.jpg'
    image = Image.open(path)

    # 设置压缩质量（0-100），数值越低，压缩效果越明显
    quality = 30

    # 保存压缩后的图片，保留原分辨率
    image.save(path, 'JPEG', quality=quality)
# path = './img/55.jpg'
# image = Image.open(path)

# # 将图像顺时针旋转90度
# rotated_image = image.rotate(-90, expand=True)

# # 保存翻转后的图片
# rotated_image.save(path)
