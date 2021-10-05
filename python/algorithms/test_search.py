import pytest
from algorithms import search


class TestBinarySearch:
    def test_target_found(self):
        arr = [1, 2, 3, 4]
        target = 4
        indexOfTarget = arr.index(target)
        assert search.binary_search(arr, target) == indexOfTarget

    def test_target_not_found(self):
        arr = [1, 2, 3, 4]
        target = -2
        assert search.binary_search(arr, target) == -1

    def test_empty_arr(self):
        assert search.binary_search([], 1) == -1


class TestBFS:

    def test_shortest_paths(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': [],
            'G': []
        }
        ans = search.bfs_shortest_paths(nodes, 'A')
        assert ans['B'] == 1
        assert ans['C'] == 1
        assert ans['D'] == 2
        assert ans['E'] == 2
        assert ans['F'] == 1
        assert ans['G'] == float('inf')

    def test_find_node(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': [],
            'G': []
        }
        ans = search.bfs_find_node(nodes, 'A', 'E')
        assert ans == True

    def test_cant_find_node(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': [],
            'G': []
        }
        ans = search.bfs_find_node(nodes, 'A', 'G')
        assert ans == False


class TestDFS:

    def test_found(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': ['E'],
            'G': []
        }
        ans = search.dfs(nodes, 'A', 'F', [])
        assert ans == True

    def test_not_found(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': ['E'],
            'G': []
        }
        ans = search.dfs(nodes, 'A', 'G', [])
        assert ans == False

    def test_parents(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': ['E'],
            'G': []
        }
        colors, parents, discovery, finish = search.dfs_visited_parent(nodes)
        assert parents['A'] == None
        assert parents['C'] == 'A'
        assert parents['B'] == 'A'
        assert parents['D'] == 'B'
        assert parents['E'] == 'D'
        assert parents['F'] == 'E'
        assert parents['G'] == None

    def test_check_cycle(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': ['E'],
            'G': []
        }

    def test_has_cycle_recursive(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['F'],
            'F': ['E'],
            'G': []
        }
        assert search.has_cycle(nodes) == True

    def test_no_cycle_recursive(self):
        nodes = {
            'A': ['B', 'C', 'F'],
            'B': ['D'],
            'C': ['E'],
            'D': ['E'],
            'E': ['G'],
            'F': ['E'],
            'G': []
        }
        assert search.has_cycle(nodes) == False
