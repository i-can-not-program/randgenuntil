#!/usr/bin/env python3
import random
import argparse
import sys


def error(message):
    print(message)
    sys.exit(1)


parser = argparse.ArgumentParser()
parser.add_argument("number",
                    help="Generate a random numbers until they are equal to this.", type=int)
parser.add_argument("-s", "--start", type=int, default=0,
                    help="The range in which the random numbers are in starts with this number. (default 0)")
parser.add_argument("-e", "--end", type=int, default=32767,
                    help="The range in which the random numbers are in ends with this number. (default 32767)")
parser.add_argument("-c", "--count",
                    help="Counts the amount of tries it takes to get to the number.", action="store_true")
parser.add_argument("-n", "--newline",
                    help="Adds a newline between random numbers.", action="store_true")

args = parser.parse_args()
if args.start > args.end:
    error("error: start is greater than end")
if args.number > args.end or args.number < args.start:
    error("error: number is either greater than end or less than start")
end = "\n" if args.newline else "\r"
rand_num = ''
tries = 0
args.end += 1
while rand_num != args.number:
    width = len(str(rand_num))
    rand_num = random.randrange(args.start, args.end)
    print("{rand_num: <{width}}".format(rand_num=rand_num, width=width), end=end)
    tries += 1
if args.count:
    print("{} tries to get to {}".format(tries, args.number))
elif end == "\r":
    print()

