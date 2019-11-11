import re
import requests
import json
import os,sys
# py2
sys.path+=["/usr/lib/gimp/2.0/python"]
from gimpfu import *
from gimpenums import *

U="https://hbimg.huabanimg.com/f11bef610be3f020ddc8dd4051298dbc4fa9ab82321bef-fsXJye_fw658"

#exec 'print "Hello World"'
#'builtin_function_or_method'
is_function=lambda o: lambda x : re.match(r'.*function.*',type(getattr(o,x)).__name__,re.I)

# a=range(10) (partition a <3) -> [[1,2][3..10]]
def partition(arr,f):
     a=[x for x in arr if f(x) ]
     b=[x for x in arr if not f(x) ]
     return (a,b)

def download(u=U):
    return requests.get(u)

def dir1(o,name="l"):
    a=[x for x in dir(o) if not re.match("__",x)]
 #   name=[k for k,v in locals().items() if v==o][0]
    (b0,c0)=partition(a,is_function(o))
    b=[ "{}.{}()".format(name,x) for  x in b0 ]
    c=[ "{}.{}".format(name,x) for x in c0 ]
    return b+c


def write_line(s,name="/tmp/ccc"):
    s1="\n".join(s)
    with open(name,"w") as f:
        f.write(s1)

def dir2(o,name="l"):
    s=dir1(o,name)
    write_line(s)


def new_name(N="/tmp/1.jpg"):
    path,name=os.path.split(i.filename)
    na,nb=name.split('.')
    N1=[path +"/" +na + "_"+x+"." +nb for x in ["a","b"]]
    return N1

def save_layer(i,l=0):
    path,name=os.path.split(i.filename)
    na,nb=name.split('.')
    n="{}/{}_{}.{}".format(path,na,l,nb)
    pdb.gimp_file_save(i, i.layers[l], n,n)

def save_select(i,filename):
    l=i.layers[0]
    pdb.gimp_edit_copy(l)
    newimage=pdb.gimp_edit_paste_as_new()
    drawable=newimage.layers[0]
    pdb.gimp_file_save(newimage, drawable, filename, filename)
    pdb.gimp_image_delete(newimage)

def select_half(i):
    pdb.gimp_selection_none(i)
    w,h=i.width,i.height
    pdb.gimp_rect_select(i,0,0,w/2,h,0,True,10.5)

def load(n="/tmp/1.jpg"):
    return p.gimp_file_load(n)

def split(i):
    select_half(i)
    N=i.filename
    f1,f2=new_name(N)
    save_select(i,f1)
    pdb.gimp_selection_invert(i)
    save_select(i,f2)
    pdb.gimp_selection_none(i)

def add_text(t="哈哈",font="迷你简瘦金书",size=2):
    l = pdb.gimp_text_layer_new(i, t, font, size, 1)
    i.insert_layer(l)
    return l

def set_text(l):
    p.gimp_text_layer_set_text(l,"呵呵")
    p.gimp_text_layer_set_font_size(l,2,1)
    p.gimp_text_layer_set_font(l,"迷你简瘦金书")
    p.gimp_layer_set_offsets(l, 0, 0)
    #l.resize(800,800)
    p.gimp_text_layer_resize(l,800,800)

def text_vectors(l):
    v=p.gimp_vectors_new_from_text_layer(i,l)
    p.gimp_vectors_stroke_close(v)
    #s=p.gimp_vectors_to_selection(v)

def flip(i):
    p.gimp_image_flip(i,1) #v
    p.gimp_image_flip(i,0) #x

def active_bg():
    l=i.layers[-1]
    p.gimp_image_set_active_layer(i, l)

def mask():
    active_layer = i.new_layer()
    active_layer.opacity = 10.0
    active_layer.fill(1)
    active_layer.name="ccc"
    p.gimp_edit_bucket_fill_full(active_layer,0,0,100,255,True,True,0,0,0)
    select_half(i)
    m=active_layer.create_mask(4)
    pdb.gimp_layer_add_mask(a, m)


def mask1(b):
    #a=i.layers[0]
    #b=a.copy()
    #i.insert_layer(b)
  #  b=i.active_layer
    i=b.image
    select_half(i)
    m=b.create_mask(4)
    pdb.gimp_layer_add_mask(b, m)
    pdb.gimp_selection_none(i)

def download_merge():
    i1= pdb.file_uri_load(u, u)
    #gimp.Display(i1)
    #l=i1.layers[0]
    z= pdb.gimp_edit_copy_visible(i1)
    i0=i.new_layer()
    floating_sel = pdb.gimp_edit_paste(i0, True)
    pdb.gimp_floating_sel_attach(floating_sel,i0)
    mask1(i0)





ii=gimp.image_list()
i=ii[0]
l=i.layers[0]

