# python照片墙设计
### 代码规划：
+ 将爬虫爬取的图片进行处理，减小尺寸
+ 将处理好的图片进行照片墙设计
### 图片处理ImageSolve.py:批量处理
+ 导入库：PIL:图像处理；glob
```
from PIL import Image
import os.path
import glob
```
+ 定义ReSize函数：
```
#由于爬虫获取的照片尺寸太大，我们更改爬虫获取的照片尺寸大小
def Resize(file, outdir, width, height):
    imgFile = Image.open(file)
    try:
        newImage = imgFile.resize((width, height), Image.BILINEAR)    #更改尺寸
        newImage.save(os.path.join(outdir, os.path.basename(file)))     #输出保存图片
    except Exception as e:
        print(e)
```
+ 处理后照片的存储
```
for file in glob.glob("res\\*.jpg"):  # 图片所在的目录
    Resize(file, "new", 100, 100)  # 新图片存放的目录
```
### 照片墙展示
+ 导入库
