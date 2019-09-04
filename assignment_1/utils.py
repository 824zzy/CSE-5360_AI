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
                # TODO: maybe lower case is more convient
                # l = l.lower().split()
                l = l.split()
                if l[0] not in input_dic:
                    input_dic[l[0]] = []
                    input_dic[l[0]].append((l[1], l[2]))
                else:
                    input_dic[l[0]].append((l[1], l[2]))
                
                if l[1] not in input_dic:
                    input_dic[l[1]] = []
                    input_dic[l[1]].append((l[0], l[2]))
                else:
                    input_dic[l[1]].append((l[0], l[2]))
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
                heuristic[l[0]] = l[1]
    return heuristic

if __name__ == "__main__":
    input_d = parse_input('./data/input1.txt')
    print(input_d)

    heuristic = parse_heuristic('./data/h_kassel.txt')
    print(heuristic)
    
