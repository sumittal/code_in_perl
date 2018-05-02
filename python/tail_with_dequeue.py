
import  argparse
from collections import deque

def tail(path, lines_to_print=5):
    if lines_to_print < 1:
        return
    d = deque(open(path), lines_to_print)
    for line in d:
        print(line.rstrip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The path to the file to tail')
    parser.add_argument('-n', help='Print the last n lines of the file', type=int, default=5)
    args = parser.parse_args()
    tail(args.path, args.n)
