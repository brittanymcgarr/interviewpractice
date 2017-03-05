/*
    Lowest Ancestor
    
    Given a binary tree of integer values and two values in the tree, return the 
    value of their lowest, shared ancestor. You may assume that the values are
    positive, unique, and that -1 indicates neither value was present. (Either
    value without the other's present is acceptable as a return.)
    
    e.g.
                5
              /   \
             3     7
            / \   / \
           1   4 6   9
         
        Input: root, 1, 4 => 3
        Input: root, 1, 7 => 5
        Input: root, 5, 7 => 5
        Input: root, 1, 10 => -1

    1.) If the tree is a Binary Search Tree and ordering is guaranteed
    2.) If the tree is a Binary Tree and the ordering is NOT guaranteed
                1
              /   \
             5     3
            / \   / \
           2   4 6   9
        
        Input: root, 1, 4 => 1
        Input: root, 5, 6 => 1
        Input: root, 2, 4 => 5
        Input: root, 1, 10 => -1
*/

#include <iostream>

using namespace std;

struct BTNode {
    BTNode* left;
    BTNode* right;
    int data;
};

int lowestAncestor(BTNode*, int, int);
int lowestAncestorUnordered(BTNode*, int, int);

int main() {
    BTNode* testTree = new BTNode();
    
    testTree->data = 5;
    testTree->left = new BTNode();
    testTree->right = new BTNode();
    testTree->left->data = 3;
    testTree->right->data = 7;
    testTree->left->left = new BTNode();
    testTree->left->right = new BTNode();
    testTree->right->left = new BTNode();
    testTree->right->right = new BTNode();
    testTree->left->left->data = 1;
    testTree->left->right->data = 4;
    testTree->right->left->data = 6;
    testTree->right->right->data = 9;
    testTree->left->left->left = NULL;
    testTree->left->left->right = NULL;
    testTree->left->right->left = NULL;
    testTree->left->right->right = NULL;
    testTree->right->left->left = NULL;
    testTree->right->left->right = NULL;
    testTree->right->right->left = NULL;
    testTree->right->right->right = NULL;
    
    cout << "First testing tree inputs 1, 4: Expecting 3" << endl;
    cout << lowestAncestor(testTree, 1, 4) << endl << endl;
    
    cout << "First testing tree inputs 1, 7: Expecting 5" << endl;
    cout << lowestAncestor(testTree, 1, 7) << endl << endl;
    
    cout << "First testing tree inputs 5, 7: Expecting 5" << endl;
    cout << lowestAncestor(testTree, 5, 7) << endl << endl;
    
    cout << "First testing tree inputs 11, 10: Expecting -1" << endl;
    cout << lowestAncestor(testTree, 11, 10) << endl << endl;
    
    testTree->data = 1;
    testTree->left->data = 5;
    testTree->right->data = 3;
    testTree->left->left->data = 2;
    testTree->left->right->data = 4;
    
    cout << "Unordered testing tree inputs 1, 4: Expecting 1" << endl;
    cout << lowestAncestorUnordered(testTree, 1, 4) << endl << endl;
    
    cout << "Unordered testing tree inputs 5, 6: Expecting 1" << endl;
    cout << lowestAncestorUnordered(testTree, 5, 6) << endl << endl;
    
    cout << "Unordered testing tree inputs 2, 4: Expecting 5" << endl;
    cout << lowestAncestorUnordered(testTree, 2, 4) << endl << endl;
    
    cout << "Unordered testing tree inputs 11, 10: Expecting -1" << endl;
    cout << lowestAncestorUnordered(testTree, 11, 10) << endl << endl;
    
    delete testTree->left->left;
    delete testTree->left->right;
    delete testTree->left;
    delete testTree->right->left;
    delete testTree->right->right;
    delete testTree->right;
    delete testTree;
    
    return 0;
}

// Lowest Ancestor BST
// Because the values in the tree are ordered where lower values than the node
// are to the left, and higher values are to the right, we can assume that where
// the current root straddles the values is the lowest, common ancestor
// If the tree is somewhat balanced, 
// O(logn) time, O(1) space
// Otherwise,
// O(n) time, O(1) space
int lowestAncestor(BTNode* root, int valueA, int valueB) {
    if(root == NULL) {
        return -1;
    }
    
    if((root->data >= valueA && root->data <= valueB) || (root->data >= valueB && root->data <= valueA)) {
        return root->data;
    } else if(root->data >= valueA && root->data >= valueB) {
        return lowestAncestor(root->left, valueA, valueB);
    } else {
        return lowestAncestor(root->right, valueA, valueB);
    }
}

// Lowest Ancestor No guarantees
// Because the values in the tree are undecided, all values have to be examined
// sequentially. The end condition for a non-NULL root is one of the values 
// present in the root, which is passed up a level. If both were found on
// left and right branches, the current node is their parent, otherwise, both
// values would be in either the left or right branches and should be recursed
// again.
// O(n) time, O(1) space
int lowestAncestorUnordered(BTNode* root, int valueA, int valueB) {
    if(root == NULL) {
        return -1;
    }
    
    if(root->data == valueA) {
        return root->data;
    }
    
    if(root->data == valueB) {
        return root->data;
    }
    
    int lowestLeft = lowestAncestorUnordered(root->left, valueA, valueB);
    int lowestRight = lowestAncestorUnordered(root->right, valueA, valueB);
    
    if(lowestLeft >= 0 && lowestRight >= 0) {
        return root->data;
    } else if(lowestLeft >= 0) {
        return lowestAncestorUnordered(root->left, valueA, valueB);
    } else {
        return lowestAncestorUnordered(root->right, valueA, valueB);
    }
}
