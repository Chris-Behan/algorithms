from typing import List


def quicksort(nums: List[int], low: int, high: int):
    """
    Sorts a list of numbers in place using the QuickSort algorithm.

    Args:
        nums (List[int]): unsorted list
        low (int): index of the leftmost element
        high (int): index of the rightmost element
    """
    if low < high:
        sorted_idx = partition(nums, low, high)

        quicksort(nums, low, sorted_idx - 1)
        quicksort(nums, sorted_idx + 1, high)


def partition(nums: List[int], low: int, high: int) -> int:
    """
    Partition function used by the quicksort algorithm.
    Re-arranges elements in the list such that all elements to the left
    of the pivot are smaller than it. Returns the index of the pivot.

    Args:
        nums (List[int]): numbers to re-arrange
        low (int): left most element that is not in guaranteed to be in its correct position
        high (int): index of the pivot

    Returns:
        int: index of an element that is in its correct position for the sorted list
    """
    pivot = nums[high]
    i = low - 1
    j = low
    while j <= high - 1:
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1
