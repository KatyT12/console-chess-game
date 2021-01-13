from classes.Piece import Piece
from classes.Piece import chess_pieces

class King(Piece):
    def __init__(self,position,color,board):
    
      if color == "white":
        code = chess_pieces["w_king"]
      elif color == "black":
        code = chess_pieces["b_king"]
      
      super().__init__(position,color,board,code)
  
    def possible_positions(self):
        dirs = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        positions = self.board.get_with_vecs(self,dirs,offset=1)
        return positions

