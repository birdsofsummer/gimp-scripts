# GIMP gif 一次去n个水印

## 适用

  + 背景透明的gif
  + 水印区域固定
  + 水印边缘不复杂
  + 如果水印边缘复杂,考虑制作蒙版通道抠图
  + 如果水印位置随机,可以考虑删除水印颜色

## 其他方案

### imagemagick

```bash
# 14,35
# 232,282
a="xxx"

identify $a.gif
#查看图片信息,找出关键位置

# 取一帧测试
convert -size 298x298 canvas:none \( "$a.gif[0]" -crop 282x272+18+14  \) \
-delete 0 \
-insert 0 -gravity center -alpha on -background  transparent cc.gif

# 修改整个gif
convert -size 298x298 canvas:none \( $a.gif  -coalesce  -crop 282x272+18+14  \) \
-insert 0 -gravity center -alpha on -background  transparent cc1.gif
        
```
### ffmpeg

```bash

a="xxx"
#一次去一个
#[(1,1),(1+14,1+35)]
#[(232,282),(232+66,282+16)]


ffmpeg -i $a.gif -filter_complex "delogo=x=1:y=1:w=14:h=35:show=0" cc2.gif
ffmpeg -i cc2.gif -filter_complex "delogo=x=232:y=282:w=66:h=16:show=0" cc3.gif

```

### cv2
  + 拆帧
  + 去水印
  + 合成gif


## 思路

  + 打开一个gif文件,找好坐标,修改保存坐标信息
  + 遍历打开gif文件
  + 遍历每个水印区域
  + 选中一个水印区域
  + 遍历n个图层删除
  + 取消选中
  + 保存文件
  + 关闭


```python

g=gimp
p=pdb

p.file_gif_load
p.file_gif_load_thumb
p.file_gif_save

p.file_aa_save
p.file_bmp_save
p.file_bz2_save
p.file_cel_save
p.file_colorxhtml_save
p.file_csource_save
p.file_dicom_save
p.file_eps_save
p.file_fits_save
p.file_fli_save
p.file_gbr_save
p.file_gif_save
p.file_gih_save
p.file_gtm_save
p.file_gz_save
p.file_header_save
p.file_ico_save
p.file_jpeg_save
p.file_mng_save
p.file_openraster_save
p.file_pat_save
p.file_pbm_save
p.file_pcx_save
p.file_pdf_save
p.file_pdf_save_multi
p.file_pgm_save
p.file_pix_save
p.file_png_save
p.file_png_save2
p.file_png_save_defaults
p.file_pnm_save
p.file_ppm_save
p.file_ps_save
p.file_psd_save
p.file_raw_save
p.file_sgi_save
p.file_sunras_save
p.file_tga_save
p.file_tiff_save
p.file_tiff_save2
p.file_uri_save
p.file_xbm_save
p.file_xmc_save
p.file_xpm_save
p.file_xwd_save

p.gimp_file_save
p.gimp_file_save_thumbnail
p.gimp_register_save_handler
p.gimp_selection_save
p.gimp_xcf_save
p.python_fu_gradient_save_as_css



ii=g.image_list()
i=ii[0]
p.gimp_image_delete(i)

i.ID
i.__class__
i.__cmp__
i.__delattr__
i.__doc__
i.__format__
i.__getattribute__
i.__hash__
i.__init__
i.__new__
i.__reduce__
i.__reduce_ex__
i.__repr__
i.__setattr__
i.__sizeof__
i.__str__
i.__subclasshook__
i.active_channel
i.active_drawable
i.active_layer
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
i.crop
i.delete_guide
i.dirty
i.disable_undo
i.duplicate
i.enable_undo
i.filename
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
i.height
i.insert_channel
i.insert_layer
i.layers
i.lower_channel
i.lower_layer
i.lower_layer_to_bottom
i.merge_down
i.merge_visible_layers
i.name
i.new_layer
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
i.resize
i.resize_to_layers
i.resolution
i.scale
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
i.width




l.__add__
l.__class__
l.__contains__
l.__delattr__
l.__delitem__
l.__delslice__
l.__doc__
l.__eq__
l.__format__
l.__ge__
l.__getattribute__
l.__getitem__
l.__getslice__
l.__gt__
l.__hash__
l.__iadd__
l.__imul__
l.__init__
l.__iter__
l.__le__
l.__len__
l.__lt__
l.__mul__
l.__ne__
l.__new__
l.__reduce__
l.__reduce_ex__
l.__repr__
l.__reversed__
l.__rmul__
l.__setattr__
l.__setitem__
l.__setslice__
l.__sizeof__
l.__str__
l.__subclasshook__
l.append
l.count
l.extend
l.index
l.insert
l.pop
l.remove
l.reverse
l.sort


ll.ID
ll.__class__
ll.__cmp__
ll.__delattr__
ll.__doc__
ll.__format__
ll.__getattribute__
ll.__hash__
ll.__init__
ll.__new__
ll.__reduce__
ll.__reduce_ex__
ll.__repr__
ll.__setattr__
ll.__sizeof__
ll.__str__
ll.__subclasshook__
ll.add_alpha
ll.add_mask
ll.apply_mask
ll.attach_new_parasite
ll.bpp
ll.children
ll.copy
ll.create_mask
ll.edit_mask
ll.fill
ll.flush
ll.free_shadow
ll.from_id
ll.get_pixel
ll.get_pixel_rgn
ll.get_tile
ll.get_tile2
ll.has_alpha
ll.height
ll.image
ll.is_floating_sel
ll.is_gray
ll.is_grey
ll.is_indexed
ll.is_layer_mask
ll.is_rgb
ll.linked
ll.lock_alpha
ll.mask
ll.mask_bounds
ll.mask_intersect
ll.merge_shadow
ll.mode
ll.name
ll.offset
ll.offsets
ll.opacity
ll.parasite_attach
ll.parasite_detach
ll.parasite_find
ll.parasite_list
ll.parent
ll.preserve_trans
ll.remove_mask
ll.resize
ll.resize_to_image_size
ll.scale
ll.set_offsets
ll.set_pixel
ll.show_mask
ll.tattoo
ll.transform_2d
ll.transform_2d_default
ll.transform_flip
ll.transform_flip_default
ll.transform_flip_simple
ll.transform_matrix
ll.transform_matrix_default
ll.transform_perspective
ll.transform_perspective_default
ll.transform_rotate
ll.transform_rotate_default
ll.transform_rotate_simple
ll.transform_scale
ll.transform_scale_default
ll.transform_shear
ll.transform_shear_default
ll.translate
ll.type
ll.type_with_alpha
ll.update
ll.visible
ll.width


```
