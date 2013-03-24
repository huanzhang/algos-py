#!/usr/bin/env python

def sort(L):
    if not L:
        return []
    return sort([x for x in L[1:] if x<L[0]])\
            + L[0:1] + sort([x for x in L[1:]\
            if x>=L[0]])

if __name__ == "__main__":
    ar = [int(i) for i in raw_input().strip().split()]
    ar = sort(ar)
    print ' '.join([`x` for x in ar]) 
