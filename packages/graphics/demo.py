import graphics.rectangle
from graphics.Dgraphics import sphere

print("Area of rectangle", graphics.rectangle.area(3, 4))
print("Perimeter of rectangle", graphics.rectangle.perimeter(3, 4))

from graphics.circle import *

print("Area of circle", area(2))
print("Perimeter of circle", perimeter(2))

from graphics.Dgraphics.cuboid import area

print("Area of cuboid", area(1, 2, 3))

from graphics.Dgraphics.cuboid import perimeter

print("Perimeter of cuboid", perimeter(1, 2, 3))

import graphics.Dgraphics.sphere

print("Area of sphere", graphics.Dgraphics.sphere.area(2))
print("Perimeter of sphere", graphics.Dgraphics.sphere.perimeter(2))

