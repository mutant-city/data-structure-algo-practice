def partition(in_array, partition_value):

    insertion_index = 0

    for swap_index in range(0, len(in_array)):
        if in_array[swap_index] < partition_value:
            # swap
            tmp = in_array[insertion_index]
            in_array[insertion_index] = in_array[swap_index]
            in_array[swap_index] = tmp

            # increment index
            insertion_index += 1



def find_pivot(in_array):
    length = len(in_array)
    first = in_array[0]
    middle = in_array[(length-1)/2]
    last = in_array[length-1]
    return max([first, middle, last])


def quick(in_array):
    pivot = find_pivot(in_array)
