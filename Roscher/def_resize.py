#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

def resize(image_name, resize_k):
    image = Image.open(image_name)
    width, height = image.size

    x = int(width / resize_k)
    y = int(height / resize_k)
    #x = 320
    #y = 240

    image_resized = image.resize((x, y), Image.BICUBIC)
    image_resized.save('resized.JPG')

    print("resize complete")
    print("width:" + str(width) + "->" + str(x))
    print("height:" + str(height) + "->" + str(y))