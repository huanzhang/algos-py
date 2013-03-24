#!/usr/bin/env python

def merge(l1, l2):
    L = []
    while l1 and l2:
        if l1[0] < l2[0]:
            L.append(l1.pop(0))
        else:
            L.append(l2.pop(0))
    return L + l1 + l2

def sort(L):
    mid = len(L)/2
    if len(L) <= 1: return L
    return merge(sort(L[0:mid]), sort(L[mid:]))


if __name__ == "__main__":
    ar = [int(i) for i in raw_input().strip().split()]
    ar = sort(ar)
    print ' '.join([`x` for x in ar]) 
