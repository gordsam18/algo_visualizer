import arcade
"""
Bubble sort:

Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

1. Go through the array, one value at a time.
2. For each value, compare the value with the next value.
3. If the value is higher than the next one, swap the values so that the highest value comes last.
4. Go through the array as many times as there are values in the array.
"""

def bubble_sort(array, sound, volume):
    array_colors = [arcade.color.BLUE for _ in array]
    array_color = []

    n = len(array)
    for x in range(n - 1):

        for i in range(n-x-1):
            if array[i] > array[i + 1]:
                temp = array[i]
                
                array[i] = array[i + 1]
                array[i + 1] = temp
                #array_colors[i], array_colors[i + 1] = arcade.color.RED, arcade.color.RED

                
                if i > 0:
                   array_colors[i-1] = arcade.color.BLUE
                return
            arcade.play_sound(sound, volume)
    return array 




"""for i in range(len(self.array) - 1):
            if self.array[i] > self.array[i + 1]:
                # Swap the elements
                self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                self.array_colors[i], self.array_colors[i + 1] = arcade.color.RED, arcade.color.RED
                
                # Reset colors after the step
                if i > 0:
                    self.array_colors[i - 1] = arcade.color.BLUE
                return  # Exit after one swap for animation

        # If no swaps are left, the sorting is done
        self.sorting_done = True
        self.array_colors = [arcade.color.GREEN for _ in self.array]  # Mark all as sorted"""