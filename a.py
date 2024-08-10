from PIL import Image

# 打开要压缩的图片
for i in range(1, 57):
    image = Image.open(f'./img/{i}.jpg')

    # 设置压缩质量（0-100），数值越低，压缩效果越明显
    quality = 50

    # 保存压缩后的图片，保留原分辨率
    image.save(f'./imgs/{i}.jpg', 'JPEG', quality=quality)
