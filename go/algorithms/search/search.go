package search

// BinarySearch searches a sorted array of integers for the specified target,
// returning its index. If the target is not present in the array, -1 is
// returned. The input array must be sorted.
func BinarySearch(arr []int, target int) int {
	low, high := 0, len(arr)-1
	for low <= high {
		mid := (low + high) / 2
		if arr[mid] == target {
			return mid
		} else if arr[mid] > target {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	// low less than high, target not in arr
	return -1
}

// LinearSearch searches an array of integers for a specified target,
// returning the index at which the target is found. -1 is returned
// if the target is not found.
func LinearSearch(arr []int, target int) int {
	for idx, num := range arr {
		if num == target {
			return idx
		}
	}
	return -1
}

// BFSShortestPath returns a map of the shortest path between each node in
// a graph and the specified start node. If there is no path from the
// start node to node x, the value in the map for node x will be -1.
// The nodes are represented as a map whose keys are strings (containing node id)
// and whose values are a slice of strings containing neighboring nodes.
func BFSShortestPath(nodes map[string][]string, start string) map[string]int {
	distances := map[string]int{}
	for key := range nodes {
		distances[key] = -1
	}

	distances[start] = 0
	q := []string{start}

	for len(q) > 0 {
		// pop from queue
		point := q[0]
		q = q[1:]

		for _, neighbour := range nodes[point] {
			if distances[neighbour] == -1 {
				distances[neighbour] = distances[point] + 1
				q = append(q, neighbour)
			}
		}
	}
	return distances
}
