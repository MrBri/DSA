package main

import "fmt"

// partition the array and return the index of the pivot element
func partition(arr []int, low, high int) int {
	pivot := arr[high]
	i := low - 1

	for j := low; j < high; j++ {
		if arr[j] < pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}

	arr[i+1], arr[high] = arr[high], arr[i+1]

	return i + 1
}

// quicksort function
func quicksort(arr []int, low, high int) {
	if low < high {
		pivot := partition(arr, low, high)
		quicksort(arr, low, pivot-1)
		quicksort(arr, pivot+1, high)
	}
}

func main() {
	arr := []int{4, 8, 1, 3, 9, 7, 2, 5, 6}
	quicksort(arr, 0, len(arr)-1)
	fmt.Println(arr)
}
