from graphics import *

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo = False):
        if self._win == None:
            return 
        
        # mid x
        mid_x = (self._x1 + self._x2) / 2
        # mid y
        mid_y = (self._y1 + self._y2) / 2

        # to_cell logic is similar
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red" 
        if undo:
            fill_color = "gray"
        
        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(mid_x, mid_y), Point(self._x1, mid_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x2, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(mid_x, mid_y), Point(self._x2, mid_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)
        
        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(mid_x, mid_y), Point(mid_x, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)
        
        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(mid_x, mid_y), Point(mid_x, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)

