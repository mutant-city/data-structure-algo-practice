## This is my personal implementation
def partition(in_array, less_than_value):
    insertion_index = 0
    test_index = 0
    for item in in_array:
        if in_array[test_index] < less_than_value:
            tmp = in_array[insertion_index]
            in_array[insertion_index] = in_array[test_index]
            in_array[test_index] = tmp
            insertion_index += 1
        test_index += 1
    return in_array



##  From: http://p-nand-q.com/python/algorithms/sorting/partitioning.html

def partition_bf(A, pivot_value):
    items_less_than = []
    items_greater_than_or_equal = []

    for item in A:
        if item < pivot_value:
            items_less_than.append(item)
        else:
            items_greater_than_or_equal.append(item)

    A = items_less_than + items_greater_than_or_equal
    return A, len(items_less_than)

## Inplace from website
def partition_inplace_value(A, start, stop, pel_value):

    # enumerate each item
    read_index = start
    while read_index <= stop:
        item = A[read_index]

        # if the current item is less than the pivot value
        if item < pel_value:

            # swap it at the insertion position
            A[start], A[read_index] = A[read_index], A[start]

            # and move the insertion position one up
            start += 1

        read_index += 1

    return start