from classes.Piece import b_vecs



"""
Outside of the board class the coordinates on the board are seen as horizontal
being x and vertical being y but the board is a 2D array so when assigning
something in it you would do eg. item[vertical][horizontal]. This annoys me so in the board class I have a swap method which is called whenever a coordinate is taken in from outside or being outputted. Remember to use the swap method in public methods when dealing with coordinates
"""

class Board:
  
  diagonal_vectors = [b_vecs["top_right"],b_vecs["bottom_right"],b_vecs["top_left"],b_vecs["top_right"]]

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

  def __init__(self,player1,player2):
    self.player1 = player1
    self.player2 = player2
    

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
      
      if self.coords[destination_coord[0]][destination_coord[1]]:
        self.__killPiece([destination_coord[0],destination_coord[1]])
      
      self.coords[source_coord[0]][source_coord[1]] = 0
      self.coords[destination_coord[0]][destination_coord[1]] = piece
      self.__replace_taken(source_coord,destination_coord)
    
    
  def __killPiece(self,coord):
    p = self.coords[coord[0]][coord[1]]
    self.taken.remove(coord)
    self.pieces.remove(p)

    print("\n%s piece at coordinate [%d,%d] was killed!\n" % (p.color,coord[1],coord[0]))
    if p.color == "white":
      self.player1.pieces.remove(p)
    else:
      self.player2.pieces.remove(p)
   
   


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

  def filter(self,coords):
    coords = [ x for x in coords if (x[0] >= 0 and x[0] <= 7) and (x[1] >= 0 and x[1] <= 7)]

    return coords

  def _check_valid(self,coord):
    if coord[0] > 7 or coord[1] < 0 or coord[1] > 7 or coord[1] < 0:
      return False
    else:
      return True

#Check if any of the points could lead to friendly fire (killing your own piece)
  def query_friendly_fire(self,piece,coordinates):
    new_coords = []
    for coord in coordinates:
      c = self.__swap(coord)

      if self.coords[c[0]][c[1]]:
        p = self.coords[c[0]][c[1]]
        if p.color == piece.color:
          continue
      new_coords.append(coord)
    return new_coords


  def _depth_filter(self,piece,vecs,offset=-1,kill=True):
    coord = self.__swap(piece.position)
    arr=[]    
    for d in vecs:
        y = coord[0] + d[0]
        x = coord[1] + d[1]
        temp = []
        f = offset

        while y <= 7 and y >= 0 and x <= 7 and x >= 0 and f != 0:
          if self.coords[y][x]:
            c = self.coords[y][x]
            if c.color == piece.color or (not kill):
              break
            else:
              temp.append([y,x])
          arr.append(self.__swap([y,x]))
          if len(temp) > 0:
            break
          
          f = f-1 if f != -1 else f
          
          y += d[0]
          x += d[1]

    return arr

  def diagonal_to(self,piece, offset=-1):
    diagonal_coords = []

    diagonal_vecs = [[1,1],[-1,1],[1,-1],[-1,-1]]

    diagonal_coords = self._depth_filter(piece,diagonal_vecs,offset)

    return diagonal_coords
        
  def get_horizontal_and_vertical(self,piece,offset=-1):
    coord = self.__swap(piece.position)
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    possible_coords = self._depth_filter(piece,directions,offset)

    return possible_coords

  def get_with_vecs(self,piece,vecs,offset=-1,kill=True):
    flipped_vecs = [self.__swap(x) for x in vecs]
    arr = self._depth_filter(piece,flipped_vecs,offset,kill)
    return arr

#For the knight
  def get_l(self,piece):
    coord = self.__swap(piece.position)
    l_vecs = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    possible_positions = []

    y = coord[0]
    x = coord[1]
    for vec in l_vecs:
        y = coord[0] + vec[0]
        x = coord[1] + vec[1]
        if not self._check_valid([y,x]):
          continue
        if self.coords[y][x]:
          c = self.coords[y][x]
          if c.color == piece.color:
            continue
        possible_positions.append(self.__swap([y,x]))
    
    return possible_positions
 
  def king_in_check(self,king_pos,pieces):
    for p in pieces:
      possible_positions = p.possible_positions()

      
      if king_pos in possible_positions: 
        return True
    return False

  def check_checkmate(self,king_piece,pieces):
    #is king currently in check
    if not self.king_in_check(king_piece.position,pieces):    
      return False
    #Can king escape check by itself 
    king_positions = king_piece.possible_positions()
    for k_pos in king_positions:
      if not self.king_in_check(k_pos,pieces):
        return False
    #Can other pieces get the king out of check
    dangerous_pieces = [x for x in pieces if king_piece.position in pieces.possible_positions()]
    this_player_pieces = [x for x in self.pieces if x.color == king_piece.color]
    for d_p in dangerous_pieces:
      if king_in_check(d_p,this_player_pieces):
        dangerous_pieces.remove(d_p)
    if len(dangerous_pieces) > 0:
      return True
    else:
      return False
