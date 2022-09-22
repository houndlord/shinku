import argparse
import utils.walk
import utils.log
import time

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="path to directory you want to replicate")
    parser.add_argument("dst", help="path to directory where replica will be stored")
    parser.add_argument("log_path", help="path to log file.")
    parser.add_argument("interval", help="sync interval in seconds")
    args = parser.parse_args()
    return args.src, args.dst, args.log_path, args.interval

def replicate(src, dst, log_path):
    utils.log.log(log_path, 'init')
    utils.walk.walk(src, dst, log_path)
    utils.walk.backwalk(src, dst, log_path)

def main():
    src, dst, log_path, interval = parse()
    while True:
        replicate(src, dst, log_path)
        time.sleep(int(interval))

if __name__ == '__main__':
    main()