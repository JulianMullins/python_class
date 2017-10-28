from Point1 import *
import copy


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """

my_circle = Circle()
my_circle.center = Point()
my_circle.center.x = 150
my_circle.center.y = 100
my_circle.radius = 75


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    dist = distance_between_points(circle.center, point)

    if dist <= circle.radius:
        return True
    else:
        return False



def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    rect_corner = Point()
    rect_corner.x = rect.corner.x
    rect_corner.y = rect.corner.y

    return point_in_circle(rect_corner, circle)

def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """

    count = []
    rect_corner = Point()
    rect_corner.x = rect.corner.x
    rect_corner.y = rect.corner.y

    for i in range(4):
        if i == 0:
            count.append(point_in_circle(rect_corner, circle))
        elif i == 1:
            rect_corner.x = rect.corner.x + rect.width
            count.append(point_in_circle(rect_corner, circle))
        elif i == 2:
            rect_corner.y = rect.corner.y + rect.height
            count.append(point_in_circle(rect_corner, circle))
        elif i == 3:
            rect_corner.x = rect.corner.x - rect.width
            count.append(point_in_circle(rect_corner, circle))

    for i in count:
        if i == False:
            return i
    return True
    

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
