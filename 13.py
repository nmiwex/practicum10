import turtle as t


def triangle(x1: float, y1: float,
                   x2: float, y2: float,
                   x3: float, y3: float,
                   color: str) -> None:
    '''
    Function, drawing triangle.
    :param x1: coordinate x of first point
    :param y1: coordinate y of first point
    :param x2: coordinate x of second point
    :param y2: coordinate y of second point
    :param x3: coordinate x of third point
    :param y3: coordinate y of third point
    :param color: color of triangle
    :return: None
    '''
    t.up()
    t.setposition(x1, y1)
    t.down()
    t.color('#fff', color)
    t.begin_fill()
    t.setposition(x2, y2)
    t.setposition(x3, y3)
    t.setposition(x1, y1)
    t.end_fill()
    t.seth(0)


def dist(a: tuple, b: tuple) -> float:
    '''
    Function, calculate distance between two points.
    :param a: first point
    :param b: second point
    :return: distance
    '''
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def square(x1: float, y1: float,
           x2: float, y2: float,
           x3: float, y3: float,
           color1: str, color2: str, type = True) -> None:
    '''
    Function, drawing square using triangles. Triangles must be right.
    :param type: type of square (main diagonal or not)
    :param x1: coordinate x of lowest and rightest point of rectangle
    :param y1: coordinate y of lowest and rightest point of rectangle
    :param x2: coordinate x of lowest and leftest point of rectangle
    :param y2: coordinate y of lowest and leftest point of rectangle
    :param x3: coordinate x of highest and rightest point of rectangle
    :param y3: coordinate y of highest and rightest point of rectangle
    :param color: color of rectangle
    :return: None
    '''

    # checking whether points defining right triangles
    side1 = dist((x1, y1), (x2, y2))
    side2 = dist((x1, y1), (x3, y3))
    side3 = dist((x3, y3), (x2, y2))
    if side1 != side2 or side1 ** 2 + side2 ** 2 != side3 ** 2:
        print('Rectangle is not right')
        return

    if type:
        triangle(x1, y1, x2, y2, x2, y3, color1)
        triangle(x2, y3, x1, y1, x3, y3, color2)
    else:
        triangle(x1, y1, x2, y2, x3, y3, color2)
        triangle(x2, y3, x2, y2, x3, y3, color1)


def switch_colors(color1: str, color2: str) -> tuple[str, str]:
    '''
    Function, next color.
    :param color1:
    :return: next color
    '''
    c_dark = "#4169E1"
    c_med = "#ADD8E6"
    c_light = "#F0FFFF"
    c_logic = [c_dark, c_med, c_light, c_med, c_dark, c_med, c_light, c_med]

    ind = 0
    while c_logic[ind] != color1 or c_logic[ind + 1] != color2:
        ind += 1
    color1, color2 = c_logic[ind + 1], c_logic[ind + 2]

    return color1, color2


def main() -> None:
    '''
    Main function, drawing pattern.
    :return: None
    '''
    c_dark = "#4169E1"
    c_med = "#ADD8E6"
    c_light = "#F0FFFF"
    c1, c2 = c_med, c_dark
    x, y = -300, -300

    t.tracer(0)
    t.hideturtle()
    t.setheading(0)
    for row in range(3):
        x = -300
        y += 100
        color_list = []
        for col in range(6):
            x += 100
            if col < 3:
                square(x + 100, y, x, y, x + 100, y + 100, c1, c2, False)
                color_list.append(c1)
                color_list.append(c2)
                c1, c2 = switch_colors(c1, c2)
            else:
                print(color_list, color_list[::-1])
                c1_local, c2_local = (color_list[::-1][0 + (col - 3) * 2],
                          color_list[::-1][0 + (col - 3) * 2 + 1])
                square(x + 100, y, x, y, x + 100, y + 100, c1_local, c2_local,
                       True)

    c1, c2 = c_med, c_dark
    y = 400
    for row in range(3):
        x = -300
        y -= 100
        color_list = []
        for col in range(6):
            x += 100
            if col < 3:
                square(x + 100, y, x, y, x + 100, y + 100, c1, c2, True)
                color_list.append(c1)
                color_list.append(c2)
                c1, c2 = switch_colors(c1, c2)
            else:
                print(color_list, color_list[::-1])
                c1_local, c2_local = (color_list[::-1][0 + (col - 3) * 2],
                          color_list[::-1][0 + (col - 3) * 2 + 1])
                square(x + 100, y, x, y, x + 100, y + 100, c1_local, c2_local,
                       False)
    t.update()
    t.done()


if __name__ == '__main__':
    main()