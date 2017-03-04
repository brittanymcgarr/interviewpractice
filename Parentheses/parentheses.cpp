/*
Nested Parentheses

Given an integer, n, generate all possible, closed parentheses combinations

e.g. n = 3 => ((())), ()()(), (())(), ()(()), (()())
*/

#include <iostream>
#include <vector>

using namespace std;

vector<string> generateParentheses(int count);
void NParentheses(vector<string>& list, int leftRem, int rightRem, char* str, int count);

int main() {
    vector<string> results;
    int choice = -1;
    
    while(choice <= 0) {
        cout << "Choose a number greater than 0: ";
        
        if(cin >> choice && choice > 0) {
            cout << "Chose " << choice << " parentheses." << endl;
        }
    }
    
    results = generateParentheses(choice);
    
    cout << "Generated " << results.size() << " results" << endl << "Your results:" << endl;
    for(int index = 0; index < results.size(); index++) {
        cout << results[index] << endl;
    }
    
    return 0;
}

// Wrapper Function
// Calls the NParentheses generator
vector<string> generateParentheses(int count) {
    char* str = new char[2*count];
    vector<string> list;
    
    NParentheses(list, count, count, str, 0);
    
    return list;
}

// Parentheses Generator
// Recursively calls itself on each set of left and corresponding right parentheses
// and stores the results in the given vector for return to wrapper.
void NParentheses(vector<string>& list, int leftRem, int rightRem, char* str, int count) {
    if(leftRem < 0 || rightRem < leftRem) {
        return;
    }
    
    if(leftRem == 0 && rightRem == 0) {
        string hold(str);
        list.push_back(hold);
    } else {
        if(leftRem > 0) {
            str[count] = '(';
            NParentheses(list, leftRem - 1, rightRem, str, count + 1);
        }
        
        if(rightRem > leftRem) {
            str[count] = ')';
            NParentheses(list, leftRem, rightRem - 1, str, count + 1);
        }
    }
}