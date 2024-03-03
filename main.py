from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(10, 10, 50, 50)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(50, 10, 90, 50)
    c2.draw_move(c1)

    c3 = Cell(win)
    c3. has_top_wall = False
    c3.draw(50, 50, 90, 90)
    c3.draw_move(c2, True)

    win.wait_for_close()

main()