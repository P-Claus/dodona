def area_of_triangle( bottom, height ):
    area = 0.5 * bottom * height
    return bottom, height, area

bottom, height, area = area_of_triangle(4.5, 1.0)
print("The area of a triangle with a bottom of {} and a height of {} is {}".format(bottom, height, area))
