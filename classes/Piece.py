import numpy

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
   
  def moveTo(self,coord):
    self.last_position = self.position
    self.position = coord
    self.__update()

  def getColor(self):
    return self.color

  def getCode(self):
    return self.code

  def __repr__(self):
    return self.code

      
chess_pieces = { 
"w_pawn"  : '\u2659', 
"w_knight" : '\u2658',
"w_rook" : '\u2656' ,
"w_bishop" : '\u2657' ,
"w_queen" : '\u2655' ,
"w_king" : '\u2654',

"b_pawn" : '\u265f',
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
  "top_right" : [1,-1],
  "top_middle" : [0,-1],
  "top_left" : [-1,-1],
  "middle_left" : [-1,0],
  "middle_middle": [0,0],
  "bottom_left" : [-1,1],
  "bottom_middle" : [0,1],
  "bottom_right" : [1,1]
}
