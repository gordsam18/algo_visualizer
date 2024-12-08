"""
Merge Sort:

The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, 
and then building the array back together the correct way so that it is sorted.

How it works:

1. Divide the unsorted array into two sub-arrays, half the size of the original.
2. Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
3. Merge two sub-arrays together by always putting the lowest value first.
4. Keep merging until there are no sub-arrays left.
"""

def merge_sort(array):
    # check if the array is over 1 index long
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    lefthalf = array[:middle]
    righthalf = array[middle:]

    sortedLeft = merge_sort(lefthalf)
    sortedRight = merge_sort(righthalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+= 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
