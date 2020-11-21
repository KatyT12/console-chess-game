from sub.Board import Board
from sub.Pieces import Piece
from sub.Pieces import Pawn
from sub.Pieces import chess_pieces
#Board is 8x8

    



class Player:
  def __init__(self,num):
    self.num = num
    self.pieces = []
  def add_piece(self,piece):
    self.pieces.append(piece)
  def remove_piece(self,piece):
    self.pieces.remove(piece)
  def print_pieces(self):
    print("Your pieces on the board:")
    for i,piece in enumerate(self.pieces):
      print(i," - ",piece," at coord",piece.position)
    print("\n")


class Game: 
  def __init__(self):
    self.board = Board()
    
    self.player1 = Player(1)
    self.player2 = Player(2)
    
    self.players = [self.player1,self.player2]
    
    
    self.focus = 0
    self._loop()

  def setup():
    pass
  
  def _int_val(self,var):
    try:
      var = int(var)
      return var
    except:
      print("invalid")
      return ""
  
  def take_move_input(self):
    self.player1.print_pieces()
    
    inpt = ""
    while type(inpt) != int:
      inpt = input("What piece would you like to move? (Give the corresponding index)")
      inpt = self._int_val(inpt)
    
    piece = self.player1.pieces[inpt]
    
    #For debugging, remove later
    possible_positions = piece.possible_positions()
   
  

    


  def _loop(self):
    while True:
      #testPiece = Piece([1,0],"white",self.board,chess_pieces["w_pawn"])
      testPawn = Pawn([1,1],"white",self.board)
      
      testPawn2 = Pawn([0,3],"black",self.board)


      self.player1.add_piece(testPawn)
      
      self.player2.add_piece(testPawn2)

      self.board.print()
      testPawn.move()
      self.board.print()
      
      self.take_move_input()

      
      


      break





#https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode




"""
  The white chess pieces will be at top coming downwards and the black chess pieces will be coming the oppisite direction so the piece class has a method that has some options where it will vertically flip things
"""


#Main
if __name__ == "__main__":
  
  game = Game()
