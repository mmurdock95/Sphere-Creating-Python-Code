import cast
from data import *
import sys
from ray_caster import *
import time

def sphere_list():
    try:
        fh=open(sys.argv[1], 'r')
    except:
        print 'file does not exist'
        exit()
    newfh=fh.read()
    spherelist=[]
    sphereline=0
    print "loading..."

    #seperating by lines
    for i in newfh.split('\n'):
        sphereline+= 1
        #checking if each line is 11 arguements
        if len(i.split())==11:
            list1=[]
            list1.append(i.split())
            #seperating by colloumns 
            for row in list1:
                color= Color(float(row[4]), float(row[5]), float(row[6]))
                finish= Finish(float(row[7]), float(row[8]), float(row[9]), float(row[10]))
                sphere= Sphere(Point(float(row[0]), float(row[1]),
                                     float(row[2])), float(row[3]), color, finish)
                spherelist.append(sphere)
        else:
            print "skipping sphere on line", sphereline
    return spherelist

def output_spheres():
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
    sphere_list()
    print time.time()-t1
