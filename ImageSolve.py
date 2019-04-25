from PIL import Image
import os.path
import glob

#由于爬虫获取的照片尺寸太大，我们更改爬虫获取的照片尺寸大小
def Resize(file, outdir, width, height):
    imgFile = Image.open(file)
    try:
        newImage = imgFile.resize((width, height), Image.BILINEAR)    #更改尺寸
        newImage.save(os.path.join(outdir, os.path.basename(file)))     #输出保存图片
    except Exception as e:
        print(e)


for file in glob.glob("res\\*.jpg"):  # 图片所在的目录
    Resize(file, "new", 60, 60)  # 新图片存放的目录
