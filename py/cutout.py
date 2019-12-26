# py2
sys.path+=["/usr/lib/gimp/2.0/python"]

from gimpfu import *
from gimpenums import *

import re
import time
import requests
import json
import os,sys

g=gimp
p=pdb

def md(path):
    if not os.path.exists(path):
          os.makedirs(path)

def cut(i,area=[]):
    l=i.layers
    for dd in area:
         p.gimp_selection_none(i)
         p.gimp_image_select_rectangle(*dd)
         [p.gimp_edit_clear(z) for z in l]
         #p.gimp_image_set_active_layer(i, ll)
         #p.gimp_edit_clear(ll)

def save(i,filename="/tmp/ccc/ccc.gif"):
     image=i
     drawable=i.active_drawable
     raw_filename=filename
     interlace=0
     loop=0
     default_delay=120
     default_dispose=0
     pdb.file_gif_save(image, drawable, filename, raw_filename, interlace, loop, default_delay, default_dispose)


def get_area(i):
     POINTS=[(30,34),(231,281)]
     w,h=i.width,i.height
     x1,y1=POINTS[0]
     x2,y2=POINTS[1]
     dx2=w-x2
     dy2=h-y2

     d1=(i,0,0,0,x1,y1)
     d2=(i,0,x2,y2,dx2,dy2)
     area=[d1,d2]
     return area


def  cutout(file_name="/tmp/gif/1.gif",path1="/tmp/ccc/"):
     md(path1)
     path,name=os.path.split(file_name)
     file_name1=os.path.join(path1,name)
     i = pdb.file_gif_load(file_name, file_name)
     area=get_area(i)
     cut(i,area)
     save(i,file_name1)
     p.gimp_image_delete(i)
    # ii=g.image_list()
    # i=ii[0]
    # p.gimp_image_delete(i)
     #gimp.pdb.gimp_image_delete(i)
     #d=gimp.Display(i)
     #gimp.pdb.gimp_display_delete(d)
     #g.delete(i)
     #g.exit()
     #g.quit()


def start():
    t="/tmp/gif/"
    z=[x for x in os.walk(t)]
    files=z[0][2]
    i=0
    for x in files:
        i=i+1
        n=t+x
        print i,n
        cutout(n)
        time.sleep(1)

start()



