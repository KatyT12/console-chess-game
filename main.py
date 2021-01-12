from classes.Board import Board
from classes.Piece import Piece
from classes.Pawn import Pawn
from classes.Bishop import Bishop

from classes.Piece import chess_pieces
    
import os
import time


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
    self.player1 = Player(1)
    self.player2 = Player(2)
    
    self.board = Board(self.player1,self.player2)
    
    self.players = [self.player1,self.player2]
    self.setup()
    
    self.focus = 0

    self.__loop()

  def setup(self):
    
    for i in range (8):
      piece = Pawn([i,1],"white",self.board)
      self.player1.add_piece(piece)

    for i in range (8):
      piece = Pawn([i,6],"black",self.board)
      self.player2.add_piece(piece)
      
    piece = Bishop([2,0],"white",self.board)
    self.player1.add_piece(piece)
    piece = Bishop([5,0],"white",self.board)
    self.player1.add_piece(piece)

    piece = Bishop([2,7],"black",self.board)
    self.player2.add_piece(piece)
    piece = Bishop([5,7],"black",self.board)
    self.player2.add_piece(piece)


    pass
  
  def __int_input(self,message,min=0,max=7):
    while True:
      var = input(message)
      try:
        var = int(var)
        if(var >= min and var <= max):
          break
        else:
          print("invalid range")
          continue
      except:
        print("that input was invalid")
    return var
        
  
  def take_move_input(self,player):
    player.print_pieces()

    while True:
      inpt = self.__int_input("What piece would you like to move? (Give the corresponding index)",max=len(player.pieces)-1)

      piece = player.pieces[inpt]
      
      possible_positions = self.board.filter(piece.possible_positions())

      if not possible_positions:
        print("No possible positions :( choose a different piece")
        continue

      print("\n")
      for i,p in enumerate(possible_positions):
        print("%d : (%d,%d)" % 
        (i,possible_positions[i][0],possible_positions[i][1]))
      
      coord_index = self.__int_input("Pick one of these possible positions your piece can move to.",max=len(possible_positions)-1)
    
      piece.moveTo(possible_positions[coord_index])
      
      break

      

  #The game loop
  def __loop(self):
    while True:
      print("It is player %d's turn\n" % (self.focus + 1))
      player = self.players[self.focus]

      self.board.print()
      self.take_move_input(player)
      
      time.sleep(1)
      os.system("clear")
      if self.focus == 0:
        self.focus = 1
      else:
        self.focus = 0
        
      
      


      





#https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode


"""
  The white chess pieces will be at top coming downwards and the black chess pieces will be coming the oppisite direction so the piece class has a method that has some options where it will vertically flip things


"""


#Main
if __name__ == "__main__":
  
  game = Game()

