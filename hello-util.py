#!/usr/bin/python3

import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    print(args.name)

if __name__ == '__main__':
    main()
