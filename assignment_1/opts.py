import argparse
import os

def parse_opt():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--input_filename', type=str, default='./data/input1.txt')
    parser.add_argument('--origin_city', type=str, default='Bremen')
    parser.add_argument('--destination_city', type=str, default='Kassel')
    parser.add_argument('--heuristic_filename', type=str, default='./data/h_kassel.txt')
    
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    opt = parse_opt()
    assert opt.input_filename == './data/input1.txt' 
    assert opt.origin_city == 'Bremen'
    assert opt.destination_city == 'Kassel'
    assert opt.heuristic_filename == './data/h_kassel.txt' 