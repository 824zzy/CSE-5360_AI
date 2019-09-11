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
    def __init__(self, data_dir, input_f, heuristic_f=None, printLog=False):
        self.data_dir = data_dir
        self.input = parse_input(self.data_dir+input_f)
        self.heuristic = parse_heuristic(self.data_dir+heuristic_f) if heuristic_f else []
        
        self.fringe = Fringe()
        self.closed = []
        self.path = []
        
        self.expanded_n = 0
        self.generated_n = 0
        self.max_n = 0
        self.printLog = printLog

    @staticmethod
    def _getTargetCost(cities, node):
        for city in cities:
            if city[0] == node:
                return city[1]
        return 0

    def _getCost(self, node, parent):
        cost = 0
        if parent:
            cost = parent.g + self._getTargetCost(self.input[parent.city], node)
        return cost
    
    def _getFValue(self, node, parent=None):
        heuristic, cost = 0, 0
        if node in self.heuristic:
            heuristic = self.heuristic[node]
        cost = self._getCost(node, parent)
        return cost, cost+heuristic
           
    def _getNode(self):
        leastFNode = None
        for node in self.fringe.elements:
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
    
    def _print(self, current=None, mode='F', succeed=True, skip=False):
        if mode=='F':
            if self.heuristic:
                print("Informed Search selected")
            else:
                print("Uninformed Search selected")
            print("Node Expanded: {}".format(self.expanded_n))
            print("Node Generated: {}".format(self.generated_n))
            print("Max Nodes in Memory: {}".format(self.max_n))
            print("Fringe:")
            print("\t{}".format([(e.city, e.g, e.f) for e in self.fringe.elements]))
            print("Closed:")
            print("\t{}\n".format(set([n.city for n in self.closed])))
        elif mode=='C':
            print("Expanding Node: {}".format(self.expanded_n))
            if not skip:
                print("Generating successors to {}".format(current.city))
            else:
                print("{} is already in closed. No successors".format(current.city))
            print("Node Expanded: {}".format(self.expanded_n))
            print("Node Generated: {}".format(self.generated_n))
            print("Max Nodes in Memory: {}".format(self.max_n))
            print("Fringe:")
            print("\t{}".format([(e.city, e.g, e.f) for e in self.fringe.elements]))
            print("Closed:")
            print("\t{}".format(set([n.city for n in self.closed])))
            print('----'*4)
        elif mode=='R':
            self.path = self.path[::-1]
            distance = sum(map(lambda x: x.c, self.path))
            if succeed:
                print("nodes expanded: {}".format(self.expanded_n+1))
            else:
                print("nodes expanded: {}".format(self.expanded_n))
            print("nodes generated: {}".format(self.generated_n))
            print("max nodes in memory: {}".format(self.max_n))
            
            if distance and len(self.path)>1:
                print("distance: {} km".format(float(distance)))
                print("route:")
                for i in range(len(self.path)-1):
                    print("{} to {}, {} km".format(self.path[i].city, self.path[i+1].city, float(self.path[i+1].c)))
            elif len(self.path)==1:
                print("distance: {} km".format(float(distance)))
                print("route:")
                print("{} to {}, {} km".format(self.path[0].city, self.path[0].city, float(self.path[0].c)))
            else:
                print("distance: infinity")
                print("route: none")


    def Search(self, origin, destination):
        cost, fvalue = self._getFValue(origin)
        startNode = Node(origin, 0, 0, fvalue, None)
        self.fringe.push(startNode)
        current = startNode
        count = 0

        if self.printLog:
            self._print(current, 'F')
        
        while self.fringe:    
            current = self._getNode()
            if current.city in [e.city for e in self.closed]:
                self.expanded_n += 1
                if self.printLog:
                    self._print(current, 'C', skip=True)
                self.fringe.pop(current)
                self.closed.append(current)
                continue
            
            neighboursNodes = self._getNeighbour(current)

            if current.city==destination:
                while current.parent:
                    self.path.append(current)
                    current = current.parent
                self.path.append(current)
                return True
            
            self.fringe.pop(current)
            self.closed.append(current)

            for nodeName, node in neighboursNodes.items():
                if node not in self.closed:
                    self.fringe.push(node)
            
            self.expanded_n += 1
            self.generated_n = (len(self.fringe.elements)+len(self.closed)-1)
            self.max_n = max(self.max_n, len(self.fringe))
            # Print log 
            if self.printLog:
                self._print(current, 'C')

        return False


if __name__ == "__main__":
    opt = opts.parse_opt()
    task1 = FindRoute(opt.data_dir,
                      opt.input_filename,
                      opt.heuristic_filename,
                      opt.printLog)

    isSucceed = task1.Search(opt.origin_city, opt.destination_city)
    task1._print(None, 'R', succeed=isSucceed)