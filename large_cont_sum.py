# coding=utf-8
"""
Largest Continuous Sum
Problem
Given an array of integers (positive and negative)
find the largest continuous sum.
"""
from nose.tools import assert_equal


def large_cont_sum(arr):
    """
    :param arr: array of integers
    :return: largest continuous sum
    """
    if len(arr) == 0:
        return 0
    else:
        cur_sum = arr[0]
        large_sum = arr[0]
        for num in arr[1:]:
            cur_sum = max(cur_sum + num, num)
            large_sum = max(cur_sum, large_sum)
        return large_sum


print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))


class LargeContTest(object):
    """
    Test class
    """

    @staticmethod
    def test(sol):
        """
        :param sol: function to be tested 
        :return: nothing
        """
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(large_cont_sum)
