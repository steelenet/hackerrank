#!/bin/python3

import os
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks, pairs = Counter(map(int, ar)), 0
    for s in socks: pairs += socks[s]//2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
