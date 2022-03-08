#include <iostream>

using namespace std;

// implement binary search (recursive)
int binarySearchRecursive(int arr[], int l, int r, int x) {
    if (r >= l) {
        int mid = (l+r)/2;
        if (arr[mid] == x) {
            return mid;
        }
        if (arr[mid] > x) {
            return binarySearchRecursive(arr, l, mid - 1, x);
        }
        return binarySearchRecursive(arr, mid + 1, r, x);
    }
    return -1;
}

// implement binary search (iterative)
int binarySearchIterative(int arr[], int l, int r, int x) {
    int loop = 0;
    while (l <= r) {
        loop++;   
        cout << loop << endl;

        int mid = (l+r)/2;
        if (arr[mid] == x) {
            return mid;
        }
        if (arr[mid] > x) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return -1;
}

// implement sequential search
int sequentialSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Binary Search Recursive
    int bin_search = binarySearchRecursive(arr, 0, n - 1, 5);
    if (bin_search) {
        cout << "Binary search (recursive): found on index " << bin_search << endl;
    } else {
        cout << "Binary search (recursive): element not found" << endl;
    }

    // Binary Search Iterative
    int bin_search_itr = binarySearchIterative(arr, 0, n - 1, 10);
    if (bin_search_itr) {
        cout << "Binary search (iterative): found on index " << bin_search_itr << endl;
    } else {
        cout << "Binary search (iterative): element not found" << endl;
    }

    // Sequential Search
    int seq_search = sequentialSearch(arr, n, 5);
    if (seq_search) {
        cout << "Sequential search: found on index " << seq_search << endl;
    } else {
        cout << "Sequential search: element not found" << endl;
    }
    
    return 0;
}