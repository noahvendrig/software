def FindMaxMin(arr):
    current_max = arr[0]
    current_min = arr[0]
    for i in range(len(arr[:-1])):  # iterate through  whole list except last element
        # check if current max/min is higher than the next value in the arr
        if current_max < arr[i+1]:
            current_max = arr[i+1]

        if current_min > arr[i+1]:
            current_min = arr[i+1]

    min, max = current_min, current_max  # final results
    return min, max


a = [9, 1, 44, 33, 105, 69, 111]  # test case
min, max = FindMaxMin(a)
print(min, max)
