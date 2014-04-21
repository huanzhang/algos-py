#!/usr/bin/env python2.7

import sys

class SSD(object):
    """
       --   --        --   --   --   --   --   --  
    |    |    | |  | |    |       | |  | |  | |  | 
    |    |    | |  | |    |       | |  | |  | |  | 
       --   --   --   --   --        --   --       
    | |       |    |    | |  |    | |  |    | |  | 
    | |       |    |    | |  |    | |  |    | |  | 
       --   --        --   --        --   --   --  
    ----------------
    |      A       |
    ----------------
    |   |      |   |
    | F |      | B |
    |   |      |   |
    ----------------
    |      G       |      s = the size of number
    ----------------
    |   |      |   |
    | E |      | C |
    |   |      |   |
    ----------------
    |      D       |
    ----------------

    Examples
    --------
    Create an SSD instance
    >>> ssd = SSD()
    Get zero with size = 2
    >>> ssd[0](2)
    Get nigh with size = 5
    >>> ssd[9](5)
    """
    def __init__(self):
        self._num = {
            0: self.__zero,
            1: self.__one,
            2: self.__two,
            3: self.__three,
            4: self.__four,
            5: self.__five,
            6: self.__six,
            7: self.__seven,
            8: self.__eight,
            9: self.__nigh,
        }

    def __getitem__(self, n):
        return self._num[n]

    @staticmethod
    def __getA(s):
        return [" " + "-" * s + " "]

    @staticmethod
    def __getB(s):
        rows = []
        for _ in range(s):
            rows.append(" " * (1 + s) + "|")
        return rows

    @staticmethod
    def __getC(s):
        return SSD.__getB(s)

    @staticmethod
    def __getD(s):
        return SSD.__getA(s)

    @staticmethod
    def __getE(s):
        rows = []
        for _ in range(s):
            rows.append("|" + " " * (1 + s))
        return rows

    @staticmethod
    def __getF(s):
        return SSD.__getE(s)

    @staticmethod
    def __getG(s):
        return SSD.__getA(s)

    @staticmethod
    def __getFB(s):
        rows = []
        for _ in range(s):
            rows.append("|" + " " * s + "|")
        return rows

    @staticmethod
    def __getEC(s):
        return SSD.__getFB(s)

    @staticmethod
    def __getBlank(s):
        return [" " * (2 + s)]

    def __zero(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getFB(s))
        rows.extend(self.__getBlank(s))
        rows.extend(self.__getEC(s))
        rows.extend(self.__getD(s))
        return rows

    def __one(self, s):
        rows = []
        rows.extend(self.__getBlank(s))
        rows.extend(self.__getB(s))
        rows.extend(self.__getBlank(s))
        rows.extend(self.__getC(s))
        rows.extend(self.__getBlank(s))
        return rows

    def __two(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getB(s))
        rows.extend(self.__getG(s))
        rows.extend(self.__getE(s))
        rows.extend(self.__getD(s))
        return rows

    def __three(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getB(s))
        rows.extend(self.__getG(s))
        rows.extend(self.__getC(s))
        rows.extend(self.__getD(s))
        return rows

    def __four(self, s):
        rows = []
        rows.extend(self.__getBlank(s))
        rows.extend(self.__getFB(s))
        rows.extend(self.__getG(s))
        rows.extend(self.__getC(s))
        rows.extend(self.__getBlank(s))
        return rows

    def __five(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getF(s))
        rows.extend(self.__getG(s))
        rows.extend(self.__getC(s))
        rows.extend(self.__getD(s))
        return rows

    def __six(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getF(s))
        rows.extend(self.__getG(s))
        rows.extend(self.__getEC(s))
        rows.extend(self.__getD(s))
        return rows

    def __seven(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getB(s))
        rows.extend(self.__getBlank(s))
        rows.extend(self.__getC(s))
        rows.extend(self.__getBlank(s))
        return rows

    def __eight(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getFB(s))
        rows.extend(self.__getG(s))
        rows.extend(self.__getEC(s))
        rows.extend(self.__getD(s))
        return rows

    def __nigh(self, s):
        rows = []
        rows.extend(self.__getA(s))
        rows.extend(self.__getFB(s))
        rows.extend(self.__getG(s))
        rows.extend(self.__getC(s))
        rows.extend(self.__getD(s))
        return rows

if __name__ == "__main__":
    ssd = SSD()
    inputs = sys.stdin.readlines()
    for input in inputs:
        s,N = input.strip().split()
        printable = []
        for n in N:
            if printable:
                for i in range(len(printable)):
                    printable[i] = " ".join([printable[i], ssd[int(n)](int(s))[i]])
            else:
                printable.extend(ssd[int(n)](int(s)))
        for p in printable:
            print p
