# implement bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# implement insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# implement maximum sort
def max_sort(arr):
    key = len(arr) - 1
    for i in range (0, len(arr)-1):
        max = arr[0]
        imax = 0
        for j in range(1, key+1):
            if (arr[j] > max):
                max = arr[j]
                imax = j
        arr[key], arr[imax] = arr[imax], arr[key]
        key -= 1
    return arr

arr = [9, 3, 2, 1, 4, 3, 10]

# print(bubble_sort(arr))
# print(insertion_sort(arr))
# print(max_sort(arr))

print(arr)



