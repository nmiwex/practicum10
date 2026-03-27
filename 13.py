import turtle

L = '#FFE4E1'
M = '#FFC0CB'
D = '#DB7093'


def triangle(x1, y1, x2, y2, x3, y3, color):
    """
    draws a triangle based on coordinates
    :return: None
    """
    turtle.up()
    turtle.setposition(x1, y1)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setposition(x2, y2)
    turtle.setposition(x3, y3)
    turtle.setposition(x1, y1)
    turtle.end_fill()


def square(x, y, size, split_type, color1, color2):
    """
    drawing square using triangles.
    :param x: the upper left x coordinate
    :param y: the upper left y coordinate
    :param size: the side of the square
    :param split_type: the type of diagonal (1 is '\', 2 is '/')
    :param color1: the color of the first triangle
    :param color2: the color of the second triangle
    :return: None
    """

    turtle.pencolor('#fff')
    turtle.pensize(2)

    if split_type == 1:
        triangle(x, y, x, y - size, x + size, y - size, color1)
        triangle(x + size, y - size, x + size, y, x, y, color2)

    else:
        triangle(x + size, y, x, y, x, y - size, color1)
        triangle(x, y - size, x + size, y - size, x + size, y, color2)


def draw_pattern():
    turtle.setup(650, 650)
    turtle.title('Кафельная плитка')
    turtle.bgcolor('#F5FFFA')

    turtle.tracer(0)

    size = 70

    # Каждая скобка это один квадрат (направление_разреза, цвет_1, цвет_2)
    grid = [
        [(1, M, D), (1, D, M), (1, M, L), (2, L, M), (2, M, D), (2, D, M)],
        [(1, L, M), (1, M, D), (1, D, M), (2, M, D), (2, D, M), (2, M, L)],
        [(1, M, L), (1, L, M), (1, M, D), (2, D, M), (2, M, L), (2, L, M)],
        [(2, M, L), (2, L, M), (2, M, D), (1, D, M), (1, M, L), (1, L, M)],
        [(2, L, M), (2, M, D), (2, D, M), (1, M, D), (1, D, M), (1, M, L)],
        [(2, M, D), (2, D, M), (2, M, L), (1, L, M), (1, M, D), (1, D, M)],
    ]

    # Координаты для старта (левый верхний угол)
    start_x = -(size * 3)
    start_y = (size * 3)

    for row in range(6):
        for col in range(6):
            x = start_x + (col * size)
            y = start_y - (row * size)

            split_type, color1, color2 = grid[row][col]

            square(x, y, size, split_type, color1, color2)

    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    draw_pattern()