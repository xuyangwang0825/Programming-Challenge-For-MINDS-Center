import argparse
from typing import Optional
from pre_process import pre_process
from compute import compute
from plot import plot

parser = argparse.ArgumentParser(
    description="Welcome to use this sentiment analysis tool!")
parser.add_argument('-o', choices=['a', 'p', 'c', 'o'],
                    help='input the operation type')


args = parser.parse_args()
if args.o:
    # pre-process, compute and plot the result
    if args.o == 'a':
        res = compute()
        plot(res)
    # pre-process the data (from html -> json -> extract necessary messages)
    elif args.o == 'p':
        pre_process()
    # compute the sentiment
    elif args.o == 'c':
        compute()
    # plot the image of sentiment analysis result
    elif args.o == 'o':
        res = compute()
        plot(res)
else:
    print("please input the operation type")
