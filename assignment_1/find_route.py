import opts
import heapq
from utils import *
from collections import defaultdict

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

        self.expanded_n = 0
        self.generated_n = 0
        self.max_n = 0
        self.printLog = True

    @staticmethod
    def _getTentativeCost(cities, node):
        for city in cities:
            if city[0] == node:
                return city[1]
        return 0

    def _getCost(self, node, parentCost):
        cost = 0
        # if self.orig != node:
        if parentCost:
            cost = parentCost.g + self._getTentativeCost(self.input[parentCost.city], node)
        return cost
    
    def _getFValue(self, node, parentCost=None):
        heuristic, cost = 0, 0
        if node in self.heuristic:
            heuristic = self.heuristic[node]
        cost = self._getCost(node, parentCost)
        return cost, cost+heuristic

    @staticmethod            
    def _getLeastFvalueNode(opened):
        leastFNode, nodes  = None, opened.elements
        for node in nodes:
            if leastFNode is None:
                leastFNode = node 
            elif leastFNode.f > node.f:
                leastFNode = node
        return leastFNode
    
    def _getNeighbour(self, parent):
        neightbours = self.input[parent.city]
        nodes = {}
        for n in neightbours:
            cost, fValue = self._getFValue(n[0], parent)
            nodes[n[0]] = Node(n[0], cost, n[1], fValue, parent)
        return nodes

    def Search(self):
        # opened, closed = set(), set()
        fringe, closed = Fringe(), []
        cost, fvalue = self._getFValue(self.orig)
        startNode = Node(self.orig, 0, 0, fvalue, None)
        fringe.push(startNode)
        current = startNode
        count = 0

        while fringe:
            # Print log 
            if self.printLog:
                print("Expanding Node: {}".format(self.expanded_n))
                print("Generating successors to {}".format(current.city))
                print("Node Expanded: {}".format(self.expanded_n))
                print("Node Generated: {}".format(self.generated_n))
                print("Max Nodes in Memory: {}".format(self.max_n))
                print("Fringe:")
                print("\t{}".format([(e.city, e.g, e.f) for e in fringe.elements]))
                print("Closed:")
                print("\t{}".format([n.city for n in closed]))
                print("\t{}".format(set([n.city for n in closed])))
                print('----'*4)
            # Generating successors
            current = self._getLeastFvalueNode(fringe)

            if current.city in [e.city for e in closed]:
                self.expanded_n += 1
                fringe.pop(current)
                closed.append(current)
                continue
            
            neighboursNodes = self._getNeighbour(current)

            if current.city==self.dest:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return (path[::-1], self.expanded_n+1, self.generated_n, self.max_n)
            
            fringe.pop(current)
            closed.append(current)

            for nodeName, node in neighboursNodes.items():
                if node not in closed:
                    fringe.push(node)
            
            self.expanded_n += 1
            self.generated_n = (len(fringe.elements)+len(closed)-1)
            self.max_n = max(self.max_n, len(fringe))

        return ([], self.expanded_n, self.generated_n, self.max_n)



if __name__ == "__main__":
    opt = opts.parse_opt()

    task1 = FindRoute(opt.data_dir,
                      opt.input_filename,
                      opt.origin_city,
                      opt.destination_city,
                      opt.heuristic_filename)

    path, expanded, generated, max_nodes = task1.Search()
    paths = [p.city for p in path]
    print(" --> ".join(paths))
    
    distance = sum(map(lambda x: x.c, path))
    print("nodes expanded: {}".format(expanded))
    print("nodes generated: {}".format(generated))
    print("max nodes in memory: {}".format(max_nodes))
    
    if distance and len(path) > 1:
      print("distance: {} km".format(float(distance)))
      print("route:")
      for i in range(len(path) -1):
        print("{} to {}, {} km".format(path[i].city, path[i+1].city, float(path[i+1].c)))
    elif len(path) == 1:
      print("distance: {} km".format(float(distance)))
      print("route:")
      print("{} to {}, {} km".format(path[0].city, path[0].city, float(path[0].c)))
    else:
      print("distance: infinity")
      print("route: none")
    