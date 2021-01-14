from classes.Piece import Piece
from classes.Piece import chess_pieces

class Queen(Piece):
    def __init__(self,position,color,board):
    
      if color == "white":
        code = chess_pieces["w_queen"]
      elif color == "black":
        code = chess_pieces["b_queen"]
      
      super().__init__(position,color,board,code)
  
    def possible_positions(self):
      possible_positions = self.board.diagonal_to(self)
      horizontal_and_vertical = self.board.get_horizontal_and_vertical(self)
      possible_positions = possible_positions.__add__(horizontal_and_vertical)

      return possible_positions

