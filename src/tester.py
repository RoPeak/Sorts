import random as rand
import os
from Algos import *

# This function tests the given sorting algorithm by creating a random list of integers
def TestSortingAlgorithms(SortAlgoToTest):
    N = 10     # size of input array
    K = 1000   # range of numbers in input array
    
    #these two arguments that are passed to the sorting algos 
    # mark the starting and ending index of the range
    #to be sorted. we always want to sort the entire array 
    p = 0
    r = N-1 
    
    print("===================================================================")
    print(f"This is a test for USER sort Function :: {SortAlgoToTest.__name__}")
    print("===================================================================")
    print(f"Creating random list of {N} integers in the range 1 - {K}")
    print("")
    
    #random array
    a_unsorted = rand.sample(range(1,K),N)
    
    #fixed array, for debug:
    #a_unsorted =  [35, 24, 824, 332, 546, 31, 429, 945, 654, 646]

    print(f"Unsorted list is :\n", a_unsorted)
    print("")    
       
    #Testing InsertionSort (1a) functionality
    print(f"Testing USER sort function...")    
    a_sorted_testing = a_unsorted.copy()
    try:
        SortAlgoToTest(a_sorted_testing, p, r)
    except:
        print(f"\nERROR: Testing not carried out. "
              f"Unable to execute the required function {SortAlgoToTest.__name__} OR "
              f"function has runtime errors"
              )    
    
    #test result 
    passed = 1
    for i in range (1,N):
        if a_sorted_testing[i] <  a_sorted_testing[i-1]:
            passed = 0
            print("TEST FAILED!")
            print(f"This is the output that failed :\n", a_sorted_testing)
            print("")
            break
    
    if passed:        
        print("TEST PASSED")
        print(f"Sorted list is :\n", a_sorted_testing)
        print("")

# This function tests the given sortin algorithm by running it on a given file
def TestMultipleSortingAlgos(algos,file):
    file = os.getcwd() + "\\resource\\" + file
    print ("")
    print(f"Time taken to sort {file}:")
    for algo2sort in algos:
        t = TimeSortingAlgorithms(algo2sort,file)
        print(f"{algo2sort.__name__:14} : {t} milliseconds")
    print ("")

def main():
    print("===================================================================")
    print(f"Timing 5 Sorting Algorithms on random inputs")
    print("===================================================================")

    #QUICKSORT test
    TestSortingAlgorithms(QUICKSORT)

    #QUICKSORT test, median of 3
    TestSortingAlgorithms(QUICKSORT_MED3)

    #BUBBLESORT test
    TestSortingAlgorithms(BUBBLESORT)

    #INSERTIONSORT test
    TestSortingAlgorithms(INSERTIONSORT)

    #MERGESORT test
    TestSortingAlgorithms(MERGESORT)

    print("===================================================================")
    print(f"Timing 5 Sorting Algorithms on variety of input sizes")
    print("===================================================================")

    algos = [ QUICKSORT
            , QUICKSORT_MED3
            , BUBBLESORT
            , INSERTIONSORT
            , MERGESORT
            ]

    # Test each algorithm on each file
    TestMultipleSortingAlgos(algos, "int10.txt")
    TestMultipleSortingAlgos(algos, "int50.txt")
    TestMultipleSortingAlgos(algos, "int100.txt")
    TestMultipleSortingAlgos(algos, "int1000.txt")
    TestMultipleSortingAlgos(algos, "int1000_presorted_ascending.txt")
    TestMultipleSortingAlgos(algos, "int1000_presorted_descending.txt")

if __name__ == "__main__":
    main()