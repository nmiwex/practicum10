import turtle
import math
scr = turtle.Screen()
scr.bgcolor('#FAEBD7')
t = turtle.Turtle()
t.pensize(1)
turtle.tracer(0)
t.penup()


def diamond(cx, cy, side, fill_color, contour='#fff'):
    """
    draws a diamond
    :param cx: center x coordinate
    :param cy: center y coordinate
    :param side: side length
    :param fill_color: color of the diamond
    :param contour: color of the diamond contour
    :return: None
    """
    half_diag = side / math.sqrt(2)
    t.color(contour, fill_color)
    t.goto(cx, cy - half_diag)
    t.pendown()
    t.begin_fill()
    t.lt(45)

    for _ in range(4):
        t.fd(side)
        t.lt(90)

    t.end_fill()
    t.penup()


def crcl(cx, cy, radius, fill_color, contour='#fff'):
    """
    draws a circle
    :param cx: center x coordinate
    :param cy: center y coordinate
    :param radius: radius of the circle
    :param fill_color: color of the circle
    :param contour: color of the circle contour
    :return: None
    """
    t.color(contour, fill_color)
    t.goto(cx, cy - radius)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()


def triangle(x, y, side, heading, fill_color, contour='#fff'):
    """
    draws a triangle
    :param x: lower corner x coordinate
    :param y: lower corner y coordinate
    :param side: side length
    :param heading: the direction of drawing
    :param fill_color: color of the triangle
    :param contour: color of the triangle contour
    :return: None
    """
    t.color(contour, fill_color)
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.begin_fill()

    for _ in range(3):
        t.forward(side)
        t.left(120)

    t.end_fill()
    t.penup()


def motif(cx, cy, side, diamond_col, circle_col, triangle_col):
    """
    draws a motif
    :param cx: center x coordinate
    :param cy: center y coordinate
    :param side: diamond side length
    :param diamond_col: color of the diamond
    :param circle_col: color of the circle
    :param triangle_col: color of the triangle
    :return: None
    """
    half_diag = side / math.sqrt(2)
    diamond(cx, cy, side, diamond_col)
    crcl(cx, cy, half_diag * 0.4, circle_col)

    triangle_side = side * 0.5
    triangle_distance = half_diag * 0.5
    upper_right = [cx + triangle_distance, cy + triangle_distance]
    upper_left = [cx - triangle_distance, cy + triangle_distance]
    lower_left = [cx - triangle_distance, cy - triangle_distance]
    lower_right = [cx + triangle_distance, cy - triangle_distance]

    triangle(upper_right[0], upper_right[1], triangle_side, 15, triangle_col)
    triangle(upper_left[0], upper_left[1], triangle_side, 105, triangle_col)
    triangle(lower_left[0], lower_left[1], triangle_side, 195, triangle_col)
    triangle(lower_right[0], lower_right[1], triangle_side, 285, triangle_col)

    t.setheading(0)


def ornament(rows, cols, side, step):
    colors_diamond = ['#6d322a', '#cfa195', '#87564b', '#c6b8ab']
    colors_circle = ['#fff', '#d2bdab', '#a59383', '#e2b8ad']
    start_x = - (cols - 1) * step / 2
    start_y = (rows - 1) * step / 2

    for r in range(rows):
        for c in range(cols):
            cx = start_x + c * step
            cy = start_y - r * step

            col_d = colors_diamond[(r + c) % len(colors_diamond)]
            col_c = colors_circle[(r * 2 + c) % len(colors_circle)]

            motif(cx, cy, side, col_d, col_c, '#E9967A')


if __name__ == '__main__':
    ornament(5, 7, 70, 150)
    turtle.done()