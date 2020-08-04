def quickSort(A, low, high):
    if low < high:
        pivotIndex = partition(A, low, high)
        quickSort(A, low, pivotIndex - 1)
        quickSort(A, pivotIndex + 1, high)
        return A


def partition(A, low, high):
    pivot = A[high]
    pi = low
    for i in range(low, high + 1):
        if A[i] < pivot:
            A[pi], A[i] = A[i], A[pi]  # swap
            pi += 1
    A[pi], A[high] = A[high], A[pi]  # swap
    return pi


arr = [5, 15, 2, -2, 6, 10, 12, 6]
arr1 = quickSort(arr, 0, len(arr) - 1)
print(arr1)
