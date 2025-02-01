from manim import *
from typing import Tuple
import numpy as np
import os

SQUARE_Z = 0
HIGHLIGHT_Z = 1
PIECE_Z = 2

class CircleBoard(Group):
    def __init__(self, size, **kwargs):
        super().__init__(**kwargs)
        size=size        
        self.squares = [[None for _ in range(size)] for _ in range(size)]
        self.draw_empty_board(size)

    def draw_empty_board(self, size):
        board = []
        size=size
        for i in range(size):
            for j in range(size):
                color = "#B58863" if ((i + j + 1) % 2) == 0 else "#F0D9B5"
                square = Square(0.999, stroke_color=BLACK, stroke_width=0)
                #square = Circle(0.999, stroke_color=BLACK, stroke_width=0)
                square.set_fill(color, 1)
                square.shift(i * DOWN + j * RIGHT)
                square.set_z(SQUARE_Z)
                self.squares[i][j] = square

        for row in self.squares:
            for sq in row:
                self.add(sq)

    def convert_to_circles(self,size):
        # Create a new VGroup for the circles
        circle_board = Group()
        
        # Convert each square to a circle while maintaining position and color
        for i in range(size):
            for j in range(size):
                square = self.squares[i][j]
                circle = Circle(radius=0.5)  # Since squares are ~1 unit
                circle.move_to(square.get_center())
                #circle.shift(DOWN*0.5+LEFT*0.5)
                circle.set_fill(square.get_fill_color(), 1)
                circle.set_stroke(width=0)
                circle.set_z(SQUARE_Z).scale(0.1)
                circle_board.add(circle)
        
        return circle_board
    
    

    def animate_to_circles(self,size):
        circles = self.convert_to_circles(size)
        return Transform(self, circles)
    
    def add_circle(self, i, j, color):
        circle = Circle(2, stroke_width=0, fill_color=color, fill_opacity=0.7)
        circle.shift(UP*j+RIGHT*i)
        circle.z_index=1
        self.add(circle)