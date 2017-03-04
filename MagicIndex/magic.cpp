/*
Magic Index

Given a zero-indexed array of integers, the magic index is any element whose value corresponds
with its position.

e.g. A = {0, 1, 3, 7, 2, 2, 9} => 0, 1 are magic indices

1.) Write a function that prints the magic indices to the console.
2.) If we know the array would be sorted, how can the algorithm be improved?
    Write a function that returns at least one magic index, if present.
*/

#include <iostream>

using namespace std;

void magicBrute(int array[], int length);
int magicBetter(int array[], int length, int start, int end, int mid);

int main() {
    int testA[8] = {0, 3, 4, 5, 5, 5, 6, 7};            // 0, 5, 6, 7
    int testB[6] = {-40, -10, 20, 1, 4, 8};             // 4
    int testC[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};  // all
    
    cout << "Test A: ";
    for(int index = 0; index < 8; index++) {
        cout << testA[index];
        
        if(index != 7) {
            cout << ", ";
        }
    }
    cout << endl;
    
    cout << "Brute: ";
    magicBrute(testA, 8);
    cout << endl << "Better: " << magicBetter(testA, 8, 0, 7, 4) << endl;
    
    cout << "Test B: ";
    for(int index = 0; index < 6; index++) {
        cout << testB[index];
        
        if(index != 5) {
            cout << ", ";
        }
    }
    cout << endl;
    
    cout << "Brute: ";
    magicBrute(testB, 6);
    cout << endl << "Better: " << magicBetter(testB, 6, 0, 5, 3) << endl;
    
    cout << "Test C: ";
    for(int index = 0; index < 10; index++) {
        cout << testC[index];
        
        if(index != 9) {
            cout << ", ";
        }
    }
    cout << endl;
    
    cout << "Brute: ";
    magicBrute(testC, 10);
    cout << endl << "Better: " << magicBetter(testC, 10, 0, 9, 5) << endl;
    
    return 0;
}

// Brute Force
// O(n) time, O(1) space
// Pretty straightforward and works for all proper int arrays, even duplicates
// and unsorted
void magicBrute(int array[], int length) {
    for(int index = 0; index < length; index++) {
        if(array[index] == index) {
            cout << index << " ";
        }
    }
}

// Improved
// O(logn) time, O(1) space
// This version assumes that the array is sorted and returns only one
int magicBetter(int array[], int length, int start, int end, int mid) {
    if(end < start || start < 0 || end >= length || mid < 0) {
        return -1;
    }
    
    if(array[mid] == mid) {
        return mid;
    }
    
    if(array[mid] < mid) {
        return magicBetter(array, length, mid+1, end, mid + ((end-mid)/2));
    } else {
        return magicBetter(array, length, start, mid, start + (mid/2));
    }
}