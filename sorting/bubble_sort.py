import timeit
from numpy.random import randint
import os

def bubbleSort(unsortedArr):
    swaps = 0
    passes = 0
    arr = unsortedArr.copy()
    steps = []
    startTime = timeit.default_timer()
    n = len(arr)
    
    for i in range(n): # Iterate through every element in the array
        passes += 1
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1): # Iterate through elements from 0 to n-i-1
            if arr[j] > arr[j+1] : # If the element found is greater than the next element ...
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap them
                steps.append(arr.copy())
                swaps += 1
                swapped = True

        if swapped == False:
            break
            
    return n, arr, startTime, timeit.default_timer(), swaps, passes, steps
 

 
def main(numTests):
    # Test Cases for the Algorithm
    # unsortedArr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # Worst Case
    # unsortedArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Best Case
    # unsortedArr = [5, 1, 4, 2, 8] # Average Case
    # unsortedArr = [64, 34, 25, 12, 22, 11, 90] # Average Case
    avgSwaps = 0
    avgPasses = 0
    avgTime = 0  
     
    for i in range(numTests):
        # unsortedArr = randint(0, 1000, 1000) # Random Case
        unsortedArr = randint(0, 100, 10) # Random Case
        n, sortedArr, startTime, endTime, swaps, passes, steps = bubbleSort(unsortedArr)

        avgSwaps += swaps
        avgPasses =+ passes
        avgTime += endTime-startTime

        # print("Bubble Sort: \n")
        # print(f"Number of Elements {n}")
        # print(f"Time taken: {endTime - startTime}")
        # print(f"Number of Swaps: {swaps}")
        # print(f"Number of Passes: {passes}")

        # print(f"Unsorted array: {unsortedArr}")
        # # for step in steps:
        # #     print(step)
        # print (f"Sorted array: {sortedArr}")
    return avgTime/(i+1), avgPasses/(i+1), avgSwaps/(i+1), int(n)

if __name__ == "__main__":
    numTests = 1000000000
    time, passes, swaps, n = main(numTests)

    print(f"No. Elements: {n}")
    print(f"No. Tests: {numTests}")
    print(f"Avg Time: {time}")
    print(f"Avg Swaps: {swaps}")
    print(f"Expected Swaps: {n*(n-1)/4}")
    print(f"Avg Passes: {passes}")

    res = str(f'n_tests: {numTests}\nn_elements: {n}\navg_time: {time}\navg_swaps: {swaps}\nexpected_swaps: {n*(n-1)/4}\navg_passes: {passes}\n\n')

    path = os.path.dirname(__file__)+"\\bubble_sort_results.txt"
    with open(path, 'a') as results:
        results.write(res)
        results.close()