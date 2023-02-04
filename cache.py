from entrypoint import Enter


class Cache:

    def __init__(self, cache_type, capacity):
        # self.capacity = capacity
        # self.cache_type = cache_type
        # print(self.cache_dict)

        self.cache = Enter().init_cache(cache_type, capacity)
        self.cache_store = self.cache.cache

    def add(self, key, value):
        self.cache.insert(key, value)

    def access(self, key):
        return self.cache.get(key)

    def display_cache(self):
        for key, value in self.cache_store.items():
            print("Key: ", key)
            print("Value: ", value)
            print("*********")


cc = Cache('lru', 3)
cc.add("A", 100)
cc.add("B", 200)
cc.add("C", 200)
cc.display_cache()
print("===================")
cc.add("A", 300)
cc.display_cache()
print("===================")
cc.add("D", 500)
cc.display_cache()
