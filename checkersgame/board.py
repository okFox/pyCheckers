import pygame

# this is a relative import. ie. in the same package
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        # 12 pieces/player to be decremented
        self.red_kings = self.white_kings = 0
        self.red_left = self.white_left = 12
        # self.create_board()

# win stands for window
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            # the modulo allows for starting red on e/o row
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                # (left, top, width, height)

    def create_board(self):
        pass
