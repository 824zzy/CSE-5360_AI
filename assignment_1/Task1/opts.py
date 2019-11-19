import argparse
import os

def parse_opt():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--data_dir', type=str, default='./data/')
    parser.add_argument('--printLog', action='store_true')
    parser.add_argument('input_filename', nargs='?', type=str, default='input1.txt')
    parser.add_argument('origin_city', nargs='?', type=str, default='Bremen')
    parser.add_argument('destination_city', nargs='?', type=str, default='Kassel')
    parser.add_argument('heuristic_filename', nargs='?', type=str, default='')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    opt = parse_opt()
    assert opt.input_filename == 'input1.txt' 
    assert opt.origin_city == 'Bremen'
    assert opt.destination_city == 'Kassel'
    assert opt.heuristic_filename == 'h_kassel.txt' 