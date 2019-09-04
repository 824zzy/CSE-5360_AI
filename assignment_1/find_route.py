import opts
import utils

class FindRoute:
    def __init__(self, input_f, orig, dest, heuristic_f=None):
        self.input = utils.parse_input(input_f)
        self.orig = orig
        self.dest = dest
        
        if heuristic_f:
            self.heuristic = utils.parse_heuristic(heuristic_f)



if __name__ == "__main__":
    opt = opts.parse_opt()

    solution = FindRoute(opt.input_filename,
                         opt.origin_city,
                         opt.destination_city,
                         opt.heuristic_filename)
    print(solution.input, solution.heuristic)
    