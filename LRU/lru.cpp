/*
    Least Recently Used Cache - LeetCode
    https://leetcode.com/problems/lru-cache/?tab=Description
    
    Design and implement a data structure for Least Recently Used (LRU) cache. 
    It should support the following operations: get and put.
    
    get(key) - Get the value (will always be positive) of the key if the key 
    exists in the cache, otherwise return -1.
    
    put(key, value) - Set or insert the value if the key is not already present. 
    When the cache reached its capacity, it should invalidate the least recently 
    used item before inserting a new item.
    
    Follow up:
    Could you do both operations in O(1) time complexity?
    
    Example:

    LRUCache cache = new LRUCache( 2 ); // Capacity is 2
    
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
    
    STUB: Still working out the kinks on this one
*/

#include <iostream>
#include <unordered_map>
#include <vector>
#include <stdlib.h>

using namespace std;

// LRUCache Header
// Assuming only int, int key, value pairs. Otherwise, use template <class K, class V>
class LRUCache {
    // Accessible methods
    public:
    
    LRUCache(int);
    ~LRUCache();
    
    int get(int);
    void put(int, int);
    
    // Data members
    private:
    
    int capacity;
    vector<int> ordering;
    unordered_map<int,pair<int,int>> storage;
};

// Constructor
// Takes capacity for elements
LRUCache::LRUCache(int inCapacity) {
    capacity = inCapacity;
}

// Destructor
// Removes the storage
LRUCache::~LRUCache() {
    capacity = 0;
    ordering.clear();
    storage.clear();
}

// Get
// Checks for the value of the key and updates the cache as having been
// used recently. Returns -1 if the key is not present.
int LRUCache::get(int key) {
    if(storage.find(key) == storage.end()) {
        return -1;
    }
    
    pair<int,int> holdValue = storage.find(key)->second;
    
    ordering.erase(ordering.begin() + holdValue.second);
    ordering.push_back(key);
    
    holdValue.second = ordering.size() - 1;
    
    storage.erase(key);
    storage.insert(make_pair(key, holdValue));
    
    return holdValue.first;
}

// Put
// Puts the new value into the desired position and updates the most recently
// used ordering. If the key is not present or capacity is reached, removes the 
// least recently used item and emplaces the new value.
void LRUCache::put(int key, int value) {
    if(storage.find(key) != storage.end()) {
        pair<int,int> holdValue = storage.find(key)->second;
        
        holdValue.first = value;
        
        ordering.erase(ordering.begin() + holdValue.second);
        ordering.push_back(key);
        
        holdValue.second = ordering.size() - 1;
        storage.erase(key);
        storage.insert(make_pair(key, holdValue));
        
        return;
    }
    
    if(capacity <= ordering.size()) {
        int keyReplace = ordering[0];
        
        ordering.erase(ordering.begin());
        storage.erase(keyReplace);
    } 
    
    ordering.push_back(key);
    storage.insert(make_pair(key, make_pair(value, ordering.size() - 1)));
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */