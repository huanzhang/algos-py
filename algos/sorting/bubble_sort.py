#!/usr/bin/env python

def sort(L):
    for i in range(0, len(L)):
        for j in range(1, len(L)-i):
            if L[j] < L[j-1]:
                L[j-1], L[j] = L[j], L[j-1]

if __name__ == "__main__":
    ar = [int(i) for i in raw_input().strip().split()]
    sort(ar)
    print ' '.join([`x` for x in ar]) 
