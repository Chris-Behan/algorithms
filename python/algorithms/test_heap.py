import pytest
from algorithms import heap


class TestMaxHeap:
    def test_heap_insert(self):
        h = heap.MaxHeap()
        h.insert(1)
        h.insert(2)
        h.insert(3)
        h.insert(10)
        h.insert(9)
        h.insert(5)
        assert h.maximum() == 10

    def test_extract_max(self):
        h = heap.MaxHeap()
        h.insert(8.5)
        h.insert(9)
        h.insert(10)
        assert h.extract_max() == 10
        assert h.maximum() == 9
