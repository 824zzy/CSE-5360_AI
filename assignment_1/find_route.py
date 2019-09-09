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
        self.heuristic = parse_heuristic(self.data_dir+heuristic_f) if heuristic_f else []

    @staticmethod
    def _getTentativeCost(cities, node):
        for city in cities:
            if city[0] == node:
                return city[1]
        return 0

    def _getCost(self, node, parentCost):
        cost = 0
        if self.orig != node:
            cost = parentCost.g + self._getTentativeCost(self.input[parentCost.city], node)
        return cost
    
    def _getFValue(self, node, parentCost=None):
        heuristic, cost = 0, 0
        if node in self.heuristic:
            heuristic = self.heuristic[node]
        if self.orig != node:
            cost = self._getCost(node, parentCost)
        return (cost, cost+heuristic)

    @staticmethod            
    def _getLeastFvalueNode(nodes):
        leastFNode = None
        for node in nodes:
            if leastFNode is None:
                leastFNode = node 
            elif leastFNode.f > node.f:
                leastFNode = node
        return leastFNode
    
    def _getNeighbour(self, node):
        return self.input[node.city]

    def _generateNodes(self, neighbours, parent):
        nodes = {}
        for n in neighbours:
            cost, fvalue = self._getFValue(n[0], parent)
            nodes[n[0]] = Node(n[0], cost, n[1], fvalue, parent)
        return nodes

    def Search(self):
        opened, closed = set(), set()
        expanded, maxNode = 1, 1
        fvalue = self._getFValue(self.orig)
        startNode = Node(self.orig, 0, 0, fvalue[1], None)
        opened.add(startNode)
        current = self.orig

        while opened:
            current = self._getLeastFvalueNode(opened)        
            neighbours = self._getNeighbour(current)
            neighboursNodes = self._generateNodes(neighbours, current)

            if current.city==self.dest:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return (path[::-1], expanded)
            
            opened.remove(current)
            closed.add(current)

            for nodes in neighboursNodes:
                if neighboursNodes[nodes] in closed:
                    continue
                if nodes not in [cities.city for cities in closed]:
                    if neighboursNodes[nodes] not in opened and nodes != self.orig:
                        opened.add(neighboursNodes[nodes])
            expanded += 1

        return ([], expanded)



if __name__ == "__main__":
    opt = opts.parse_opt()

    task1 = FindRoute(opt.data_dir,
                      opt.input_filename,
                      opt.origin_city,
                      opt.destination_city,
                      opt.heuristic_filename)
    print(task1.heuristic)
    path, expanded = task1.Search()
    paths = [p.city for p in path]
    print(" --> ".join(paths))
    
    distance = sum(map(lambda x: x.tc, path))
    print("nodes expanded: {}".format(expanded))
    
    if distance and len(path) > 1:
      print("distance: {} km".format(float(distance)))
      print("route:")
      for i in range(len(path) -1):
        print("{} to {}, {} km".format(path[i].city, path[i+1].city, float(path[i+1].tc)))
    elif len(path) == 1:
      print("distance: {} km".format(float(distance)))
      print("route:")
      print("{} to {}, {} km".format(path[0].city, path[0].city, float(path[0].tc)))
    else:
      print("distance: infinity")
      print("route: none")
    