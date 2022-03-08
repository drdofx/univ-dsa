# implement maximum sort
def max_sort(a):
    for i in range(len(a)):
        max_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[max_index]:
                max_index = j
        a[i], a[max_index] = a[max_index], a[i]
    return a

a = [10, 41, 2, 13, 5, 8, 7, 6, 9, 3, 4, 1]

print(max_sort(a))