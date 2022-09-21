import argparse
#from consistency_check import generate_files_tree
import utils.walk

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="path to directory you want to replicate")
    parser.add_argument("dst", help="path to directory where replica will be stored")
    parser.add_argument("log_path", help="path to log file.")
    parser.add_argument("interval", help="sync interval in seconds")
    args = parser.parse_args()
    #print(args.src)
    #parser.parse_args()
    utils.walk.walk(args.src, args.dst, args.log_path)
    utils.walk.backwalk(args.src, args.dst, args.log_path)


if __name__ == '__main__':
    main()