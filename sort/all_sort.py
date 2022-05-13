import os

def clear():
    os.system('clear')

class Sorting:
    def __init__(self, max):
        self.max = max
        self.arr = []

    def insert_to_array(self):
        index = 0
        while (index < self.max):
            num = int(input(f"Enter a number for index {index}: "))
            self.arr.append(num)
            index += 1
        print("\nbefore sort: " + str(self.arr) + "\n")

    def output_array(self):
        print("after insertion sort: " + str(self.is_arr))
        print("after bubble sort: " + str(self.bs_arr) + "\n")

    def insertion_sort(self):
        self.is_arr = self.arr.copy()
        number_swap = 0
        number_loop = 0
        for i in range(1, len(self.is_arr)):
            number_loop += 1
            key = self.is_arr[i]
            j = i-1
            while j >= 0 and key < self.is_arr[j]:
                number_swap += 1
                self.is_arr[j+1] = self.is_arr[j]
                j -= 1
            self.is_arr[j+1] = key
        print("number of loop in insertion sort: " + str(number_loop))
        print("number of swap in insertion sort: " + str(number_swap) + "\n")
        print("after insertion sort: " + str(self.is_arr) + "\n")
        return self.is_arr
    
    def bubble_sort(self):
        self.bs_arr = self.arr.copy()
        number_swap = 0
        number_loop = 0
        for i in range(len(self.bs_arr)):
            number_loop += 1
            for j in range(len(self.bs_arr)-1-i):
                if self.bs_arr[j] > self.bs_arr[j+1]:
                    number_swap += 1
                    self.bs_arr[j], self.bs_arr[j+1] = self.bs_arr[j+1], self.bs_arr[j]
        print("number of loop in bubble sort: " + str(number_loop))
        print("number of swap in bubble sort: " + str(number_swap) + "\n")
        print("after bubble sort: " + str(self.bs_arr) + "\n")
        return self.bs_arr
    
    def selection_sort(self):
        self.ss_arr = self.arr.copy()
        number_swap = 0
        number_loop = 0
        for i in range(len(self.ss_arr)):
            number_loop += 1
            min_index = i
            for j in range(i+1, len(self.ss_arr)):
                if self.ss_arr[j] < self.ss_arr[min_index]:
                    min_index = j
            if min_index != i:
                number_swap += 1
                self.ss_arr[i], self.ss_arr[min_index] = self.ss_arr[min_index], self.ss_arr[i]
        print("number of loop in selection sort: " + str(number_loop))
        print("number of swap in selection sort: " + str(number_swap) + "\n")
        print("after selection sort: " + str(self.ss_arr) + "\n")
        return self.ss_arr


def main():
    max_element = int(input("Enter the maximum number of elements: "))
    arr = Sorting(max_element)

    arr.insert_to_array()
    
    while (True):
        clear()
        print("\n1. Insertion Sort")
        print("2. Bubble Sort")
        print("3. Selection Sort")
        print("4. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            arr.insertion_sort()
        elif choice == 2:
            arr.bubble_sort()
        elif choice == 3:
            arr.selection_sort()
        elif choice == 4:
            break
        else:
            print("\nInvalid choice!\n")
        input("\nEnter any key to continue...")
    print("Bye!")

main()

    

