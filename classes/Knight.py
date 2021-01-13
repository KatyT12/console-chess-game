from classes.Piece import Piece
from classes.Piece import chess_pieces

class Knight(Piece):
    def __init__(self,position,color,board):
    
      if color == "white":
        code = chess_pieces["w_knight"]
      elif color == "black":
        code = chess_pieces["b_knight"]
      
      super().__init__(position,color,board,code)
  
    def possible_positions(self):
      possible_positions = self.board.get_l(self)


      return possible_positions

