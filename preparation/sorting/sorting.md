## Sorting


#### Basic Sorts
* All O(n^2)

1. bubble sort: 
	* compares two, swaps, then compares next two
	* the largest item ends up at the end
	* repeat except not comparing item at end of array
	* sorted section is at end of the array

1. selection sort: 
	* searches entire array, finds smallest element and puts it at and of sorted array at front of main array
	* searches the unsorted space and ignores the sorted space
	* sort is at the beginning of array

1. insertion sort: 
	* grabs an element and tests with previous element until its in a sorted position, grabs next element
	* sorted portion is in beginning of array


#### More efficient Advance Sorts

1. merge sort
    * Θ(n lg n) on average, O(n^2) worst
    * https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
    * requires extra space
    
1. quicksort
    * https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html?highlight=quicksort
    * O(n log n) on average, O(n^2) worst
    
1. heapsort
    * Note: requires knowledge of a binary tree, and heap datastructure


https://medium.com/@mera.stackhouse/which-sorting-algorithms-to-know-for-the-tech-interview-654a1f619e1d










