#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

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

int main() {
    int arr[] = {9, 3, 2, 1, 5, 6, 7, 8, 10};

    int n = sizeof(arr) / sizeof(arr[0]);

    // insertion sort
    auto start = high_resolution_clock::now();
    cout << "Insertion sort: "; insertionSort(arr, n);
    auto stop = high_resolution_clock::now();
    auto ms_int = duration_cast<microseconds>(stop - start);
    duration<double, micro> ms_double = stop-start;
    cout << ms_double.count() << " microseconds" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << '\n';

    return 0;
}