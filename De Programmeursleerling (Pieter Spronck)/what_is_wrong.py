def area_of_triangle( bottom, height ):
    area = 0.5 * bottom * height
    string = "The area of a triangle with a bottom of {} and a height of {} is {}".format(bottom, height, area)
    return string

print(area_of_triangle(4.5, 1.0))