#!/usr/bin/env python3
import random
import argparse
import sys

parser = argparse.ArgumentParser("randGenUntil")
parser.add_argument("number", help="Generate a random numbers until they are equal to this.", type=int)
parser.add_argument("-s", "--start", type=int, default=0,
                    help="The range in which the random numbers are in starts with this number. (default 0)")
parser.add_argument("-e", "--end", type=int, default=32767,
                    help="The range in which the random numbers are in ends with this number. (default 32767)")
parser.add_argument("-n", "--newline", help="Adds a newline between random numbers.", action="store_true")


def error(message, exit_code):
    print(message)
    sys.exit(exit_code)


args = parser.parse_args()
if args.start > args.end:
    print("error: start is greater than end")
    sys.exit(1)
if args.number > args.end or args.number < args.start:
    print("error: number is either greater than end or less than start")
    sys.exit(1)
end = ''
end = "\n" if args.newline else "\r"
rand_num = ''
args.end += 1
while rand_num != args.number:
    width = len(str(rand_num))
    rand_num = random.randrange(args.start, args.end)
    print("{rand_num: <{width}}".format(rand_num=rand_num, width=width), end=end)
if end == "\r":
    print()
