from manim import *
from chess_board import ChessBoard
import numpy as np

class Chess(Scene):
    def construct(self):
        board = ChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

        cd
        for (i, j) in highlights:
            board.add_highlight(i, j, BLUE)
        self.add(board.move_to(ORIGIN))

 