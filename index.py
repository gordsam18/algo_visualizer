import random
import time
from algos.sort.bubble import bubble_sort
from algos.sort.insertion import insertion_sort
from algos.sort.selection import selection_sort
from algos.sort.merge import merge_sort

unsorted_array = [random.randint(0, 9) for _ in range(50)]



# print("hello world")

print(f"Original array: {unsorted_array}")
start_time = time.time()
print(f"Bubble Sort:    {bubble_sort(unsorted_array)} : Execution time: {(time.time() - start_time) * 1000:.3f}ms")
start_time = time.time()
print(f"Insterion Sort: {insertion_sort(unsorted_array)} : Execution time: {(time.time() - start_time) * 1000:.3f}ms")
start_time = time.time()
print(f"Selection Sort: {selection_sort(unsorted_array)} : Execution time: {(time.time() - start_time) * 1000:.3f}ms")
start_time = time.time()
print(f"Merge Sort:     {merge_sort(unsorted_array)} : Execution time: {(time.time() - start_time) * 1000:.3f}ms")
"""
start_time = time.time()
bubble_sort(unsorted_array)
print(f"Bubble Sort Execution time: {(time.time() - start_time) * 1000:.3f}ms")

start_time = time.time()
insertion_sort(unsorted_array)
print(f"Insterion Sort Execution time: {(time.time() - start_time) * 1000:.3f}ms")

start_time = time.time()
selection_sort(unsorted_array)
print(f"Selection Sort Execution time: {(time.time() - start_time) * 1000:.3f}ms")

start_time = time.time()
merge_sort(unsorted_array)
print(f"Merge Sort Execution time: {(time.time() - start_time) * 1000:.3f}ms")
"""