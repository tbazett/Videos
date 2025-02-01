from manim import *
from typing import Tuple
import numpy as np
import os

SQUARE_Z = 0
HIGHLIGHT_Z = 1
PIECE_Z = 2

class ChessBoard(Mobject):
    def __init__(self, fen, **kwargs):
        super().__init__(**kwargs)
        self.fen_rows, self.dims = self._read_fen(fen)
        self.icons = [[None for _ in range(self.dims[1])] for _ in range(self.dims[0])]
        self.squares = [[None for _ in range(self.dims[1])] for _ in range(self.dims[0])]
        self.draw_empty_board()
        self.draw_pieces()


    def move_piece(self, i, j, n, m):
        piece_at = self.icons[n][m]
        anims = [None, None]
        if piece_at is not None:
            anims[0] = FadeOut(piece_at)
        
        piece_to_move = self.icons[i][j]

        piece_to_move.generate_target()

        piece_to_move.target.move_to(self.squares[n][m].get_center())
        anims[1] = MoveToTarget(piece_to_move)

        self.icons[n][m] = piece_to_move #added by Trefor
        self.icons[i][j] = None #added by Trefor
        return anims

    def add_arrow(self, i, j, dx, dy):
        graphical_arrow = Arrow((DOWN * i + RIGHT * j), (DOWN * (i + dx) + RIGHT * (j + dy)), color=BLUE, stroke_width=25, max_stroke_width_to_length_ratio=10, max_tip_length_to_length_ratio=0.5)
        #circle = Circle(0.45, stroke_width=DEFAULT_STROKE_WIDTH*2).shift((DOWN * (i + dx) + RIGHT * (j + dy)))
        #group = Group(circle, graphical_arrow)
        group =graphical_arrow 
        self.add(group)

    def add_knight_arrow(self, i,j, dx, dy, width=15):
        #For 8x8 board use stroek_width 15. For 16x16 use 7. 
        graphical_segment = Line((DOWN * i + RIGHT * j), (DOWN * (i + dx) + RIGHT * j), color=BLUE, stroke_width=width)
        graphical_arrow = Arrow((DOWN * (i+dx) + RIGHT * j), (DOWN * (i + dx) + RIGHT * (j + dy)), color=BLUE, stroke_width=width, max_stroke_width_to_length_ratio=125, max_tip_length_to_length_ratio=0.5, buff=0)
        square=Square(side_length=(width/15)*21/135, fill_color=BLUE, fill_opacity=1, stroke_opacity=0).shift(DOWN*(i+dx)+RIGHT*j)
        group = Group(graphical_segment, graphical_arrow, square)
        group.z_index=1
        #group=graphical_arrow
        self.add(group)

    def add_king_arrow(self, i,j, dx, dy, width=15):
        #For 8x8 board use stroek_width 15. For 16x16 use 7. 
        graphical_arrow = Arrow((DOWN * i + RIGHT * j), (DOWN * (i + dx) + RIGHT * (j + dy)), color=YELLOW, stroke_width=width, max_stroke_width_to_length_ratio=125, max_tip_length_to_length_ratio=0.5, buff=0)
        graphical_arrow.z_index=1
        self.add(graphical_arrow)

    def add_text(self, i, j, text,color):
        tex = MathTex(text)
        tex.set_color(color).scale(2)
        tex.z_index=2
        tex.move_to(RIGHT * i + DOWN * j)     
        self.add(tex)
        

    def FadeIn_text(self, i, j, text,color):
        board_position = self.get_center()
        tex = MathTex(text)
        tex.set_color(color).scale(2)
        tex.z_index=2
        tex.move_to(-board_position+RIGHT * i + DOWN * j)  
        anim =FadeIn(tex)
        return anim 


    def add_highlight(self, i, j, color):
        square = Square(0.999, stroke_width=0, fill_color=color, fill_opacity=0.7)
        square.move_to(self.squares[i][j])
        self.add(square)
        
    def set_piece_opacities(self, opacities: np.ndarray):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                icon = self.icons[i][j]
                if icon is not None:
                    alpha = opacities[i, j]
                    alpha_mask = np.copy(icon.pixel_array[:, :, 3]) != 0
                    icon.pixel_array[:, :, 3] = int(255 * alpha) * alpha_mask

    def _piece_to_icon(self, c):
        prefix = "w" if c.isupper() else "b"
        prefix = prefix if not c.isspace() else ""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        piece_path = os.path.join(dir_path, "png_pieces/{}.png".format(prefix + c.upper()))
        icon = ImageMobject(piece_path)
        icon.set_x(0)
        icon.set_y(0)
        icon.scale(0.27)
        if c.lower() == "k":
            icon.shift(UP * 0.035)
        return icon

    # def _read_fen(self, fen):
    #     if " " in fen:
    #         fen = fen.split(" ")[0]
        
    #     rows = fen.split("/")


    #     for i, row in enumerate(rows):
    #         new_row = ""
    #         for c in row:
    #             if c in "123456789":
    #                 new_row += " " * int(c)
    #             else:
    #                 new_row += c
    #         rows[i] = new_row
    #     dims = (len(rows), max([len(row) for row in rows]))
    #     return rows, dims
    def _read_fen(self, fen):
        if " " in fen:
            fen = fen.split(" ")[0]  # Extract the board part of the FEN string
        
        rows = fen.split("/")  # Split rows by '/'
        processed_rows = []
        
        for row in rows:
            new_row = ""
            number_buffer = ""  # Buffer to handle multi-digit numbers
            
            for c in row:
                if c.isdigit():  # Accumulate digits
                    number_buffer += c
                else:
                    if number_buffer:  # If we have a buffered number, expand it
                        new_row += " " * int(number_buffer)
                        number_buffer = ""  # Clear the buffer
                    new_row += c  # Add the character (e.g., a piece symbol)
            
            if number_buffer:  # Handle any remaining buffered number
                new_row += " " * int(number_buffer)
            
            processed_rows.append(new_row)
    
        # Determine dimensions
        dims = (len(processed_rows), max(len(row) for row in processed_rows))
        return processed_rows, dims

    def draw_pieces(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                if not self.fen_rows[i][j].isspace():
                    icon = self._piece_to_icon(self.fen_rows[i][j]).shift(i * DOWN + j * RIGHT).set_z_index(PIECE_Z)
                    self.icons[i][j] = icon
        
        for row in self.icons:
            for icon in row:
                if icon is not None:
                    self.add(icon)

    def draw_empty_board(self):
        board = []
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                color = "#B58863" if ((i + j + 1) % 2) == 0 else "#F0D9B5"
                square = Square(0.999, stroke_color=BLACK, stroke_width=0)
                #square = Circle(0.999, stroke_color=BLACK, stroke_width=0)
                square.set_fill(color, 1)  #CHANGE OPACITY BACK LATER
                square.shift(i * DOWN + j * RIGHT)
                square.set_z(SQUARE_Z)
                self.squares[i][j] = square

        for row in self.squares:
            for sq in row:
                self.add(sq)

    def convert_to_circles(self):
        for mob in self.submobjects[:]:  # Create a copy of the list to iterate over
            if isinstance(mob, Square):  # Only convert if the mobject is a Square
                # Get the center and width of the square
                center = mob.get_center()
                width = mob.get_width()
                
                # Create a circle with the same size
                circle = Circle(radius=width/2)
                circle.move_to(center)
                
                # Match the style properties of the square
                circle.set_style(
                    stroke_color=mob.get_stroke_color(),
                    stroke_width=mob.get_stroke_width(),
                    fill_color=mob.get_fill_color(),
                    fill_opacity=mob.get_fill_opacity()
                ).scale(0.1)
                
                # Replace the square with the circle in the collection
                self.remove(mob)
                self.add(circle)


    

    def animate_to_circles(self):
        circles = self.convert_to_circles()
        return ReplacementTransform(self, circles)