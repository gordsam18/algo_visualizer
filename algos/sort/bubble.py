"""
Bubble sort:

Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

1. Go through the array, one value at a time.
2. For each value, compare the value with the next value.
3. If the value is higher than the next one, swap the values so that the highest value comes last.
4. Go through the array as many times as there are values in the array.
"""

def bubble_sort(array):

    n = len(array)
    for x in range(n - 1):

        for i in range(n-x-1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    
    return array 
