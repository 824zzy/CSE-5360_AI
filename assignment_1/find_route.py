import opts
import heapq
from utils import *

class FindRoute:
    """Description
    Args: 
	    arg: explanation
    Returns: 
	    The return values of *.
    """
    def __init__(self, data_dir, input_f, orig, dest, heuristic_f=None):
        self.data_dir = data_dir
        self.input = parse_input(self.data_dir+input_f)
        self.orig = orig
        self.dest = dest
        
        if heuristic_f:
            self.heuristic = parse_heuristic(heuristic_f)

    def _getTentativeCost(cities, node):
        for city in cities:
            if city[0] == node:
                return city[1]
        return 0

    def _getCost(self, city, parentCost):
        cost = 0
        if self.orig != city:
            cost = parentCost.g + self._getTentativeCost(self.input[parentCost.city], city)
        return cost
    
    def _getFValue(self, city, parentCost=None):
        heuristic, cost = 0, 0
        if city in self.heuristic:
            heuristic = self.heuristic[city]
        if self.orig != city:
            cost = self._getCost(city, parentCost)
        return (cost, cost+heuristic)
            

    def _getLeastFvalueNode(nodes):
        leastFNode = None
        for node in nodes:
            if leastFNode is None:
                leastFNode = node 
            elif leastFNode.f > node.f:
                leastFNode = node
        return leastFNode
    
    def _getNeighbor(self, node):
        return self.input[node.city]

    def _generateNodes(self, neighbors, parent):
        nodes = {}
        for n in neighbors:
            cost, fvalue = self.getFValue(n[0], parent)
            nodes[n[0]] = Node(city=n[0], g=cost, f=n[1], tc=fvalue, parent=parent)
        return nodes

    
    def uninformSearch():
        pass


    def informSearch(self):
        opened, closed, expaned = set(), set(), 1
        fvalue = getFValue(self.orig)
        startNode = node(self.orig, 0, 0, fvalue[1], parent=None)
        opened.add(startNode)
        current = self.orig

        while opened:
            current = self._getLeastFvalueNode(opened)        
            neighbors = self._getNeighbor(current)
            neighborsNodes = self._generateNodes(neighbors, current)

            if current.city==self.dest:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return (path[::-1], expanded)
            
            opened.remove(current)
            closed.add(current)

            for nodes in neighbors:
                if neighborsNodes[Node]


        return ([], expanded)



if __name__ == "__main__":
    opt = opts.parse_opt()

    task1 = FindRoute(opt.data_dir,
                      opt.input_filename,
                      opt.origin_city,
                      opt.destination_city,
                      opt.heuristic_filename)
    print(task1.input)
    exit()
    if not opt.heuristic:
        path, expanded = task1.uninformSearch()
    else:
        path, expanded = task1.informSearch()
    