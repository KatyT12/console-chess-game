from classes.Piece import Piece
from classes.Piece import chess_pieces
import numpy


class Pawn(Piece):
  def __init__(self,position,color,board):
    self.start = True
    
    if color == "white":
      code = chess_pieces["w_pawn"]
    elif color == "black":
      code = chess_pieces["b_pawn"]
    
    super().__init__(position,color,board,code)
  
  #calculates the possible positions the coord can move to
  def possible_positions(self):
    if self.turns == 0: #If it is the start pawns can move 2 forward
      max_offset = 2
    else: 
      max_offset = 1

    vv = [[0,1]] if self.color == "white" else [[0,-1]]
    dv = [[1,1],[-1,1]] if self.color == "white" else [[1,-1],[-1,-1]]

    positions = self.board.get_with_vecs(self,vv,offset=max_offset,kill=False)
    nearby = self.board.get_with_vecs(self,dv,offset=1,kill=True)
       
    potential_kills = []
    for coord in nearby:
      piece = self.board.getSquare(coord)
      if piece != 0:
        if piece.color != self.color:
            potential_kills.append(coord)
    
    positions = positions.__add__(potential_kills)

    return positions
