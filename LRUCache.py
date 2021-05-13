'''Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
'''


from collections import OrderedDict  # LinkedHashMap in Java


class LRUCache(OrderedDict):

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
    lRUCache = LRUCache(2);
    print(lRUCache.put(1, 1)); # cache is {1 = 1}
    print(lRUCache.put(2, 2)); # cache is {1 = 1, 2 = 2}
    print(lRUCache.get(1)); # return 1
    print(lRUCache.put(3, 3)); # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
    print('### cache now is ', lRUCache)
    print(lRUCache.get(2)); # returns - 1(not found)
    print(lRUCache.put(4, 4)); # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    print(lRUCache.get(1)); # return -1(not found)
    print(lRUCache.get(3)); # return 3
    print(lRUCache.get(4)); # return 4
