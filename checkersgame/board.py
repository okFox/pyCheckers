import pygame

# this is a relative import. ie. in the same package
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        # 12 pieces/player to be decremented
        self.red_kings = self.white_kings = 0
        self.red_left = self.white_left = 12
        self.create_board()

# win stands for window
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            # the modulo allows for starting red on e/o row
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                # (left, top, width, height)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1 % 2)):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)    
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)