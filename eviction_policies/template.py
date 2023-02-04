import threading


class < cache_name >:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.store = <custom_ds >

    def insert(self, key, value):

        with threading.Lock():

            if key in self.cache:
                self.cache[key] = value

            elif self.store.qsize() == self.capacity:
                self.remove()
                self.cache[key] = value
                item = (key, value)
                self.store.put(item)
            else:
                self.cache[key] = value
                item = (key, value)
                self.store.put(item)

        # print(self.cache)
        # print("================================")
        # print("================================")

    def remove(self):

        key, _ = self.store.get()
        # print("::::::::::::::::::::::::::::::::::::::::::::")
        # print("::::::::::::::::::::::::::::::::::::::::::::")
        # print(self.cache)
        # print("::::::::::::::::::::::::::::::::::::::::::::")
        # print("::::::::::::::::::::::::::::::::::::::::::::")
        self.cache.pop(key)

    def get(self, key):

        with threading.Lock():

            if key in self.cache:

                return self.cache[key]

            else:

                raise KeyError("Not found!")


cc = <cache_name > (5)
cc.insert(1, 'a')
cc.insert(2, 'b')
cc.insert(3, 'c')
cc.insert(4, 'd')
cc.insert(5, 'e')
cc.get(1)
cc.insert(6, 'f')
