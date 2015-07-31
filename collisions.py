from data import *
from vector_math import *
from math import *

def sphere_intersection_point(ray, sphere):
        a=dot_vector(ray.dir, ray.dir)
        b=2.0 * dot_vector(difference_point(ray.pt, sphere.center), ray.dir)
        c=dot_vector(difference_point(ray.pt, sphere.center),
                     difference_point(ray.pt, sphere.center)) - sphere.radius**2
        if (b**2 - 4*a*c) > 0:
                t = ((-b) + sqrt(b**2 - 4*a*c))/ (2*a)
                t2= ((-b) - sqrt(b**2 - 4*a*c))/ (2*a)
                if t>=0 and t2>=0:
                        if t<t2:
                                return translate_point(ray.pt, scale_vector(ray.dir, t))
                        elif t2<t:
                                return translate_point(ray.pt, scale_vector(ray.dir, t2))
                elif t>=0 and t2<0:
                        return translate_point(ray.pt, scale_vector(ray.dir, t))
                elif t2>=0 and t<0:
                        return  translate_point(ray.pt, scale_vector(ray.dir, t2))
        elif (b**2 - 4*a*c) == 0:
                t = (-b) / (2*a)
                if t>=0:
                        return translate_point(ray.pt, scale_vector(ray.dir, t))
        else:
                return None


def find_intersection_points(sphere_list, ray2):
        list_points= []
        for x in range(len(sphere_list)):
                 if sphere_intersection_point(ray2, sphere_list[x]) != None:
                        list_points.append( (sphere_list[x], sphere_intersection_point(ray2, sphere_list[x])) )
        return list_points

def sphere_normal_at_point(sphere, point):
        return normalize_vector(vector_from_to(sphere.center, point))

