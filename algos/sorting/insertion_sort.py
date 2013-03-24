#!/usr/bin/env python

def sort(L):
    for i in range(1, len(L)):
        j = i - 1
        v = L[i]
        while j >= 0 and v < L[j]:
            L[j+1] = L[j]
            j = j - 1
        L[j+1] = v


if __name__ == "__main__":
    ar = [int(i) for i in raw_input().strip().split()]
    insertionSort(ar)
    print ' '.join([`num` for num in ar])
