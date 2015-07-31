from data import *
import unittest
import vector_math
from collisions import *
from cast import *

class TestData(unittest.TestCase):
    def test_cast_ray(self):
        myambient= Finish(0.2, 0.4, 0.5, 0.05)
        myambientlight= Color(1.0, 1.0, 1.0)
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        light= Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
        myeye= Point(0.0, 0.0, -14.0)
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
        w= Color(1.0, 1.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 1.0, r, myambient)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g, myambient)),
                      (Sphere(Point(3.0, 3.0, 3.0), 1.0, b, myambient))]
	self.assertEqual(cast_ray(myray, myspherelist, myambientlight, light, myeye),
                         Color(0.0, 0.2, 0.0))

    def test_cast_ray2(self):
        myambient= Finish(0.2, 0.4, 0.5, 0.05)
        myambientlight= Color(1.0, 1.0, 1.0)
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        light= Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
        myeye= Point(0.0, 0.0, -14.0)
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
        w= Color(1.0, 1.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 5.0, r, myambient)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g, myambient)),
                      (Sphere(Point(3.0, 3.0, 3.0), 1.0, b, myambient))]
	self.assertEqual(cast_ray(myray, myspherelist, myambientlight, light, myeye),
                         Color(0.2, 0.0, 0.0))

    def test_cast_ray3(self):
        myambient= Finish(0.2, 0.4, 0.5, 0.05)
        myambientlight= Color(0.0, 1.0, 1.0)
        myray= Ray(Point(0.0, 0.0, 0.0), Vector(20.0, 20.0, 20.0))
        light= Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
        myeye= Point(0.0, 0.0, -14.0)
        r= Color(1.0,0.0,0.0)
        g= Color(0.0,1.0,0.0)
	b= Color(0.0, 0.0, 1.0)
        w= Color(1.0, 1.0, 1.0)
	myspherelist=[(Sphere(Point(4.0, 4.0, 4.0), 5.0, r, myambient)),
                      (Sphere(Point(2.0, 2.0, 2.0), 1.0, g, myambient)),
                      (Sphere(Point(3.0, 3.0, 3.0), 1.0, b, myambient))]
	self.assertEqual(cast_ray(myray, myspherelist, myambientlight,light, myeye),
                         Color(0.0, 0.0, 0.0))

        
    def test_translated_point(self):
        myambient1= Finish(0.2, 0.4, 0.5, 0.05)
        blue= Color(0.0, 0.0, 1.0)
        sphere1= Sphere(Point(0.0, 0.0, 0.0), 2.0, blue, myambient1)
        self.assertEqual(translated_point(sphere1, Point(0.0,100.0,0.0)), Point(0.0,100.01,0.0))

    def test_translated_point2(self):
        myambient1= Finish(0.2, 0.4, 0.5, 0.05)
        blue= Color(0.0, 0.0, 1.0)
        sphere1= Sphere(Point(0.0, 0.0, 0.0), 2.0, blue, myambient1)
        self.assertEqual(translated_point(sphere1, Point(0.0,0.0,100.0)), Point(0.0, 0.0 , 100.01))

    def test_normalized_ldir(self):
        light= Light(Point(4.0, 0.0, 0.0), Color(1.5, 1.5, 1.5))
        pe=Point(0.0, 0.0, 0.0)
        self.assertEqual(normalized_ldir(light.pt, pe), Vector(1.0, 0.0, 0.0))

    def test_normalized_ldir2(self):
        light= Light(Point(0.0, 4.0, 0.0), Color(1.5, 1.5, 1.5))
        pe=Point(0.0, 0.0, 0.0)
        self.assertEqual(normalized_ldir(light.pt, pe), Vector(0.0, 1.0, 0.0))

    def test_light_visable(self):
        n=Vector(0.0,0.0,0.0)
        ldir=Vector(1.0, 1.0, 1.0)
        self.assertFalse(light_visable(n, ldir))

    def test_light_visable2(self):
        n=Vector(1.0,1.0,1.0)
        ldir=Vector(1.0, 1.0, 1.0)
        self.assertTrue(light_visable(n, ldir))

    def test_reflection_vector(self):
        n=Vector(1.0,1.0,1.0)
        ldir=Vector(1.0, 1.0, 1.0)
        self.assertEqual(reflection_vector(n, ldir), Vector(-5.0, -5.0, -5.0))

    def test_reflection_vector2(self):
        ldir=Vector(0.0,0.0,0.0)
        n=Vector(1.0, 1.0, 1.0)
        self.assertEqual(reflection_vector(n, ldir), Vector(1.0, 1.0, 1.0))

    def test_normalized_vdir(self):
        eye_point=Point(0.0,0.0,0.0)
        pe=Point(2.0,0.0,0.0)
        self.assertEqual(normalized_vdir(eye_point, pe), Vector(1.0, 0.0,0.0))

    def test_normalized_vdir2(self):
        eye_point=Point(0.0,0.0,0.0)
        pe=Point(0.0,2.0,0.0)
        self.assertEqual(normalized_vdir(eye_point, pe), Vector(0.0, 1.0,0.0))

    def test_specular_intensity(self):
        reflection=Vector(0.0,0.0,0.0)
        vdir=Vector(0.0,0.0,0.0)
        self.assertEqual(specular_intensity(reflection, vdir), 0.0)

    def test_specular_intensity2(self):
        reflection=Vector(1.0,0.0,0.0)
        vdir=Vector(1.0,0.0,0.0)
        self.assertEqual(specular_intensity(reflection, vdir), 1.0)



    
if __name__== "__main__":
    unittest.main()


