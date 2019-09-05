import argparse
import os

def parse_opt():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--data_dir', type=str, default='./data/')
    parser.add_argument('--input_filename', type=str, default='input1.txt')
    parser.add_argument('--origin_city', type=str, default='Bremen')
    parser.add_argument('--destination_city', type=str, default='Kassel')
    # default heuristic suppose to be h_kassel.txt.
    parser.add_argument('--heuristic_filename', type=str, default='')
    
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    opt = parse_opt()
    assert opt.input_filename == 'input1.txt' 
    assert opt.origin_city == 'Bremen'
    assert opt.destination_city == 'Kassel'
    assert opt.heuristic_filename == 'h_kassel.txt' 