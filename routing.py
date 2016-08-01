import csv
import os.path
import random
import sys


# print "number of args: ", len(sys.argv), ' arguments'
# print "list of args: ", str(sys.argv)
class Node:

    nodes = {}

    def __init__(self,id,x,y):
        self.id = id
        self.x = x
        self.y = y
        self.predecessor = None
        self.successor = None

    def print_node(self,id):
        print "Node:", self.id, "coordinates: (",self.x, ",",self.y,")"


def read_file():
    if ( len(sys.argv) == 2 ):
        filename = "maps/"+sys.argv[1]
    else:
        print "usage: $ python routing.py <filename>"
        quit()

    if (os.path.isfile(filename)):
        print "within os.path"
        with open(filename,"rb") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # skip headers
            for row in reader:
                print row
                capture_line(row)
    else:
        print "file not found.... exiting now"
        exit()

def capture_line(input):
    print "capturing line!"
    n = Node(input[0], input[1], input[2])
    n.nodes[input[0]] = [input[1], input[2]]
    n.print_node(input[0])

# define Node data structure




# main program
if __name__ == '__main__':
    read_file()
    print Node.nodes
    nodes_size = len(Node.nodes)
    keys = list(Node.nodes)
    random.shuffle(keys)
    print "keys"
    print keys
    print "Order number Node"
    for k, val in enumerate(keys):
        print k+1, "\t", val
