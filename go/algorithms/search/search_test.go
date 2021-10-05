package search

import "testing"

func TestBinaryTargetFound(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	indexOfFour := 3
	result := BinarySearch(arr, 4)
	if result != indexOfFour {
		t.Fatalf("BinarySearch(%v, %v) returned %v, expected %v", arr, indexOfFour, result, indexOfFour)
	}
}

func TestBinaryTargetNotFound(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	notInArr := 6
	result := BinarySearch(arr, notInArr)
	if result != -1 {
		t.Fatalf("BinarySearch(%v, %v) returned %v, expected -1", arr, notInArr, result)
	}
}

func TestBinaryEmptyInput(t *testing.T) {
	arr := []int{}
	result := BinarySearch(arr, 1)
	if result != -1 {
		t.Fatalf("BinarySearch(%v, 1) returned %v, expected -1", arr, result)
	}
}

func TestLinearTargetFound(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	indexOfFour := 3
	result := LinearSearch(arr, 4)
	if result != indexOfFour {
		t.Fatalf("LinearSearch(%v, %v) returned %v, expected %v", arr, indexOfFour, result, indexOfFour)
	}
}

func TestLinearTargetNotFound(t *testing.T) {
	arr := []int{1, 2, 3, 4, 5}
	notInArr := 6
	result := LinearSearch(arr, notInArr)
	if result != -1 {
		t.Fatalf("LinearSearch(%v, %v) returned %v, expected -1", arr, notInArr, result)
	}
}

func TestLinearEmptyInput(t *testing.T) {
	arr := []int{}
	result := LinearSearch(arr, 1)
	if result != -1 {
		t.Fatalf("LinearSearch(%v, 1) returned %v, expected -1", arr, result)
	}
}

func TestBFSShortestPath(t *testing.T) {
	nodes := map[string][]string{
		"a": {"b", "c", "f"},
		"b": {"d"},
		"c": {"e"},
		"d": {"e"},
		"e": {"f"},
		"f": {},
		"g": {},
	}
	result := BFSShortestPath(nodes, "a")
	if result["b"] != 1 {
		t.Fatalf("distance to b should be 1, instead it is %v", result["b"])
	}
	if result["c"] != 1 {
		t.Fatalf("distance to c should be 1, instead it is %v", result["c"])
	}
	if result["d"] != 2 {
		t.Fatalf("distance to d should be 2, instead it is %v", result["d"])
	}
	if result["e"] != 2 {
		t.Fatalf("distance to e should be 2, instead it is %v", result["e"])
	}
	if result["f"] != 1 {
		t.Fatalf("distance to f should be 1, instead it is %v", result["f"])
	}
	if result["g"] != -1 {
		t.Fatalf("distance to g should be -1, instead it is %v", result["e"])
	}
}
