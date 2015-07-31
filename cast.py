import collisions
from  vector_math import *
from data import Point, Ray, Color, Finish

def cast_ray(ray, sphere_list, ambient, light, eye_point):
    points= collisions.find_intersection_points(sphere_list, ray)
    if len(points) == 0:
        return Color(1.0, 1.0, 1.0)
    else:
        #using helper functions below
        closest= closest_sphere(ray, points)
        pe=translated_point(closest[0], closest[1])
        n=normalize_vector(difference_point(closest[1], closest[0].center))
        ldir=normalized_ldir(light.pt, pe)
        visable=light_visable(n, ldir)
        spheres_finish_color=finish_sphere(closest[0], ambient)
        reflection=reflection_vector(ldir, n)
        vdir=normalized_vdir(eye_point, pe)
        specular=specular_intensity(vdir, reflection)
        if not visable:
            return spheres_finish_color
        newpoints=collisions.find_intersection_points(sphere_list, Ray(pe, ldir))
        if newpoints != []:
            return spheres_finish_color
        #no shine
        else:
            red=spheres_finish_color.r + (dot_vector(n, ldir) * light.color.r *
                                          closest[0].color.r * closest[0].finish.diffuse)
            green=spheres_finish_color.g + (dot_vector(n, ldir) * light.color.g *
                                            closest[0].color.g * closest[0].finish.diffuse)
            blue=spheres_finish_color.b + (dot_vector(n, ldir) * light.color.b *
                                           closest[0].color.b * closest[0].finish.diffuse)
            if specular<=0:
                return Color(red, green, blue)
            #white shine
            else:
                red1= red + (light.color.r * closest[0].finish.specular *
                             specular**(1.0/closest[0].finish.roughness))
                green1= green + (light.color.g * closest[0].finish.specular *
                                 specular**(1.0/closest[0].finish.roughness))
                blue1= blue + (light.color.b * closest[0].finish.specular *
                               specular**(1.0/closest[0].finish.roughness))
                return Color(red1, green1, blue1)


def closest_sphere(ray, sphere_list_points):
    distance= length_vector(vector_from_to(ray.pt, sphere_list_points[0][1]))
    nearest= sphere_list_points[0][0]
    point=sphere_list_points[0][1]
    for (l, n) in sphere_list_points:
        length=length_vector(vector_from_to(ray.pt, n))
        if length < distance:
                distance=length
                nearest= l
                point = n
    return (nearest, point)

def finish_sphere(closest_sphere, ambient):
    red=closest_sphere.color.r * ambient.r * closest_sphere.finish.ambient
    green=closest_sphere.color.g * ambient.g * closest_sphere.finish.ambient
    blue=closest_sphere.color.b * ambient.b * closest_sphere.finish.ambient
    return Color(red, green, blue)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
                  eye_point, sphere_list, ambient, light):
    delta_x= (max_x - min_x)/width
    delta_y= (max_y - min_y)/height
    list_of_rows=[]
    for y in xrange(height):
        #updated to make a list of lists for hw5
        rows=[]
        for x in xrange(width):
            x_val=min_x + x*delta_x
            y_val=max_y - y*delta_y
            dir=vector_from_to(eye_point, Point(x_val, y_val, 0))
            r=Ray(eye_point, dir)
            result= cast_ray(r, sphere_list, ambient, light, eye_point)
            rows.append((min(int(result.r*255),255), min(int(result.g*255),255), min(int(result.b*255),255)))
        list_of_rows.append(rows)
    return list_of_rows

    
def translated_point(sphere, point):
    return translate_point(point, scale_vector
                           (normalize_vector(difference_point(point, sphere.center)), 0.01))

def normalized_ldir(lights_pt, pe):
    return normalize_vector(difference_point(lights_pt, pe))

def light_visable(n, ldir):
    good=dot_vector(n, ldir)
    return good>0

def reflection_vector(ldir, n):
    return difference_vector(ldir, scale_vector(n, 2.0*dot_vector(n, ldir)))

def normalized_vdir(eye_point, pe):
    return normalize_vector(difference_point(pe, eye_point))

def specular_intensity(reflection, vdir):
    return float(dot_vector(reflection, vdir))
