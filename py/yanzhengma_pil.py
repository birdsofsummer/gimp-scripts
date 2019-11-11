#py2
# apt-get install python-imaging
#https://www.liaoxuefeng.com/wiki/897692888725344/966759628285152
#http://effbot.org/imagingbook/

import Image, ImageDraw, ImageFont, ImageFilter
import random

FONT='/usr/share/fonts/简瘦金书.ttf'
repeat=lambda f,n: lambda:[f(x) for x in range(n)]
repeat1=lambda f,n: lambda:tuple([f(x) for x in range(n)])
rndChar=lambda  : chr(random.randint(65, 90))
rnd1=lambda x: random.randint (64, 127)
rnd2=lambda x: random.randint (32, 127)
rndColor=repeat1(rnd1,3)
rndColor2=repeat1(rnd2,3)

def yanzhengma(output='code.jpg',height = 60,n=6):
    width=n*40
    size=36
    font = ImageFont.truetype(FONT, size)
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    """
    看不清
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    """
    for t in range(n):
        draw.text((size * t , 10), rndChar(), font=font, fill=rndColor2())
    #image = image.filter(ImageFilter.BLUR)
    image.save(output, 'jpeg');
    return image

def save(f):
    def f1(file_name='./1.jpg',output="1_t.jpg"):
        i = Image.open(file_name)
        f(i)
        i.save(output, 'jpeg')
    return f1

@save
def thumb(i):
    w, h = i.size
    i.thumbnail((w//2, h//2))

#thumb("1.jpg","11.jpg")
