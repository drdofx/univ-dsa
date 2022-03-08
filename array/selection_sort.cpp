#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

// implement maximum sort
void maximumSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        swap(arr[i], arr[min]);
    }
} 

int main() {
    int arr[] = {9, 3, 2, 1, 5, 6, 7, 8, 10};

    int n = sizeof(arr) / sizeof(arr[0]);

    // maximum sort
    auto start = high_resolution_clock::now();
    cout << "Maximum sort: "; maximumSort(arr, n);
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