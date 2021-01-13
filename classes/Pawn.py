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
    if self.start: #If it is the start pawns can move 2 forward
      max_offset = 2
      self.start = False
    else: 
      max_offset = 1

    vectors = [[0,x+1] for x in range(max_offset)]
    
    vectors = self._vertical_flip(cmd="flip_vectors",vectors=vectors) if self.color == "black" else vectors
    
    positions = [[self.position[0] + x[0],self.position[1]+x[1]] for x in vectors]

    #Check if there are already pieces on the same team, if so remove those possible positions
    positions = self.board.query_friendly_fire(self,positions)

    nearby = self.board.nearby_pieces(self.position)
    
    potential_kills = []
    for coord in nearby:
      
      piece = self.board.getSquare(coord)
      
     
      #Check any positions where it could kill a piece from the opposite team
      if piece.color != self.color:
        tr = numpy.array((1,1))
        tl = numpy.array(self.vecs["top_left"])
        pos = numpy.array(self.position)

        if (pos + tr).tolist() == coord or (pos + tl).tolist() == coord:
          potential_kills.append(coord)
    
    
    positions = positions.__add__(potential_kills)

    return positions
