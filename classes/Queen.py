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
      possible_positions.__add__(self.board.get_horizontal_and_vertical(self))

      return possible_positions

