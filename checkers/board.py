













import pygame

# this is a relative import. ie. in the same package
from .constants import BLACK, ROWS, RED, SQUARE_SIZE

class Board:
  def __init__(self):
    self.board = []
    self.selected_piece = None
    self.red_left = self.white_left = 12 # sets 12 pieces per player to be decremented
    self.red_kings = self.white_kings = 0

# win stands for window
  def draw_cubes(self, win):
    win.fill(BLACK)
    for row in range(ROWS):
      for col in range(row % 2, ROWS): # the modulo allows for starting red on every other row
        pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) # (left, top, width, height)