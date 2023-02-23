package main

import "fmt"

// merge two sorted arrays into a new sorted array
func merge(left, right []int) []int {
	merged := make([]int, len(left)+len(right))
	i, j, k := 0, 0, 0

	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			merged[k] = left[i]
			i++
		} else {
			merged[k] = right[j]
			j++
		}
		k++
	}

	for i < len(left) {
		merged[k] = left[i]
		i++
		k++
	}

	for j < len(right) {
		merged[k] = right[j]
		j++
		k++
	}

	return merged
}

// merge sort function
func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2
	left := arr[:mid]
	right := arr[mid:]

	left = mergeSort(left)
	right = mergeSort(right)

	return merge(left, right)
}

func main() {
	arr := []int{4, 8, 1, 3, 9, 7, 2, 5, 6}
	sorted := mergeSort(arr)
	fmt.Println(sorted)
}
