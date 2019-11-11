import os,sys
# py2
sys.path+=["/usr/lib/gimp/2.0/python"]
#gimp --no-interface --batch '(python_fu_hello_world RUN-NONINTERACTIVE "Hello" Sans 50 red)' -b '(gimp-quit 1)'
from gimpfu import *

def hello_world():
 gimp.message("Hello, GIMP world!\n")

register(
 "hello_world",
 'A simple Python-Fu "Hello, World" plug-in',
 'When run this plug-in prints "Hello, GIMP world!" in a dialog box.',
 "Tony Podlaski",
 "Tony Podlaski 2017. MIT License",
 "2017",
 "Hello World",
 "",
 [],
 [],
 hello_world,
 menu="/Filters/HelloWorld",
)

main()
