from typing import List, Dict, Tuple
from collections import namedtuple


def linear_search(arr: List[int], target: int) -> int:
    """Performs a linear search on a list.
    If the target is found, its index is returned.
    If the target is not found, -1 is returned.

    Args:
        arr (List[int]): list to search
        target (int): number to search for

    Returns:
        int: index of the target
    """
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1


def binary_search(arr: List[int], target: int) -> int:
    """Performs a binary search on a list of sorted integers.
    If the target is found, its index is returned.
    If the target is not found, -1 is returned.

    Args:
        arr (List[int]): sorted integers
        target (int): number to search for

    Returns:
        int: index of the target
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid
    return -1


def bfs_shortest_paths(nodes: Dict[str, List[str]], source: str) -> Dict[str, float]:
    """Returns a dictionary containing the shortest path to a 
    node from the source node.

    If a node cannot be reached, its value is float(inf)

    Args:
        nodes (Dict): A dictionary mapping nodes to the list of nodes
        they connect to.
        source (str): The source node

    Returns:
        Dict: dictionary mapping nodes to their distance from the source node. 
    """
    levels = {point: float('inf') for point in nodes.keys()}
    levels[source] = 0
    q = []
    q.append(source)
    while q:
        point = q.pop(0)
        for edge in nodes[point]:
            if levels[edge] == float('inf'):
                levels[edge] = levels[point] + 1
                q.append(edge)
    return levels


def bfs_find_node(nodes: Dict[str, List[str]], source: str, target: str) -> bool:
    """Uses bfs to search a dictionary of nodes, returning true if the target can
    be reached from the source node, false otherwise.

    Args:
        nodes (Dict[str, List[str]]): adjacency list represented as dict
        source (str): starting point
        target (str): node to search for

    Returns:
        bool: Whether or not the target node can be reached from the source
    """
    q = []
    visited = []
    q.append(source)
    while q:
        node = q.pop(0)
        for edge in nodes[node]:
            if edge not in visited:
                if edge == target:
                    return True
                visited.append(edge)
                q.append(edge)
    return False


def dfs(nodes: Dict[str, List[str]], source: str, target: str, visited: list) -> bool:
    """Uses a depth-first search to find a target in a dictionary of nodes, starting at
    some source node. The dictionary of nodes is in form of an adjacency list,
    where the keys are the node values, and the values are a list of a node's neighbours.
    The source must exist in the nodes dictionary.
    The visited list should be called with an empty list.

    Args:
        nodes (Dict[str, List[str]]): Dictionary representation of an adjacency list
        source (str): Starting point
        target (str): Node to search for
        visited (list): List of nodes already visited

    Returns:
        bool: whether or not the target value can be reached. 
    """
    if source == target:
        return True

    visited.append(source)

    for neighbour in nodes[source]:
        if neighbour not in visited:
            if dfs(nodes, neighbour, target, visited):
                return True
    return False


def dfs_visited_parent(graph: Dict[str, List[str]]) -> Tuple[Dict, Dict, Dict, Dict]:
    """Performs a depth-first search on a graph, returning a dictionary of the graphs colors,
    parents, discovery time, and finish time, for each node.

    Colors will are white (0), grey (1), and black (2). White means unvisited, grey means visited,
    black means all neighbours have been visited. All colours in the graph will be black after the 
    depth first search.

    Parents maps a each node to its parent node.

    Discovery time is the integer value at which the node was discovered (turned grey). 
    Time starts at 0 and every time the color of a node is changed, time increments.

    Finish time is the interger value at which the node had all of it's neighbours visited
    (turned black).

    Args:
        graph (Dict[str, List[str]]): Adjacency list representation of the graph

    Returns:
        Tuple[Dict, Dict, Dict, Dict]: colors, parents, discovery time, and finish time.
    """

    colors = {point: 0 for point in graph.keys()}
    parents = {point: None for point in graph.keys()}
    discovery = {}
    finish = {}
    time = 0

    def dfs_visit(point):
        nonlocal time
        colors[point] = 1
        time += 1
        discovery[point] = time
        for neighbour in graph[point]:
            if colors[neighbour] == 0:
                parents[neighbour] = point
                dfs_visit(neighbour)
        colors[point] = 2
        time += 1
        finish[point] = time

    for point in graph.keys():
        if colors[point] == 0:
            dfs_visit(point)
    return colors, parents, discovery, finish


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """Returns whether or not a graph contains a cycle.

    Args:
        graph (Dict[str, List[str]]): Adjacency list

    Returns:
        bool: Whether or not graph contains a cycle
    """
    colors = {point: 0 for point in graph.keys()}
    for point in graph.keys():
        if colors[point] == 0:
            cycle = check_cycle(graph, point, colors)
            if cycle:
                return True
    return False


def check_cycle(graph: Dict[str, List[str]], point: str, colors: Dict[str, int]) -> bool:
    """Check whether or not a graph has a cycle,
    where a cycle is determined by a node visiting a node
    that has already been visited.

    Args:
        graph (Dict[str, List[str]]): Adjacency list representation of a graph
        point (str): Point to start seaching from
        colors (Dict): Dictionary of colors for each point

    Returns:
        bool: Whether or not the graph has a cycle from the specificed point
    """
    colors[point] = 1
    for neighbour in graph[point]:
        if colors[neighbour] == 1:
            return True
        elif colors[neighbour] == 0:
            cycle = check_cycle(graph, neighbour, colors)
            if cycle:
                return True
    colors[point] = 2
    return False
