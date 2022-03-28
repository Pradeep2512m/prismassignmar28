import RectangularPrism

from math import sqrt

def test_Suface_Area():
    length = 10
    width = 5
    height = 2
    result = RectangularPrism.Suface_Area(length,width,height)
    assert result == 2*(width*length+height*length+height*width)

def test_Volume():
    length = 20
    width = 4
    height = 20
    result = RectangularPrism.Volume(length,width,height)
    assert result == width*height*length

def test_Space_Diagonal():
    length = 30
    width = 9
    height = 4
    result = RectangularPrism.Space_Diagonal(length,width,height)
    assert result == sqrt(width**2+height**2+length**2)