# implement insertion sort
def insertion_sort(arr):
    number_swap = 0
    number_loop = 0
    for i in range(1, len(arr)):
        number_loop += 1
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            number_swap += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    print("number of loop in Insertion Sort: " + str(number_loop))
    print("number of swap in Insertion Sort: " + str(number_swap) + "\n")
    print(arr)
    return

arr = [12, 32, 27, 8, 35, 19, 42, 43]

insertion_sort(arr)