import numpy


class Board:
  
  """
  Outside of the board class the coordinates on the board are seen as horizontal
  being x and vertical being y but the board is a 2D array so when assigning
  something in it you would do eg. item[vertical][horizontal]. This annoys me so in the board class I have a swap method which is called whenever a coordinate is taken in from outside or being outputted. Remember to use the swap method in public methods when dealing with coordinates
  """

  coords = [
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0]]
  pieces = []
  taken = []

  def __init__(self):
    pass

  def update(self,newCoords):
    self.coords = newCoords

  #I will pass coord in as [x,y] so I want to swap them
  def __swap(self,coord):
    return [coord[1],coord[0]]

  def getSquare(self,coord):
    coord = self.__swap(coord)
    return self.coords[coord[0]][coord[1]]
  

  def __setSquare(self,coord,piece):
    coord = self.__swap(coord)
    self.coords[coord[0]][coord[1]] = piece
    self.taken.append(coord)

  def add_piece(self,piece):
    self.pieces.append(piece)
    self.__setSquare(piece.position,piece)

  def __replace_taken(self,old,new):
    for i,item in enumerate(self.taken):
      if item[0] == old[0] and item[1] == old[1]:
        self.taken[i] = new
        

  def movePiece(self,source_coord,destination_coord,piece):
    source_coord = self.__swap(source_coord)
    destination_coord = self.__swap(destination_coord)
    if self.coords[source_coord[0]][source_coord[1]]:
      self.coords[source_coord[0]][source_coord[1]] = 0
      self.coords[destination_coord[0]][destination_coord[1]] = piece
      self.__replace_taken(source_coord,destination_coord)
    
  def print(self):
     print("  | 0  1  2  3  4  5  6  7\n__|________________________")
     for i in range(8):
      string = "%d |" % i
      for j in range(8):
        if self.coords[i][j]:
          string += " "+ self.coords[i][j].getCode() + " "
        else:
          string += " X "
    
      print(string) 
     print()

  def nearby_pieces(self,coord,offset=1):
    coord = self.__swap(coord)
    
    #Coordinates that fit in x range
    nearby = [[x[0],x[1]] for x in self.taken if x[1] <= coord[1] + 
    offset and x[1] >= coord[1] - offset]
    #Coordinates that fit in x and y range
    nearby = [[x[0],x[1]] for x in nearby if x[0] <= coord[0] + offset and x[0] >= coord[0] - offset]
    
    #Get rid of it's own coordinate
    nearby = [x for x in nearby if x != coord]

    #Swap the coords
    nearby = [self.__swap(x) for x in nearby]

    return nearby #Returns coords of nearby pieces
    
    


#Board is 8x8

class Piece:
  def __init__(self,position,color,board,code):
      self.onBoard = False
      self.last_position = [-1,-1]
      self.position = position
      self.color = color
      self.board = board
      self.code = code
      self.__update()


      if self.color == "black":
          self.vecs = b_vecs
      if self.color == "white":
          self.vecs = w_vecs
          
          



  def __update(self):
    if not self.onBoard:
      self.board.add_piece(self)
      self.onBoard = True
    else:
      self.board.movePiece(self.last_position,self.position,self)

  def _vertical_flip(self,cmd="flip_c_pos",tbf=[],vectors=[]):
    if cmd == "flip_c_pos": #Flip current position
      self.position = [self.position[0],7-self.position[1]]
      self.update()
    if cmd == "ret_flipped": #Flip given positions
      flipped = [[x[0],7-x[1]] for x in tbf]
      return flipped
    if cmd == "flip_vectors": #Flip the vertical direction of vectors
      flipped_vectors = [[x[0],x[1] * -1] for x in vectors] 
      return flipped_vectors
   
    

  def move(self):
    #The default move method, this method should be overidden
    self.last_position = self.position
    self.position = [self.position[0],self.position[1] + 1]
    self.__update()

  def getColor(self):
    return self.color

  def getCode(self):
    return self.code

  def __repr__(self):
    return self.code



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

    nearby = self.board.nearby_pieces(self.position)
    
    potential_kills = []
    for coord in nearby:
      
      piece = self.board.getSquare(coord)
      
     
      if piece.color != self.color:
 
        
        tr = numpy.array((1,1))
        tl = numpy.array(self.vecs["top_left"])
        pos = numpy.array(self.position)

       


        if (pos + tr).tolist() == coord or (pos + tl).tolist() == coord:
          potential_kills.append(coord)
    
    
    print(potential_kills)

    
   

    

    return positions

      
    



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
chess_pieces = { 
"w_pawn"  : '\u2659', 
"w_knight" : '\u2658',
"w_rook" : '\u2657' ,
"w_bishop" : '\u2657' ,
"w_queen" : '\u2655' ,
"w_king" : '\u2654',

"b_pawn" : '\u2659',
"b_knight" : '\u265e',
"b_rook" : '\u265c', 
"b_bishop" : '\u265d', 
"b_queen" :  '\u265b' , 
"b_king" : '\u265a'
}

#Just makes checking nearby pieces and all that slightly easier and more readable
w_vecs = {
  "top_right" : [1,1],
  "top_middle" : [0,1],
  "top_left" : [-1,1],
  "middle_left" : [-1,0],
  "middle_middle": [0,0],
  "bottom_left" : [-1,-1],
  "bottom_middle" : [0,-1],
  "bottom right" : [1,-1]
}

b_vecs = {
  "top_right" : [1,1],
  "top_middle" : [0,1],
  "top_left" : [-1,1],
  "middle_left" : [-1,0],
  "middle_middle": [0,0],
  "bottom_left" : [-1,-1],
  "bottom_middle" : [0,-1],
  "bottom right" : [1,-1]
}

"""
  The white chess pieces will be at top coming downwards and the black chess pieces will be coming the oppisite direction so the piece class has a method that has some options where it will vertically flip things


"""


#Main
if __name__ == "__main__":
  
  game = Game()
