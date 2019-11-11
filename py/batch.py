import os,glob,sys,time
sys.path+=["/usr/lib/gimp/2.0/python"]
from gimpfu import *

#https://www.e-learn.cn/content/wangluowenzhang/334970
#gimp -idf --batch-interpreter python-fu-eval -b "import sys;sys.path=['.']+sys.path;import batch;batch.run('./images')" -b "pdb.gimp_quit(1)"

def process(infile):
        print "Processing file %s " % infile
        image = pdb.file_jpeg_load(infile,infile)
        drawable = pdb.gimp_image_get_active_layer(image)

        print "File %s loaded OK" % infile
        pdb.plug_in_photocopy(image, drawable,8.,0.8,0.2,0.2)
        pdb.plug_in_cartoon(image, drawable, 7.,0.2)
        outfile=os.path.join('processed',os.path.basename(infile))
        outfile=os.path.join(os.path.dirname(infile),outfile)
        print "Saving to %s" % outfile
        pdb.file_jpeg_save(image, drawable, outfile, outfile, "0.5",0,1,0,"",0,1,0,0)
        print "Saved to %s" % outfile
        pdb.gimp_image_delete(image)


def run(directory):
        start=time.time()
        print "Running on directory \"%s\"" % directory
#   os.mkdir(os.path.join(directory,'processed'))
        for infile in glob.glob(os.path.join(directory, '*.jpg')):
                process(infile)
        end=time.time()
        print "Finished, total processing time: %.2f seconds" % (end-start)


if __name__ == "__main__":
        print "Running as __main__ with args: %s" % sys.argv
