# py2
sys.path+=["/usr/lib/gimp/2.0/python"]

from gimpfu import *
from gimpenums import *

import re
import time
import requests
import json
import os,sys
import time

SCALE = 1000
FONT = "Sans 24"
zh_CN_FONT = "文鼎PL中楷Uni 24"
FONT_NUMBER = "Sans 24"
COLOR_CROSS     = (0, 0, 0, 0.2)
COLOR_HIGHLIGHT = (0, 0, 1, 1.0)
COLOR_CHAR      = (0, 0, 0, 0.2)
COLOR_NUMBER    = (0, 0, 1.0, 1.0)
CANVAS_NORMAL   = 0
CANVAS_EDITING  = 1

g=gimp
p=pdb
ii=g.image_list()
i=ii[0]
l=i.layers

ac=i.active_channel
ad=i.active_drawable
al=i.active_layer
av=i.active_vectors
#av=pdb.gimp_image_get_active_vectors(i)
ps= p.gimp_path_list(i)
#(1, ('ccc',))
pname=p.gimp_path_get_current(i)
#'ccc'
p.gimp_image_get_vectors(i)
#(1, (5,))
zidian=[]




def get_dict(n):
    with open(n) as f:
        return json.loads(f.read())

def find(w="川"):
    f=lambda x:x['utf8'][0].encode('utf-8')==w
    return filter(f,zidian)

def line(ss=[]):
    hpt=[1.0,2.0]
    pt=[2.0,1.0,2.0]
    get_pt=lambda x: hpt if x else pt
    t=0
    for sss in ss:
       for b in get_pt(t== 0):
            x=float(sss['x'])
            y=float(sss['y'])
            point=(x,y,b)
            #print(len(points),point)
            yield point
       t+=1

def pline(s):
    for ss in s:
        points_pairs=[]
        for x in line(ss):
            points_pairs+=x
        yield(points_pairs)

def draw_line(t,s):
    z=0
    for x in pline(s):
        z+=1
        print z,x
        p.gimp_path_set_points(i, "{}_{}".format(t,z), 1, len(x), x)
        #p.gimp_edit_stroke_vectors(ad, i.active_vectors) #描边


def path2points(i):
    _,ps=p.gimp_path_list(i)
    for n in ps:
        yield (n,pdb.gimp_path_get_points(i, n))

def stroke1():
    num_vectors, vector_ids = pdb.gimp_image_get_vectors(i)
    #(3, (18, 17, 16))
    for vi in vector_ids:
        pass

def stroke(i):
    #(3, ('fff_3', 'fff_2', 'fff_1'))
    _,ps=p.gimp_path_list(i)
    for n in ps:
        vv=p.gimp_image_get_vectors_by_name(i, n)
        p.gimp_edit_stroke_vectors(ad, vv) #描边


def slow_stroke(i):
    #(3, ('fff_3', 'fff_2', 'fff_1'))
    _,ps=p.gimp_path_list(i)
    for n in ps:
        vv=p.gimp_image_get_vectors_by_name(i, n)
        p.gimp_edit_stroke_vectors(ad, vv) #描边
        time.sleep(1)

def del_path(i):
    #(3, ('fff_3', 'fff_2', 'fff_1'))
    _,ps=p.gimp_path_list(i)
    for n in ps:
        pdb.gimp_path_delete(i, n)
        #p.gimp_image_remove_vectors(i,n)


def add_text(t="哈哈",font="迷你简瘦金书",size=2):
    l = pdb.gimp_text_layer_new(i, t, font, size, 1)
    c=pdb.gimp_text_layer_get_color(l)
    i.insert_layer(l)
    return l


def text2path(l):
    v = pdb.gimp_vectors_new_from_text_layer(i, l)
    pdb.gimp_image_add_vectors(i, v, 0)
    #p.gimp_edit_stroke_vectors(ad, v)
    #p.gimp_edit_stroke_vectors(i.layers[1], v)
    return v

def clean_text_l(i):
    l=i.layers
    tl=[x for x in l if p.gimp_drawable_is_text_layer(x)==1]
    map(lambda x:pdb.gimp_image_remove_layer(i,x ),tl)
    #map(p.gimp_item_delete,tl)
    #map(p.gimp_layer_delete,tl)
    #[p.gimp_item_delete(x) for x in l[:-2]]

