import arcade
"""
Insertion Sort:

The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.

1. Take the first value from the unsorted part of the array.
2. Move the value into the correct place in the sorted part of the array.
3. Go through the unsorted part of the array again as many times as there are values.
"""
def insertion_sort(array, sound, volume):
    array_colors = [arcade.color.BLUE for _ in array]
    array_color = []
    
    n = len(array)
    
    for i in range(1, n):
        insert_index = i
        array_colors[i] = arcade.color.BLUE
        current = array.pop(i)
        for j in range(i-1, -1, -1):
            array_colors[j] = arcade.color.RED
            if array[j] > current:
                insert_index = j
                array_colors[j] = arcade.color.BLUE
                arcade.play_sound(sound, volume)
        array.insert(insert_index, current)

    array_colors[i] = arcade.color.BLUE  # Reset color
    array.insert(insert_index, array.pop(i))

    return array
