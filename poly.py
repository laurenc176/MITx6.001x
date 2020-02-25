import math
def polysum(n, s):
    """ Sum the area and square of the perimeter of a regular polygon.
        Returns the sum rounded to 4 decimal places.
        n is number of sides
        s is the length of each side"""
    def areaofpoly(n,s):
        area = (0.25*n*s**2)/math.tan(math.pi/n)
        return area
    def perofpoly(n,s):
        per = n * s
        return per
    total = areaofpoly(n,s) + perofpoly(n,s) **2
    return round(total,4)
    
