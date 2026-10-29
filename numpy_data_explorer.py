
import numpy as np
import time
import os

print("=" * 50)
print("          NUMPY DATA EXPLORER")
print("=" * 50)

# 1. ARRAY CREATION
print("\n1. ARRAY CREATION")

data = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 78])

print("Student marks:", data)
print("Numbers 1 to 10:", np.arange(1, 11))
print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))

# 2. INDEXING AND SLICING
print("\n2. INDEXING AND SLICING")

print("First mark:", data[0])
print("Last mark:", data[-1])
print("First five marks:", data[:5])
print("Marks from index 3 to 6:", data[3:7])

# 3. MATHEMATICAL OPERATIONS
print("\n3. MATHEMATICAL OPERATIONS")

print("Marks + 5:", data + 5)
print("Marks - 5:", data - 5)
print("Marks * 2:", data * 2)
print("Marks / 2:", data / 2)

# 4. STATISTICAL OPERATIONS
print("\n4. STATISTICAL OPERATIONS")

print("Total marks:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard deviation:", round(np.std(data), 2))
print("Sorted marks:", np.sort(data))

# 5. AXIS-WISE OPERATIONS
print("\n5. AXIS-WISE OPERATIONS")

scores = np.array([
    [75, 80, 65],
    [90, 85, 70],
    [95, 60, 88]
])

print("Score matrix:\n", scores)
print("Sum of each row:", np.sum(scores, axis=1))
print("Sum of each column:", np.sum(scores, axis=0))
print("Average of each row:", np.mean(scores, axis=1))

# 6. RESHAPING
print("\n6. RESHAPING")

numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)

print("Original array:", numbers)
print("Reshaped 3x4 matrix:\n", matrix)

# 7. BROADCASTING
print("\n7. BROADCASTING")

bonus_marks = np.array([5, 10, 0, 5])
original_marks = np.array([
    [70, 75, 80, 85],
    [60, 65, 70, 75],
    [80, 85, 90, 95]
])

updated_marks = original_marks + bonus_marks

print("Original marks:\n", original_marks)
print("Bonus marks:", bonus_marks)
print("Updated marks:\n", updated_marks)

# 8. SAVE AND LOAD ARRAYS
print("\n8. SAVE AND LOAD ARRAYS")

np.save("student_marks.npy", data)
loaded_data = np.load("student_marks.npy")

print("Array saved to student_marks.npy")
print("Loaded array:", loaded_data)
print("Arrays match:", np.array_equal(data, loaded_data))

# 9. NUMPY VS PYTHON LIST PERFORMANCE
print("\n9. PERFORMANCE COMPARISON")

size = 1_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

start = time.perf_counter()
list_result = [x * 2 for x in python_list]
list_time = time.perf_counter() - start

start = time.perf_counter()
numpy_result = numpy_array * 2
numpy_time = time.perf_counter() - start

print(f"Python list calculation: {list_time:.6f} seconds")
print(f"NumPy array calculation: {numpy_time:.6f} seconds")

if numpy_time > 0:
    print("List time / NumPy time:", round(list_time / numpy_time, 2))

# 10. FILTERING DATA
print("\n10. FILTERING DATA")

print("Marks greater than or equal to 80:", data[data >= 80])
print("Marks below 70:", data[data < 70])

print("\nProject completed successfully!")
print("=" * 50)

