#/usr/bin/env python

def search(L,k):
    """Search item from turned array
    like [6, 7, 8, 9, 1, 2, 3, 4, 5]
    """
    lo = 0
    hi = len(L) - 1
    while(lo <= hi):
        mid = lo + (hi-lo)/2
        if(L[hi] >= L[lo]):
            if(L[mid] < k):
                lo = mid + 1
            elif(L[mid] > k):
                hi = mid - 1
            else:
                return mid
        else:
            if(L[mid] >= L[lo]):
                if (L[mid] < k):
                    lo = mid + 1
                elif(L[mid] > k):
                    if(L[lo] <= k):
                        hi = mid -1
                    else:
                        lo = mid + 1
                else:
                    return mid
            else:
                if (L[mid] > k):
                    lo = mid + 1
                elif(L[mid] < k):
                    if(L[hi] >= k):
                        lo = mid + 1
                    else:
                        hi = mid - 1
                else:
                    return mid
    return -1

