#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

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

int main() {
    int arr[] = {9, 3, 2, 1, 5, 6, 7, 8, 10};

    int n = sizeof(arr) / sizeof(arr[0]);

    // bubble sort
    auto start = high_resolution_clock::now();
    cout << "Bubble sort: "; bubbleSort(arr, n);
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