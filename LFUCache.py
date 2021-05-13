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