#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

def resize(resize_k):
    img_name = "/disk021/share/omura/20190531/441050001033/IMG_3341.JPG"
    img = Image.open(img_name)
    width, height = img.size

    x = int(width / resize_k)
    y = int(height / resize_k)

    image_resized = img.resize((x, y), Image.BICUBIC)
    image_resized.save('resized.JPG')

    print("resize complete")
    print("width:" + str(width) + "->" + str(x))
    print("height:" + str(height) + "->" + str(y))