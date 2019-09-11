import heapq

class Node:
    def __init__(self, city, g=0, c=0, f=0, parent=None):
        """Description: 
        'Nodes[nbour[0]] = node(nbour[0],cost,nbour[1], fvalue, parent)  
        Args: 
            city: str, the origin city name
	        g: int, g(n), cumulative cost, the cost from the start node to node n
            tc: int, cost of current node to next node
            f: int, f(n), estimated cost of the cheapest solution through n
            parent: node, parent node, just record only parent rather than whole path
        """
        self.city = city
        self.g = g
        self.c = c
        self.f = f
        self.parent = parent

class Fringe:
    def __init__(self):
        self.elements = []
    
    def __len__(self):
        return len(self.elements)
    
    def push(self, item):
        self.elements.append(item)
    
    def pop(self, item):
        self.elements.remove(item)

def parse_input(file):
    """ Parse input file's lines into dictionary
    Args: 
	    file: a str represent the path to input

    Returns: 
	    input_dic: a dictionary where key is origin city name and
                   value is destination ciry and distance.
    """
    
    input_dic = {}
    with open(file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            if l != 'END OF INPUT':
                l = l.split()
                if l[0] not in input_dic:
                    input_dic[l[0]] = []
                    input_dic[l[0]].append((l[1], int(l[2])))
                else:
                    input_dic[l[0]].append((l[1], int(l[2])))
                
                if l[1] not in input_dic:
                    input_dic[l[1]] = []
                    input_dic[l[1]].append((l[0], int(l[2])))
                else:
                    input_dic[l[1]].append((l[0], int(l[2])))
    return input_dic

def parse_heuristic(file):
    """ Parse heuristic file lines into dictionary
    Args: 
	    file: a str represent the path to input
    Returns: 
	    heuristic: a dictionary where key is city name and \
                   value is actual cost to reach destination
    """
    
    heuristic = {}
    with open(file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            if l != 'END OF INPUT':
                # TODO: maybe lower case is more convient
                # l = l.lower().split()
                l = l.split()
                heuristic[l[0]] = int(l[1])
    return heuristic


if __name__ == "__main__":
    input_d = parse_input('./data/input1.txt')
    print(input_d)

    heuristic = parse_heuristic('./data/h_kassel.txt')
    print(heuristic)
    
