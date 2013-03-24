import unittest
import random
import logging
from algos.sorting import insertion_sort,\
        quick_sort, merge_sort, bubble_sort

class TestInsertionSort(unittest.TestCase):
    def test_sort(self):
        input = range(1000)
        random.shuffle(input)
        insertion_sort.sort(input)
        self.assertEqual(range(1000), input)

    def test_sort_empty_list(self):
        input = range(0)
        insertion_sort.sort(input)
        self.assertEqual(range(0), input)

    def test_sort_one_element_list(self):
        input = range(1)
        insertion_sort.sort(input)
        self.assertEqual(range(1), input)

    def test_sort_two_elements_list(self):
        input = range(2)
        random.shuffle(input)
        insertion_sort.sort(input)
        self.assertEqual(range(2), input)

    def test_sort_inverted_list(self):
        input = range(1000)
        input.reverse()
        insertion_sort.sort(input)
        self.assertEqual(range(1000), input)

class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
        input = range(1000)
        random.shuffle(input)
        bubble_sort.sort(input)
        self.assertEqual(range(1000), input)

    def test_sort_empty_list(self):
        input = range(0)
        bubble_sort.sort(input)
        self.assertEqual(range(0), input)

    def test_sort_one_element_list(self):
        input = range(1)
        bubble_sort.sort(input)
        self.assertEqual(range(1), input)

    def test_sort_two_elements_list(self):
        input = range(2)
        random.shuffle(input)
        bubble_sort.sort(input)
        self.assertEqual(range(2), input)

    def test_sort_inverted_list(self):
        input = range(1000)
        input.reverse()
        bubble_sort.sort(input)
        self.assertEqual(range(1000), input)


class TestQuickSort(unittest.TestCase):
    def test_sort(self):
        input = range(100)
        random.shuffle(input)
        output = quick_sort.sort(input)
        self.assertEqual(range(100), output)

    def test_sort_empty_list(self):
        input = range(0)
        output = quick_sort.sort(input)
        self.assertEqual(range(0), output)

    def test_sort_one_element_list(self):
        input = range(1)
        output = quick_sort.sort(input)
        self.assertEqual(range(1), output)

    def test_sort_two_elements_list(self):
        input = range(2)
        random.shuffle(input)
        output = quick_sort.sort(input)
        self.assertEqual(range(2), output)

    def test_sort_inverted_list(self):
        input = range(100)
        input.reverse()
        output = quick_sort.sort(input)
        self.assertEqual(range(100), output)

class TestMergeSort(unittest.TestCase):
    def test_sort(self):
        input = range(100)
        random.shuffle(input)
        output = merge_sort.sort(input)
        self.assertEqual(range(100), output)

    def test_sort_empty_list(self):
        input = range(0)
        output = merge_sort.sort(input)
        self.assertEqual(range(0), output)

    def test_sort_one_element_list(self):
        input = range(1)
        output = merge_sort.sort(input)
        self.assertEqual(range(1), output)

    def test_sort_two_elements_list(self):
        input = range(2)
        random.shuffle(input)
        output = merge_sort.sort(input)
        self.assertEqual(range(2), output)

    def test_sort_inverted_list(self):
        input = range(100)
        input.reverse()
        output = merge_sort.sort(input)
        self.assertEqual(range(100), output)
