#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hour_glass_sums = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            current_sum = 0
            current_sum += sum(arr[i][j: j + 3]) + \
                arr[i+1][j+1] + sum(arr[i+2][j: j + 3])
            hour_glass_sums.append(current_sum)

    print(max(hour_glass_sums))
