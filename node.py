class Node:

  def __init__(self,id,x,y):
    self.id = id
    self.x = x
    self.y = y
    self.predecessor = None
    self.successor = None

  def print_node(self,id):
    print "Node:", self.id, "coordinates: (",self.x, ",",self.y,")"


n1 =Node(1,13,10)
n1.print_node(1)