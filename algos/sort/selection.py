"""
Selection Sort:

The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

How it works:

1. Take the first value from the unsorted part of the array.
2. Move the value into the correct place in the sorted part of the array.
3. Go through the unsorted part of the array again as many times as there are values.
"""

def selection_sort(array):
    # take the length of the array 
    n = len(array)

    # loop through the range of the array starting at the second index
    for i in range(1, n):
        # record the insert index
        insert_index = i
        # pop the current index off the array
        current_value = array.pop(i)
        # Loop through the array from the next index that increments through the sorted array
        for j in range(i-1, -1, -1):
            # compare the index wiht the current value 
            if array[j] > current_value:
                insert_index = j
        array.insert(insert_index, current_value)
    
    return array

