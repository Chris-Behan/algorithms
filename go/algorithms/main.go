package main

import (
	"fmt"

	"example.com/algorithms/search"
)

func main() {
	idx := search.BinarySearch([]int{1, 2, 3, 4, 5}, 5)
	fmt.Printf("%v", idx)
}
