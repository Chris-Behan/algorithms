from typing import Union


class MaxHeap:
    """Max heap data structure for ints and floats.
    """

    def __init__(self) -> None:
        """Creates an empty max heap.
        The underlying array is initialized to have a single element at index 0, which we will never
        touch. We do this because the math associated with heap operations depends on the first
        element being at index 1. For example, the left child of an element in a heap is 2 * index,
        but if the index is 0, we would say the left child is 2 * 0 = 0, which is incorrect.
        """
        self.arr: list[Union[int, float]] = [0]

    def maximum(self) -> Union[int, float]:
        """Returns the value of largest number in the heap.

        Returns:
            Union[int, float]: largest number
        """
        return self.arr[1]

    def heapify(self, idx: int):
        """Exchanges the value at idx with the larger of its two children. This process is repeated
        until the value of idx is equal to or greater than its children and thus in the correct
        position.

        Args:
            idx (int): index to move

        Raises:
            ValueError: raised if the idx is out of bounds
        """
        if idx < 1 or idx >= len(self.arr):
            raise ValueError(
                f"idx must be between 1 and {len(self.arr)} inclusive. You entered {idx}.")

        left_idx = 2 * idx
        right_idx = 2 * idx + 1
        largest_idx = idx

        if left_idx < len(self.arr) and self.arr[left_idx] > self.arr[idx]:
            largest_idx = left_idx

        if right_idx < len(self.arr) and self.arr[right_idx] > self.arr[idx]:
            largest_idx = right_idx

        if largest_idx != idx:
            self.arr[largest_idx], self.arr[idx] = self.arr[idx], self.arr[largest_idx]
            self.heapify(largest_idx)

    def extract_max(self) -> Union[int, float]:
        """Removes and returns the largest value in the heap.

        Raises:
            ValueError: Heap is empty
        """
        if self._is_empty():
            raise ValueError("Heap is empty.")
        maximum = self.arr[1]
        self.arr[1] = self.arr[-1]
        self.arr.pop()
        self.heapify(1)
        return maximum

    def _is_empty(self):
        if len(self.arr) == 1:
            return True
        return False

    def insert(self, val: Union[int, float]):
        """Insert a number into the max heap.

        Args:
            val (Union[int, float]): number to insert
        """
        self.arr.append(val)
        insertion_idx = len(self.arr) - 1
        parent_idx = insertion_idx // 2
        while insertion_idx > 1 and self.arr[parent_idx] < self.arr[insertion_idx]:
            self.arr[insertion_idx], self.arr[parent_idx] = (self.arr[parent_idx],
                                                             self.arr[insertion_idx])
            insertion_idx = parent_idx
            parent_idx = parent_idx // 2
