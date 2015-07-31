from data import *
import unittest
import vector_math
from collisions import *

class TestData(unittest.TestCase):
    def test_collision_1(self):
        ray= Ray(Point(-2.0, 0.0, 0.0), Vector(2.0, 0.0, 0.0))
        sphere= Sphere(Point(0.0, 0.0, 0.0), 1.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), Point(-1.0, 0.0, 0.0))

    def test_collision_2(self):
        ray= Ray(Point(0.0, -2.0, 0.0), Vector(0.0, 2.0, 0.0))
        sphere= Sphere(Point(0.0, 0.0, 0.0), 1.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), Point(0.0, -1.0, 0.0))

    def test_collision_3(self):
        ray= Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 5.0, 0.0))
        sphere= Sphere(Point(0.0, 0.0, 0.0), 2.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), Point(0.0, 2.0, 0.0))
        
    def test_collision_4(self):
        ray= Ray(Point(2.0, 4.0, 0.0), Vector(0.0, -5.0, 0.0))
        sphere= Sphere(Point(0.0, 0.0, 0.0), 2.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), Point(2.0, 0.0, 0.0))


    def test_collision_5(self):
        ray= Ray(Point(0.0, -3.0, 0.0), Vector(0.0, 8.0, 0.0))
        sphere= Sphere(Point(0.0, 0.0, 0.0), 2.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), Point(0.0, -2.0, 0.0))

    def test_collision_6(self):
        ray= Ray(Point(0.0, 1.0, 0.0), Vector(0.0, 0.0, 1.5))
        sphere= Sphere(Point(0.0, 1.0, 2.0), 1.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), Point(0.0, 1.0, 1.0))

    def test_collision_7(self):
        ray= Ray(Point(2.0, 0.0, 2.0), Vector(-4.5, 0.0, 0.0))
        sphere= Sphere(Point(-2.0, 0.0, 2.0), 1.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), Point(-1.0, 0.0, 2.0))

    def test_collision_8(self):
        ray= Ray(Point(2.0, 0.0, 2.0), Vector(-4.5, 0.0, 0.0))
        sphere= Sphere(Point(-45.0, -10.0, 2.0), 1.0)
	self.assertEqual(sphere_intersection_point(ray, sphere), None)



    def test_intersection_points(self):
        spheres=[(Sphere(Point(0.0, 0.0, 0.0), 1.0)),
                 (Sphere(Point(10.0, 0.0, 0.0), 1.0))]
        ray= Ray(Point(-2.0, 0.0, 0.0), Vector(17.0, 0.0, 0.0))
        expected=[ (Sphere(Point(0.0, 0.0, 0.0), 1.0), Point(-1.0, 0.0, 0.0)),
                  (Sphere(Point(10.0, 0.0, 0.0), 1.0), Point(9.0, 0.0, 0.0))]
        self.assertEqual(find_intersection_points(spheres, ray), expected)

    def test_intersection_points2(self):
        spheres=[(Sphere(Point(-2.0, 0.0, 2.0), 1.0)),
                 (Sphere(Point( 2.0, 0.0, 2.0), 1.0))]
        ray= Ray(Point(10.0, 0.0, 2.0), Vector(-20.0, 0.0, 0.0))
        expected=[(Sphere(Point(-2.0, 0.0, 2.0), 1.0), Point(-1.0, 0.0, 2.0)),
                   (Sphere(Point(2.0, 0.0, 2.0), 1.0), Point(3.0, 0.0, 2.0))]
        self.assertEqual(find_intersection_points(spheres, ray), expected)

        
        

    def test_sphere_normal_at_point(self):
        sphere= Sphere(Point(-2.0, 0.0, 2.0), 1.0)
        point= Point(3.0, 0.0, 2.0)
        self.assertEqual(sphere_normal_at_point(sphere, point), Vector(1.0, 0.0, 0.0))

    def test_sphere_normal_at_point2(self):
        sphere= Sphere(Point(10.0, 0.0, 0.0), 1.0)
        point= Point(9.0, 0.0, 0.0)
        self.assertEqual(sphere_normal_at_point(sphere, point), Vector(-1.0, 0.0, 0.0))


        

if __name__== "__main__":
    unittest.main()
