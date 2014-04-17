#!/usr/bin/env python

def search(L, k):
    lo = 0
    hi = len(L) - 1
    while(lo <= hi):
        mid = lo + (hi - lo)/2
        if(L[mid] > k):
            hi = mid - 1
        elif(L[mid] < k):
            lo = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    ar = [int(i) for i in raw_input().strip().split()]
    k = int(raw_input())
    r = search(ar, k)
    print r
