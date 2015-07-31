from data import *
import unittest
import vector_math
from collisions import *
from cast import *

class TestData(unittest.TestCase):
    def test_finish_sphere(self):
        myambient= Finish(0.2, )
        myambientlight= Color(1.0, 1.0, 1.0)
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
        w= Color(1.0, 1.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 1.0, r, myambient)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g, myambient)),
                      (Sphere(Point(3.0, 3.0, 3.0), 1.0, b, myambient))]
	self.assertEqual(cast_ray(myray, myspherelist, myambientlight),
                         Color(0.0, 0.2, 0.0))

    def test_finish_sphere2(self):
        myambient= Finish(0.4)
        myambientlight= Color(1.0, 1.0, 1.0)
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
        w= Color(1.0, 1.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 5.0, r, myambient)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g, myambient)),
                      (Sphere(Point(3.0, 3.0, 3.0), 1.0, b, myambient))]
	self.assertEqual(cast_ray(myray, myspherelist, myambientlight),
                         Color(0.4, 0.0, 0.0))

    def test_finish_sphere3(self):
        myambient= Finish(0.4)
        myambientlight= Color(0.6, 1.0, 1.0)
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
        w= Color(1.0, 1.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 5.0, r, myambient)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g, myambient)),
                      (Sphere(Point(3.0, 3.0, 3.0), 1.0, b, myambient))]
	self.assertEqual(cast_ray(myray, myspherelist, myambientlight),
                         Color(0.24, 0.0, 0.0))

    def test_translated_point(self):
        self.assertEqual(translated_point(Sphere(0,0,0)))
        

if __name__== "__main__":
    unittest.main()
