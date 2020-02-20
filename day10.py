#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = bin(int(input()))[2:].split('0')
    print(max([len(item) for item in n]))
