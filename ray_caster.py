import sys
from cast import *
from commandline import *
from data import *
import time
#from __future__ import print_function

def command_line():
    argv=sys.argv

    #checking to make sure their is a .txt file included
    if len(argv)<2:
        print "error, argv length is less than 2"
        print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
        exit()

    #original points
    eye=Point(0.0, 0.0, -14.0)
    min_x=-10.0
    max_x=10.0
    min_y=-7.5
    max_y=7.5
    width=1024
    height=768
    light= Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
    ambient= Color(1.0, 1.0, 1.0)
    spherelist=sphere_list()
    
    for flags in xrange(len(argv)):
        #if user inputs flags
        if str(argv[flags])== '-eye':
            try:
                eye=Point(float(argv[flags+1]), float(argv[flags+2]), float(argv[flags+3]))
            except:
                print "invalid eye argument(s)"
        if str(argv[flags])== '-view':
            try:
                min_x=float(argv[flags+1])
                max_x=float(argv[flags+2])
                min_y=float(argv[flags+3])
                max_y=float(argv[flags+4])
                width=int(argv[flags+5])
                height=int(argv[flags+6])
            except:
                print "invalid view arguent(s)"
                min_x=-10.0
                max_x=10.0
                min_y=-7.5
                max_y=7.5
                width=1024
                height=768
        if str(argv[flags])== '-light':
            try:
                light=Light(Point(float(argv[flags+1]), float(argv[flags+2]),
                                  float(argv[flags+3])),
                            Color(float(argv[flags+4]), float(argv[flags+5]),
                                  float(argv[flags+6])))
            except:
                print "invalid light arguement(s)"
        if str(argv[flags])== '-ambient':
            try:
                ambient= Color(float(argv[flags+1]), float(argv[flags+2]),
                               float(argv[flags+3]))
            except:
                print "invalid ambient argument(s)"

    #witing color value for multiple spheres
    gh=open('image.ppm', 'w')
    gh.write("P3\n")
    gh.write("1024 768\n")
    gh.write("255\n")

    #going through the new list of lits from cast_all_rays
    for row in cast_all_rays(min_x, max_x, min_y, max_y, width,
                             height, eye, spherelist, ambient, light):
        for  i in row:
            gh.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

                
if __name__== "__main__":
    t1=time.time()
    command_line()
    print time.time()-t1
