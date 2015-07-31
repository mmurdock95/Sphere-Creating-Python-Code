from data import *
import unittest
import vector_math
from collisions import *
from cast import *

class TestData(unittest.TestCase):
    def test_cast_ray(self):
        myray= Ray(Point(10.0, 0.0, 2.0), Vector(-20.0, 0.0, 0.0))
	mycolor= Color(1.0, 0.0, 0.0)
        myspherelist=[(Sphere(Point(-2.0, 0.0, 2.0), 1.0, mycolor)),
                      (Sphere(Point( 2.0, 0.0, 2.0), 1.0, mycolor))]
        self.assertTrue(cast_ray(myray, myspherelist))
    
    def test_cast_ray2(self):
        myray=Ray(Point(10.0, 0.0, 2.0), Vector(-20.0, 0.0, 0.0))
	mycolor= Color(0.0, 1.0, 0.0)
        myspherelist= [(Sphere(Point(-2.0, 0.0, 2.0), 1.0, mycolor)),
                       (Sphere(Point( 2.0, 0.0, 2.0), 1.0, mycolor))]

        self.assertTrue(cast_ray(myray, myspherelist))
        
    def test_closest_sphere(self):
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 1.0, r)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g)),
                      (Sphere(Point( 3.0, 3.0, 3.0), 1.0, b))]
	self.assertEqual(cast_ray(myray, myspherelist), g)

    def test_cast_ray3(self):
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(-20.0, -20.0, -20.0))
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
        w= Color(1.0, 1.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 1.0, r)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g)),
                      (Sphere(Point( 3.0, 3.0, 3.0), 1.0, b))]
	self.assertEqual(cast_ray(myray, myspherelist), w)

    def test_closest_sphere(self):
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        r= Color(1.0, 0.0, 0.0)
        g= Color(0.0, 1.0, 0.0)
	b= Color(0.0, 0.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 5.0, r)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g))]
	self.assertEqual(cast_ray(myray, myspherelist), r)

        

if __name__== "__main__":
    unittest.main()