def active_top(i):
    l=i.layers[0]
    pdb.gimp_image_set_active_layer(i,l)

def init_zidian():
    n=os.getenv('bihua_zidian') # xxx.json
    zidian=get_dict(n)
    print len(zidian)
    return zidian

def write(n="龙"):
    active_top(i)
    zi=find(n)[0]
    s=zi['strokes']
    pdb.gimp_edit_clear(ad)
    p.gimp_selection_none(i)
    del_path(i)
    draw_line(n,s)
    stroke(i)
    l0=pdb.gimp_image_get_active_layer(i)
    pdb.gimp_layer_set_opacity(l0, 40)
    #stroke(i)
    #p.gimp_image_delete(i)
    clean_text_l(i)
    c1="#dddeee"
    c2="#f6e73d"
    pdb.gimp_context_set_foreground(c2)
    pdb.gimp_context_set_background(c1)
    print pdb.gimp_context_get_foreground()
    print pdb.gimp_context_get_background()
    cf=pdb.gimp_context_get_font()
    print cf
    fn,fs=pdb.gimp_fonts_get_list("楷")
    font="迷你简瘦金书"
    l=add_text(n,fs[0],size=14)
    pdb.gimp_layer_set_opacity(l, 20)
    pdb.gimp_image_lower_item(i, l)
    active_top(i)
    #save
    #file_name="/tmp/{}.png".format(n)
    #l1=pdb.gimp_image_merge_down(i,i.layers[0],0)
    #l2= pdb.gimp_image_merge_visible_layers(i,0)
    #pdb.gimp_file_save(i, l2, file_name,file_name)


def main():
    init_zidian()
    write()



























'''


#gimpcolor.RGB(0.964706, 0.904887, 0.238339, 1.0)
#gimpcolor.RGB(0.0, 0.0, 0.0, 1.0)
#p.gimp-image-get-active-vectors(i)
p.gimp_edit_stroke_vectors(ad, i.active_vectors) #描边


p.gimp_path_delete()
p.gimp_path_get_current()
p.gimp_path_get_locked()
p.gimp_path_get_point_at_dist()
p.gimp_path_get_points()
p.gimp_path_get_tattoo()
p.gimp_path_import()
p.gimp_path_set_current()
p.gimp_path_set_locked()
p.gimp_path_set_points()
p.gimp_path_set_tattoo()
p.gimp_path_stroke_current()
p.gimp_path_to_selection()
p.plug_in_sel2path()
p.plug_in_sel2path_advanced()
p.gimp_get_path_by_tattoo()
p.gimp_help_concepts_paths()



#p.gimp_image_set_active_layer(i, ll)

p.gimp_image_delete(i)
s=zi["strokes"]



av.ID
av.__class__
av.__cmp__
av.__delattr__
av.__doc__
av.__format__
av.__getattribute__
av.__hash__
av.__init__
av.__new__
av.__reduce__
av.__reduce_ex__
av.__repr__
av.__setattr__
av.__sizeof__
av.__str__
av.__subclasshook__
av.children
av.from_id
av.image
av.linked
av.name
av.parasite_attach
av.parasite_detach
av.parasite_find
av.parasite_list
av.parent
av.remove_stroke
av.strokes #[]
av.tattoo #5
av.visible #False
av.to_selection()
p.gimp_selection_none(i)


pdb.gimp_path_set_points(image, name, ptype, num_path_points, points_pairs)
贝塞尔曲线
1.0 = BEZIER_ANCHOR,
2.0 = BEZIER_CONTROL,
3.0= BEZIER_MOVE

# [(int(sss['x']),int(sss['y'])) for sss in ss for ss in s]
dd  = pdb.gimp_path_get_points(i, 'ccc')
path_type, path_closed, num_path_point_details, points_pairs

(1, 0, 33,
(304.0, 212.0, 1.0,
 304.0, 212.0, 2.0,

 308.0, 432.0, 2.0,
 308.0, 432.0, 1.0,
 308.0, 432.0, 2.0,

 256.0, 628.0, 2.0,
 256.0, 628.0, 1.0,
 256.0, 628.0, 2.0,

 216.0, 756.0, 2.0,
 216.0, 756.0, 1.0,
 216.0, 756.0, 2.0
 )
)
ACC ACC ACC ACC

'''

