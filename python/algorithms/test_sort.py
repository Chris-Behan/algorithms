from algorithms import sort
import pytest


@pytest.mark.parametrize("nums,expected", [([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
                                           ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
                                           ([1, 3, 4, 5, 2], [1, 2, 3, 4, 5]),
                                           ([], [])])
def test_quicksort(nums, expected):
    sort.quicksort(nums, 0, len(nums) - 1)
    assert nums == expected
