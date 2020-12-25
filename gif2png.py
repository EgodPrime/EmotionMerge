# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:01:27 2020

@author: egod
"""
import os
from PIL import Image, ImageSequence


def parseGIF(gifname):
    # 将gif解析为图片
    # 读取GIF
    im = Image.open(gifname)
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(im)
    # 返回第一帧
    return iter[0]
    
    
def walkDirParse(dirpath):
    # 存储位置
    data_dir = dirpath.split('/')[0]+'/png/'
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    for root,dirs,files in os.walk(dirpath):
        it = 1
        
        for file in files:
            img = parseGIF(os.path.join(dirpath,file))
            img.save(data_dir+str(it)+'.png')
            it += 1



if __name__ == "__main__":
    walkDirParse('data/gif')
    