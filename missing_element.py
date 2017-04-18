# coding=utf-8
"""
Find the missing element
"""
from nose.tools import assert_equal


class TestFinder(object):
    """
    Test Class
    """

    def test(self, sol):
        """
        
        :param sol: 
        :return: 
        """
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1],
                         [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print("PASS")


def finder(arr1, arr2):
    """
    :param arr1: original array
    :param arr2: shuffled array with random element missing
    :return: missing element
    """
    arr1.sort()
    arr2.sort()
    idx = 0
    while arr1[idx] == arr2[idx]:
        idx += 1
    return arr1[idx]

t = TestFinder()
t.test(finder)
