import random

# Quick Sort (Deterministic)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Quick Sort (Randomized)
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    left = [x for i, x in enumerate(arr) if i != pivot_idx and x < pivot]
    right = [x for i, x in enumerate(arr) if i != pivot_idx and x >= pivot]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)

# Function to test the Quick Sort variants
def test_quick_sort(arr):
    sorted_arr_deterministic = quick_sort(arr.copy())
    sorted_arr_randomized = randomized_quick_sort(arr.copy())
    print("Original array:", arr)
    print("Deterministic Quick Sort:", sorted_arr_deterministic)
    print("Randomized Quick Sort:", sorted_arr_randomized)

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    test_quick_sort(arr)