attr=lambda l:[x for x in dir(l) if not re.match("__",x)]
find1=lambda p: ",".join([x for x in dir1(l) if re.match('.*{}.*'.format(p), x)])
find=lambda p: ",".join(["i.{}()".format(x) for x in dir(i) if re.match('.*{}.*'.format(p), x)])


i.width
i.height

i.ID
i.name="cc"
i.filename="/tmp/cc"

i.crop
i.scale
i.resize
i.resize_to_layers

i.add_channel()
i.add_hguide()
i.add_layer()
i.add_vguide()


i.attach_new_parasite()
i.new_layer()
i.layers
i.add_layer

i.active_layer()

i.insert_layer(l.copy())

i.get_layer_by_tattoo()
i.lower_layer()
i.lower_layer_to_bottom()
i.merge_visible_layers()
i.pick_correlate_layer()

i.raise_layer()
i.raise_layer_to_top()
i.remove_layer()
i.resize_to_layers()

i.channels
i.active_channel
i.add_channel()
i.insert_channel()
i.get_channel_by_tattoo()
i.lower_channel()
i.raise_channel()
i.remove_channel()
i.unset_active_channel()

i.active_channel
i.active_drawable
i.active_vectors
i.add_channel
i.add_hguide
i.add_layer
i.add_vguide
i.attach_new_parasite
i.base_type
i.channels
i.clean_all
i.colormap

i.delete_guide
i.dirty
i.disable_undo
i.duplicate
i.enable_undo
i.find_next_guide
i.flatten
i.floating_sel_attached_to
i.floating_selection
i.free_shadow

i.get_channel_by_tattoo
i.get_component_active
i.get_component_visible
i.get_guide_orientation
i.get_guide_position
i.get_layer_by_tattoo

i.insert_channel
i.lower_channel
i.lower_layer(l)
i.lower_layer_to_bottom(l)
i.merge_down
i.merge_visible_layers(0)
i.new_layer()
i.parasite_attach
i.parasite_detach
i.parasite_find
i.parasite_list
i.pick_correlate_layer
i.raise_channel
i.raise_layer
i.raise_layer_to_top

i.remove_channel
i.remove_layer

i.resolution
i.selection
i.set_component_active
i.set_component_visible
i.tattoo_state
i.undo_freeze
i.undo_group_end
i.undo_group_start
i.undo_is_enabled
i.undo_thaw
i.unit
i.unset_active_channel
i.uri
i.vectors



l.ID
l.name
l.apply_mask
l.bpp
l.children
l.edit_mask
l.has_alpha
l.height
l.image

l.is_floating_sel
l.is_gray
l.is_grey
l.is_indexed
l.is_layer_mask
l.is_rgb

l.linked
l.lock_alpha
l.mask
l.mask_bounds
l.mode
l.name
l.offsets
l.opacity
l.parent
l.preserve_trans
l.show_mask
l.tattoo
l.type
l.type_with_alpha
l.visible
l.width


l.add_alpha()
l.add_mask()
l.attach_new_parasite()
l.copy()
l.create_mask()
l.fill()
l.flush()
l.free_shadow()
l.from_id()
l.get_pixel()
l.get_pixel_rgn()
l.get_tile()
l.get_tile2()
l.mask_intersect()
l.merge_shadow()
l.offset()
l.parasite_attach()
l.parasite_detach()
l.parasite_find()
l.parasite_list()
l.remove_mask()
l.resize()
l.resize_to_image_size()
l.scale()
l.set_offsets()
l.set_pixel()
l.transform_2d()
l.transform_2d_default()
l.transform_flip()
l.transform_flip_default()
l.transform_flip_simple()
l.transform_matrix()
l.transform_matrix_default()
l.transform_perspective()
l.transform_perspective_default()
l.transform_rotate()
l.transform_rotate_default()
l.transform_rotate_simple()
l.transform_scale()
l.transform_scale_default()
l.transform_shear()
l.transform_shear_default()
l.translate(100,100)
l.update()

#---------------detail----------------------------------------------------
l.edit_mask
l.is_layer_mask
l.mask
l.mask_bounds
l.show_mask

l.add_mask()
l.create_mask()
l.mask_intersect()
l.remove_mask()
l.apply_mask

l.transform_2d()
l.transform_2d_default()
l.transform_flip()
l.transform_flip_default()
l.transform_flip_simple()
l.transform_matrix()
l.transform_matrix_default()
l.transform_perspective()
l.transform_perspective_default()
l.transform_rotate()
l.transform_rotate_default()
l.transform_rotate_simple()
l.transform_scale()
l.transform_scale_default()
l.transform_shear()
l.transform_shear_default()
l.translate()
l.preserve_trans
