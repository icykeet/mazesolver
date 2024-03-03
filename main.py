from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(250, 100, 500, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(150, 200, 300, 250)

    win.wait_for_close()

main()