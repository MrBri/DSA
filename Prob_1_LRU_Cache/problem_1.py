import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) >= self.cap:
            self.cache.popitem(last=False) # Remove oldest
        self.cache[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print('get 1', our_cache.get(1), our_cache.cache, our_cache.cap)       # returns 1
print('get 2', our_cache.get(2), our_cache.cache, our_cache.cap)       # returns 2
print('get 9', our_cache.get(9), our_cache.cache, our_cache.cap)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print('get 3', our_cache.get(3), our_cache.cache, our_cache.cap)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

cache = LRU_Cache(2)
cache.set(0, 0)
cache.set(0, 0)
cache.set(0, 0)

print('get 0', cache.get(0), cache.cache, cache.cap)       # returns 0
print('get 0', cache.get(0), cache.cache, cache.cap)       # returns 0
print('get 0', cache.get(0), cache.cache, cache.cap)       # returns 0

# Test Case 2
cache = LRU_Cache(2)
cache.set("", "")
cache.set("", "")
cache.set("", "")

print('get blank', cache.get(""), cache.cache, cache.cap)       # returns ''
print('get 0', cache.get(0), cache.cache, cache.cap)       # returns -1

# Test Case 3
cache = LRU_Cache(10)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)
cache.set(5, 5)
cache.set(6, 6)
cache.set(7, 7)
cache.set(8, 8)
cache.set(9, 9)
cache.set(10, 10)
cache.set(11, 11)
cache.set(12, 12)

print('get 1', cache.get(1), cache.cache, cache.cap)       # returns 0
print('get 0', cache.get(0), cache.cache, cache.cap)       # returns 0
print('get 3', cache.get(3), cache.cache, cache.cap)       # returns 0

# Show Me the Data Structures
