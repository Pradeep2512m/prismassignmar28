from math import sqrt


def Suface_Area(length,width,height):
    return 2*(width*length+height*length+height*width)

def Volume(length,width,height):
    return width*height*length

def Space_Diagonal(length,width,height):
    return sqrt(width**2+height**2+length**2)

if __name__ == "__main__":

    length = int(input("enter the value of length: "))
    height = int(input("enter the value of height: "))
    width = int(input("enter the value of width: "))

    surface_area = Suface_Area(length,width,height)
    print(surface_area)
    volume = Volume(length,width,height)
    print(volume)
    space_diagonal = Space_Diagonal(length,width,height)
    print(space_diagonal)