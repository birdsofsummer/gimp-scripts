#https://blog.csdn.net/akof1314/article/details/42922051
#https://blog.csdn.net/mo3408/article/details/80671398?utm_source=blogxgwz7

convert -list font > fonts.txt
convert -list color >colors.txt

img1=name.gif
img2=watermark.png
img3=output.png


convert $img1 -background black -alpha remove $img1-black.jpg
convert $img1 -alpha extract  $img1-mask.png

convert -coalesce $img1 -gravity SouthEast -geometry +0+0 null: $img2 -layers composite -layers optimize $img3
convert 123/a-1.png  m.png  -compose  copyopacity -composite 1.gif
convert -delay 10 123/*.png -loop 0 animated.gif



a=9752
name=$a.gif
identify $name

convert $name -coalesce +append star.png

convert "$a.gif[0]"  -alpha extract  z-m.png
gimp z-m.png
# 反相 -> 水印涂黑 -> 保存
# 拆帧 -> 去水印 ->合成
md z
rm z/*


convert $name z/a.png
#convert  -coalesce $a -alpha on  -fuzz 20% -transparent red ccc.gif
find z -type f -exec convert {}  z-m.png -compose copyopacity -composite -alpha on  -fuzz 2% -transparent white {} \;
convert -delay 10 z/*.png -loop 0 $a-1.gif
ffplay $a-1.gif
gimp $a-1.gif
rm z/*


md out
md out1
md out2

for i in `magick -list compose` ;
do
    echo $i;
 #   echo convert z-m.png z/a-10.png   -compose $i z/a-10.png -geometry 295x294+0+0 -composite  out/$i.png ;
    convert z-m.png z/a-18.png   -compose $i  -geometry 295x294+0+0 -composite  out/$i.png ;
    convert z/a-18.png z-m.png   -compose $i  -geometry 295x294+0+0 -composite  out1/$i.png ;
    #convert z/a-10.png '(z-m.png -negate )' -compose $i z/a-10.png -geometry 295x294+0+0 -composite  out2/$i.png ;
    convert z/a-18.png z-m-n.png  -compose $i -geometry 295x294+0+0 -composite  out2/$i.png ;
done

# magick -list compose

# -compose Atop
# -compose Blend
# -compose Blur
# -compose Bumpmap
# -compose ChangeMask
# -compose Clear
# -compose ColorBurn
# -compose ColorDodge
# -compose Colorize
# -compose CopyAlpha
# -compose CopyBlack
# -compose CopyBlue
# -compose CopyCyan
# -compose CopyGreen
# -compose Copy
# -compose CopyMagenta
# -compose CopyRed
# -compose CopyYellow
# -compose Darken
# -compose DarkenIntensity
# -compose DivideDst
# -compose DivideSrc
# -compose Dst
# -compose Difference
# -compose Displace
# -compose Dissolve
# -compose Distort
# -compose DstAtop
# -compose DstIn
# -compose DstOut
# -compose DstOver
# -compose Exclusion
# -compose HardLight
# -compose HardMix
# -compose Hue
# -compose In
# -compose Intensity
# -compose Lighten
# -compose LightenIntensity
# -compose LinearBurn
# -compose LinearDodge
# -compose LinearLight
# -compose Luminize
# -compose Mathematics
# -compose MinusDst
# -compose MinusSrc
# -compose Modulate
# -compose ModulusAdd
# -compose ModulusSubtract
# -compose Multiply
# -compose None
# -compose Out
# -compose Overlay
# -compose Over
# -compose PegtopLight
# -compose PinLight
# -compose Plus
# -compose Replace
# -compose Saturate
# -compose Screen
# -compose SoftLight
# -compose Src
# -compose SrcAtop
# -compose SrcIn
# -compose SrcOut
# -compose SrcOver
# -compose Stereo
# -compose VividLight
# -compose Xor

convert rose:  -fx "(1/(1+exp(10*(.5-u)))-0.0066928509)*1.0092503" sigmoidal.png
convert rose:  -sigmoidal-contrast 10,50% logo_sigmoidal.png
convert rose:  -normalize  normalize_gray.jpg

 -contrast-stretch 15%
 -colors 64
 -monochrome
 -threshold -1
 -threshold 25%
 -threshold 50%
 -threshold 75%
 -threshold 100%
 -background lightblue -fill blue -font Candice -pointsize 72 label:ccc
 -background lightblue -fill blue -font 迷你简瘦金书 -pointsize 72 label:@ccc.txt
 -background lightblue -fill blue -font Times-Roman -pointsize 36 -size 320x caption:"This is a very long caption line."


convert rose: -font 迷你简瘦金书 -fill white -undercolor '#00000080' -gravity South -annotate 0x0+0+10 @ccc.txt anno.png
convert -size 100x100 xc:blue canvas_blue.gif
convert -size 100x100 xc:rgb(0,0,255) canvas_blue.gif
convert -size 50x50 xc:red xc:blue +append red+blue.gif
convert -size 50x50 xc:red xc:blue -append red-blue.gif
convert -size 100x100 gradient: gradient.jpg
convert -size 100x100 gradient:blue gradient_blue.jpg
convert -size 100x100 gradient:red-blue gradient_red_to_blue.jpg
convert -size 100x60 xc:skyblue -fill white -stroke black -draw "rectangle 20,10 80,50" draw_rect.gif
convert -size 100x60 xc:skyblue -fill white -stroke black -draw "ellipse 50,30 40,20 0,360" draw_ellipse.gif
convert -size 100x60 xc:skyblue -fill white -stroke black -draw "polyline 40,10 20,50 90,10 70,40" draw_polyline.gif
convert -size 100x60 xc:skyblue -fill white -stroke black -draw "roundrectangle 20,10 80,50 20,15" draw_rrect.gif
convert -size 100x60 xc:skyblue -fill white -stroke black -draw "ellipse 50,30 40,20 45,270" draw_ellipse_partial.gif
convert -size 100x60 xc:skyblue -gravity center -draw "image over 0,0 0,0 'terminal.gif'" draw_image.gif
convert -size 100x60 xc:skyblue -fill white -stroke black -font Candice -pointsize 40 -gravity center -draw "text 0,0 'Hello'" draw_text.gif



convert -size 320x90 canvas:none -stroke snow4 -size 1x90 -tile gradient:white-snow4 \
  -draw 'roundrectangle 16, 5, 304, 85 20,40' +tile -fill snow \
  -draw 'roundrectangle 264, 5, 304, 85  20,40' -tile gradient:chartreuse-green \
  -draw 'roundrectangle 16,  5, 180, 85  20,40' -tile gradient:chartreuse1-chartreuse3 \
  -draw 'roundrectangle 140, 5, 180, 85  20,40' +tile -fill none \
  -draw 'roundrectangle 264, 5, 304, 85 20,40' -strokewidth 2 \
  -draw 'roundrectangle 16, 5, 304, 85 20,40' \( +clone -background snow4 \
  -shadow 80x3+3+3 \) +swap -background none -layers merge \( +size -font Helvetica \
  -pointsize 90 -strokewidth 1 -fill red label:'50 %' -trim +repage \( +clone \
  -background firebrick3 -shadow 80x3+3+3 \) +swap -background none -layers merge \) \
  -insert 0 -gravity center -append -background white -gravity center -extent 320x200 \
  cylinder_shaded.png



# 14,35
# 232,282
convert -size 298x298 canvas:none \( "$a.gif[0]" -crop 282x272+18+14  \) \
-delete 0 \
-insert 0 -gravity center -alpha on -background  transparent cc.gif

convert -size 298x298 canvas:none \( $a.gif  -coalesce  -crop 282x272+18+14  \) \
-insert 0 -gravity center -alpha on -background  transparent cc1.gif

ffplay cc1.gif



# +repage

convert 2pages.png -crop 50%x100% +repage newpage.png
convert page*.png -crop 50%x100% +repage newpaged.png
convert page100.png -trim +repage trim.png
convert r90.png -rotate -90 page200.png
mogrify -path newdir -rotate -90 *.png
convert r2pages.png -rotate -90 -crop 50%x100% +repage newpage.png
convert page200.png -background blue -rotate 10 r10.png

# 斜
convert page100.png -background white -deskew 40% deskewed.png
mogrify -path newdir -background white -deskew 40% *.png
convert page.png -noop noop.png
convert page.png -negate negated.png

convert page.png -level 25% p15.png
convert page.png -level 0,85% p0-85.png
convert page.png +level 25% p+25.png

convert page.png -level 0,100%,2.0 p0-100-2.0.png
convert page.png -level 0,100%,0.5 p0-100-2.0.png
convert page.png -level 0,85%,0.5 p0-100-2.0.png


ffmpeg -i $a.gif -filter_complex "delogo=x=1:y=1:w=14:h=35:show=0" cc2.gif
ffmpeg -i cc2.gif -filter_complex "delogo=x=232:y=282:w=66:h=16:show=0" cc3.gif

ffplay cc3.gif

