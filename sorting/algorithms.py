from visualizer import Visualizer
##################################


def swap(list, key_one, key_two):
    list[key_one], list[key_two] = list[key_two], list[key_one]

#################################################


def selection_sort(array):
    array_length = len(array)

    for i in range(array_length):
        min_index = i

        for j in range(i + 1, array_length):
            if (array[j] < array[min_index]):
                min_index = j

            if min_index != i:
                swap(array, min_index, i)

            

##################################


def bubble_sort(array):
    array_length = len(array)

    for i in range(array_length):
        for j in range(array_length - i - 1):
            if (array[j] > array[j + 1]):
                swap(array, j, j + 1)
                print("yup")
                Visualizer.visualize(j, j+1, array)


##############################################

def insertion_sort(array, start=0, gap=1):
    array_length = len(array)

    for i in range(start + gap, array_length, gap):
        value_to_sort = array[i]

        while array[i - 1] > value_to_sort and i > 0:
            swap(array, i, i-1)
            i -= gap


def shell_sort(array):
    gap = len(array) // 2

    while gap > 0:
        for i in range(gap):
            insertion_sort(array, i, gap)
        
        gap //= 2

################################################


def merge_sort(array):
    array_length = len(array)

    if array_length <= 1:
        return array

    middle = array_length // 2

    start = array[:middle]
    end = array[middle:]

    start = merge_sort(start)
    end = merge_sort(end)

    return merge(start, end)


def merge(start, end):
    result = []
    start_index, end_index = 0, 0
    start_length, end_length = len(start), len(end)

    while start_index < start_length and end_index < end_length:
        if start[start_index] <= end[end_index]:
            result.append(start[start_index])
            start_index += 1
        else:
            result.append(end[end_index])
            end_index += 1

    if start_index < start_length:
        result.extend(start[start_index:])
    if end_index < end_length:
        result.extend(end[end_index:])

    return result

#####################################################


def quick_sort(array, start, end):

    if end - start > 0:
        pivot, _start, _end = array[start], start, end

        while _start <= _end:

            while array[_start] < pivot:
                _start += 1

            while array[_end] > pivot:
                _end -= 1

            if _start <= _end:
                swap(array, _start, _end)
                _start += 1
                _end -= 1

        quick_sort(array, start, _end)
        quick_sort(array, _start, end)

###########################################################


def heap_sort(array):
    array_length = len(array)

    for start in range(array_length // 2 - 1, -1, -1):
        sift_down(array, array_length, start)

    for end in range(array_length - 1, 0, -1):
        swap(array, end, 0)
        sift_down(array, end, 0)


def sift_down(array, start, end):
    root = end

    _start = 2 * end + 1
    _end = 2 * end + 2

    if _start < start and array[_start] > array[root]:
        root = _start

    if _end < start and array[_end] > array[root]:
        root = _end

    if root != end:
        swap(array, end, root)
        sift_down(array, start, root)

###########################################
