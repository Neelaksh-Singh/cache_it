from eviction_policies.lifo import LIFO
from eviction_policies.lru import LRU
from eviction_policies.fifo import FIFO


class Enter:
    def __init__(self):
        pass

    def init_cache(self, cache_type, capacity):
        cache_type = cache_type.lower()
        if cache_type == 'lifo':
            return LIFO(capacity)
        elif cache_type == 'fifo':
            return FIFO(capacity)
        elif cache_type == 'lru':
            return LRU(capacity)
        else:
            raise Exception("!! No such eviction policy present !!")

# cc = Enter()
# cc.init_cache('lmuT',10)
