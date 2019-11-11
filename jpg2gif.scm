;(find-name "/tmp/1.jpg")
;("/tmp/1.jpg" "/tmp/1" "/tmp/1.jpg" "/tmp/1.gif")
(
 define (find-name filename)
  (let*(
    (picname (strbreakup filename ".")) 
    (picname (unbreakupstr (butlast picname) "."))
    (jpgname (string-append picname ".jpg"))
    (gifname (string-append picname ".gif"))
    )
    (list filename picname jpgname gifname)
    )
)

(define (convert filename picname jpgname gifname)
  (let*(
        (image (car (gimp-file-load 1 filename filename)))
        (drawable (car (gimp-image-flatten image)))
  )
  (file-jpeg-save 1 image drawable jpgname jpgname 0.85 0 1 1 "No comment!" 2 1 0 0)
    (gimp-image-convert-indexed image FS-DITHER MAKE-PALETTE 255 FALSE FALSE "")
    (gimp-file-save 1 image drawable gifname gifname)
    (gimp-image-delete image)
  )
)

(define (jpg2gif filename)
  (   let*( (names (find-name filename)))
      (apply convert (find-name filename))
  )
)

;(jpg2gif "/tmp/1.jpg")
;gimp -i -b '(jpg2gif "/tmp/1.jpg")' '(gimp-quit 0)'



(script-fu-register "script-fu-basic1-logo"
  _"_Basic I..."
  _"Create a plain text logo with a gradient effect, a drop shadow, and a background"
  "Spencer Kimball"
  "Spencer Kimball"
  "1996"
  ""
  SF-STRING     _"Text"               "GIMP"
  SF-ADJUSTMENT _"Font size (pixels)" '(100 2 1000 1 10 0 1)
  SF-FONT       _"Font"               "Dragonwick"
  SF-COLOR      _"Background color"   "white"
  SF-COLOR      _"Text color"         '(6 6 206)
)
(script-fu-menu-register "script-fu-basic1-logo" "<Image>/File/Create/Logos")
