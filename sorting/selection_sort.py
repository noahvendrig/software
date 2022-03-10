
def SelectionSort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min] = arr[min], arr[i]
    return arr


# Test the code
arr = [111, 73, 230, 2, 15, 24]  # test case
print("Sorted array")
print(SelectionSort(arr))
