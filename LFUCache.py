'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
'''
from collections import OrderedDict  # LinkedHashMap in Java


class LFUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# param_1 = obj.get(3)
# obj.put(3,3)

if __name__ == '__main__':
    lfu = LFUCache(2);
    print(lfu.put(1, 1)); # cache is {1 = 1}
    print(lfu.put(2, 2)); # cache is {1 = 1, 2 = 2}
    print(lfu.get(1)); # return 1
    print(lfu.put(3, 3)); # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
    print('### cache is now ', lfu)
    print(lfu.get(2)); # returns - 1(not found)
    print(lfu.get(3)); #return 3 - cache = [3, 1], cnt(3) = 2, cnt(1) = 2
    print(lfu.put(4, 4)); # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    print(lfu.get(1)); # return -1(not found)
    print(lfu.get(3)); # return 3
    print(lfu.get(4)); # return 4
