/*
Duplicates

Given an array of integers, 1-N, find the duplicate entries.

e.g. A = {1, 2, 1, 3, 4, 5, 6} => 1

1.) Assume only one integer is duplicated and that the array of size N+1 contains
    all entries 1-N. O(n) time and O(1) space.
    e.g. A = {1, 2, 1, 3, 4, 5, 6} N = 6 => 1
    
2.) Assume many duplicates are in the array with no bounds on value. 
    O(n) time and O(n) space.
    e.g. A = {-1, 4, 8, 7, 2, 2, -1} => -1, 2
    
3.) Assume all values are in the range 1-N and unsorted. There may be multiple.
    O(n) time and O(1) space.
    e.g. A = {8, 3, 2, 1, 4, 1, 2} => 1, 2

*/

#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <unordered_set>

using namespace std;

int duplicatesA(vector<int>&);
vector<int> duplicatesB(vector<int>&);
void duplicatesC(vector<int>);
unordered_set<int> duplicatesD(vector<int>);

int main() {
    vector<int> testA;
    vector<int> testB;
    vector<int> testC;
    
    srand(time(NULL));
    
    for(int index = 1; index < 10; index++) {
        testA.push_back(index);
    }
    testA.push_back(1);
    
    for(int index = 0; index < 20; index++) {
        int random = rand() % 19 + (-9);
        testB.push_back(random);
    }
    
    for(int index = 0; index < 20; index++) {
        int random = rand() % 20;
        testC.push_back(random);
    }
    
    cout << "First Test: " << endl;
    for(const int& index : testA) {
        cout << index << ", ";
    }
    cout << endl << "Result: " << duplicatesA(testA) << endl << endl;
    
    cout << "Second Test: " << endl;
    for(const int& index : testB) {
        cout << index << ", ";
    }
    cout << endl << "Result: ";
    vector<int> results = duplicatesB(testB);
    for(const int& index : results) {
        cout << index << ", ";
    }
    cout << endl << endl;
    
    cout << "Third Test: " << endl;
    for(const int& index : testC) {
        cout << index << ", ";
    }
    cout << endl << "Result: ";
    duplicatesC(testC);
    cout << endl;
    
    cout << "Bonus to Third Test: " << endl;
    unordered_set<int> found = duplicatesD(testC);
    for(const int& value : found) {
        cout << value << ", ";
    }
    cout << endl;
    
    return 0;
}


// One duplicate
// O(n) time O(1) space
// If the array is a legal entry containing all 1-N values, then this method
// relies on a fast calculation of the projected sum of all integers and 
// deducts that from the iterated tally of the actual elements.
int duplicatesA(vector<int>& A) {
    int size = A.size() - 1;
    int projected = (size * (size+1)) / 2;
    int tally = 0;
    
    for(int index = 0; index < size + 1; index++) {
        tally += A[index];
    }
    
    return tally - projected;
}

// Many Duplicates Random Values
// O(n) time, O(n) space
// Because there are no guarantees about the input data, including sign,
// we are forced to collect the duplicate entries and iterate through the
// detected duplicates for uniqueness. Maximum space for each set and 
// results would be n (1/2 n if all entries are duplicates)
vector<int> duplicatesB(vector<int>& A) {
    unordered_set<int> found;
    unordered_set<int> duplicates;
    vector<int> results;
    
    for(int index = 0; index < A.size(); index++) {
        if(found.find(A[index]) != found.end()) {
            duplicates.insert(A[index]);
        } else {
            found.insert(A[index]);
        }
    }
    
    for(const int& value : duplicates) {
        results.push_back(value);
    }
    
    return results;
}

// Multiple Duplicates All 1-N
// O(n) time, O(1) space
// This method takes advantage of the integers within the array's length and
// positive. A detected integer is converted to an offset and checked for its 
// sign. If the integer at the offset is negative, another element has used that
// position, meaning they were already there and the new is a duplicate.
// Downsides: multiples are repeated and integers cannot be zero or less.
void duplicatesC(vector<int> A) {
    for(int index = 0; index < A.size(); index++) {
        if(A[abs(A[index])] < 0) {
            cout << abs(A[index]) << " ";
        } else {
            A[abs(A[index])] *= -1;
        }
    }
}

// Uniqueness fix for duplicatesC
// O(n) time, up to O(0.5n) space
unordered_set<int> duplicatesD(vector<int> A) {
    unordered_set<int> found;
    
    for(int index = 0; index < A.size(); index++) {
        if(A[abs(A[index])] < 0) {
            found.insert(abs(A[index]));
        } else {
            A[abs(A[index])] *= -1;
        }
    }
    
    return found;
}