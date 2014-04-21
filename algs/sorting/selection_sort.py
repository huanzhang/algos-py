#!/usr/bin/env python

def sort(L):
    for i in range(0, len(L)):
        m = i
        for j in range(i+1, len(L)):
            if L[j] < L[m]:
                m = j
        L[i], L[m] = L[m], L[i]

if __name__ == "__main__":
    ar = [int(i) for i in raw_input().strip().split()]
    sort(ar)
    print ' '.join([`x` for x in ar]) 
