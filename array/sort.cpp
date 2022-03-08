#include <iostream>

using namespace std;

// implement bubble sort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// implement insertion sort
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// implement maximum sort
void maximumSort(int arr[], int n) {
    int key = n-1;
    for (int i = 0; i < n - 1; i++) {
        int maks = arr[0];
        int imaks = 0;
        for (int j = 1; j <= key; j++) {
            if (arr[j] > maks) {
                maks = arr[j];
                imaks = j;
            }
        }
        swap(arr[key], arr[imaks]);
        key--;
    }
}

int main() {
    int arr[] = {9, 3, 2, 1, 5, 6, 7, 8, 10};
    int arr2[] = {9, 3, 2, 1, 5, 6, 7, 8, 10};
    int arr3[] = {9, 3, 2, 1, 5, 6, 7, 8, 10};

    int n = sizeof(arr) / sizeof(arr[0]);

    // bubble sort
    cout << "Bubble sort: "; bubbleSort(arr, n);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << '\n';

    // insertion sort
    cout << "Insertion sort: "; insertionSort(arr2, n);
    for (int i = 0; i < n; i++) {
        cout << arr2[i] << " ";
    }
    cout << '\n';

    // maximum sort
    cout << "Maximum sort: "; maximumSort(arr3, n);
    for (int i = 0; i < n; i++) {
        cout << arr3[i] << " ";
    }
    cout << '\n';

    return 0;
}