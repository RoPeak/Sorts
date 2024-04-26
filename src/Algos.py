import time
import sys
def is_sorted(A):
    # Quick check whether a given list is sorted
    # Used for my own testing purposes
    return all(A[i] <= A[i+1] for i in range(len(A) - 1)) or all(A[i] >= A[i+1] for i in range(len(A) - 1))

def QUICKSORT(A, start, end):
    if start < end:
        pivot = PARTITION(A, start, end)
        QUICKSORT(A, start, pivot-1)
        QUICKSORT(A, pivot+1, end)

def QUICKSORT_MED3(A, start, end):
    if start < end:
        # Find median
        mid = (start + end) // 2
        medianFinder = sorted([A[start], A[mid], A[end]]) # Put the first, middle, and last elements of the array in a seperate, sorted list
        median = medianFinder[1] # Median will always be element at index 1 after sorted() call

        # Find position of the value above
        medianIndex = A.index(median)

        # Swap median with last array element
        temp = A[end]
        A[end] = A[medianIndex]
        A[medianIndex] = temp

        # Carry out sort
        pivot = PARTITION(A, start, end)
        QUICKSORT_MED3(A, start, pivot-1)
        QUICKSORT_MED3(A, pivot+1, end)

def PARTITION(A, start, end):
    pval = A[end]
    p = start

    for t in range(start, end):
        if A[t] <= pval:
            p += 1
            temp = A[p-1]
            A[p-1] = A[t]
            A[t] = temp
    temp = A[p]
    A[p] = A[end]
    A[end] = temp
    return p

def BUBBLESORT(A, start, end):
    for outer in range(end, start, -1):
        for i in range(outer):
            if (A[i] > A[i+1]):
                # Swap adjacent variables
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

def INSERTIONSORT(A, start, end):
    for outer in range(start, end+1):
        key = A[outer]
        inner = outer
        while inner > 0 and A[inner-1] > key:
            A[inner] = A[inner-1]
            inner -= 1
        A[inner] = key

def MERGESORT(A, start, end):
    if start < end:
        mid = (start + end) // 2
        MERGESORT(A, start, mid)
        MERGESORT(A, mid+1, end)
        MERGE(A, start, mid, end)

def MERGE(A, start, mid, end):
    left = A[start:mid+1]
    right = A[mid+1:end+1]
    i = j = 0
    k = start

    for k in range(start, end+1):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1

def TimeSortingAlgorithms(algorithm, fileName):
    # Increasing limit for large quicksorts
    sys.setrecursionlimit(2000)

    # Collect all the values from the given file
    unsorted_list = []
    with open(fileName, "r") as file:
        for integer in file:
            value = int(integer.strip())
            unsorted_list.append(value)

    # Initialise start and end values
    start = 0
    end = len(unsorted_list) - 1

    # Time sorting algorithm
    beginning = time.perf_counter()
    algorithm(unsorted_list, start, end)
    ending = time.perf_counter()

    # Return time taken in milliseconds
    return (ending - beginning) * 1000