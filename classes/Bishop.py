from classes.Piece import Piece
from classes.Piece import chess_pieces

class Bishop(Piece):
    def __init__(self,position,color,board):
    
      if color == "white":
        code = chess_pieces["w_bishop"]
      elif color == "black":
        code = chess_pieces["b_bishop"]
      
      super().__init__(position,color,board,code)
  
    def possible_positions(self):
      possible_positions = self.board.diagonal_to(self)


      return possible_positions

