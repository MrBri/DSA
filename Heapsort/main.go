package main

import "fmt"

// heapify the subtree rooted at index i
func heapify(arr []int, n, i int) {
	largest := i     // initialize largest as root
	left := 2*i + 1  // left child index
	right := 2*i + 2 // right child index

	// if left child is larger than root
	if left < n && arr[left] > arr[largest] {
		largest = left
	}

	// if right child is larger than largest so far
	if right < n && arr[right] > arr[largest] {
		largest = right
	}

	// if largest is not root
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]

		// recursively heapify the affected subtree
		heapify(arr, n, largest)
	}
}

// heapsort function
func heapsort(arr []int) {
	n := len(arr)

	// build heap (rearrange array)
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}

	// one by one extract elements
	for i := n - 1; i >= 0; i-- {
		// move current root to end
		arr[0], arr[i] = arr[i], arr[0]

		// call max heapify on the reduced heap
		heapify(arr, i, 0)
	}
}

func main() {
	arr := []int{4, 8, 1, 3, 9, 7, 2, 5, 6}
	heapsort(arr)
	fmt.Println(arr)
}
