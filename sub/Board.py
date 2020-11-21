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
    
    