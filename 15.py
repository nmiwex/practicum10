import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('#1a1a2e')
screen.title('Night city')
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()


def draw_rectangle(x, y, width, height, color):
    """draws rectangle"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_stars(num_stars: int):
    """
    draws starry sky
    num_stars: number of stars
    """
    t.color('#fff')
    for _ in range(num_stars):
        x = random.randint(-400, 400)
        y = random.randint(50, 300)
        size = random.randint(1, 3)

        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(size)


def draw_moon():
    """draws moon"""
    t.penup()
    t.goto(250, 200)
    t.pendown()
    t.color('#f4f1c9')
    t.dot(60)

    t.penup()
    t.goto(240, 210)
    t.pendown()
    t.color('#1a1a2e')
    t.dot(60)


def draw_windows(start_x, start_y, b_width, b_height):
    """
    Рисует окна внутри здания.
    Окна загораются случайным образом.
    """
    window_size = 10
    gap = 8
    cols = (b_width - gap) // (window_size + gap)
    rows = (b_height - gap) // (window_size + gap)

    lit_color = '#ffd700'
    dark_color = '#2a2a40'

    current_y = start_y + gap

    for r in range(rows):
        current_x = start_x + gap
        for c in range(cols):
            # случайный выбор горит свет или нет (30% что горит)
            if random.random() < 0.3:
                color = lit_color
            else:
                color = dark_color

            draw_rectangle(current_x, current_y, window_size, window_size, color)
            current_x += window_size + gap
        current_y += window_size + gap


def draw_roof(x, y, width, roof_type):
    """
    draws roof of building
    x,y - upper left coordinate of building
    width - width of building
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('#2e2e4e')
    t.begin_fill()

    if roof_type == 'flat':
        t.goto(x + width - 10, y)
        t.goto(x + width - 10, y + 5)
        t.goto(x+10, y + 5)
        t.goto(x+10, y)

    elif roof_type == 'pointed':
        t.goto(x + width, y)
        t.goto(x + width / 2, y + width / 2)
        t.goto(x, y)

    elif roof_type == 'tower':
        t.goto(x + width, y)
        t.goto(x + width - 10, y)
        t.goto(x + width - 10, y + 20)
        t.goto(x + width / 2, y + 40)
        t.goto(x + 10, y + 20)
        t.goto(x + 10, y)

    t.end_fill()


def draw_building(x, width):
    """
    Draws an entire building: the building, roof, and windows.
    The height is randomly generated.
    """
    height = random.randint(100, 400)
    base_y = -300

    building_color = '#2e2e4e'
    draw_rectangle(x, base_y, width, height, building_color)

    draw_windows(x, base_y, width, height)

    roof_types = ['flat', 'flat', 'pointed', 'tower']
    roof = random.choice(roof_types)
    draw_roof(x, base_y + height, width, roof)


def main():
    """the main function generating the landscape"""
    draw_stars(100)
    draw_moon()

    current_x = -400

    while current_x < 400:
        building_width = random.randint(40, 100)
        draw_building(current_x, building_width)

        current_x += building_width - 2

    turtle.done()


if __name__ == '__main__':
    main()