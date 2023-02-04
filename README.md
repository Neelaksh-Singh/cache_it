# cache_it
A library providing in-memory, thread-safe caching for general use. Currently has provisions for LRU, FIFO and LIFO cache.

## 💻 Installation And Running

`!!! Having Python is a must. !!!` <br>

Python 3.6+ is required to run code from this repo. 

```console
$ git clone https://github.com/Neelaksh-Singh/cache_it.git
$ cd cache_it/
```
You can initiate the <b>cache object</b>, present in `cache.py`, by passing the desired cache technique along with cache size.

## Custom Cache
You can create your custom cache and adding it to `eviction_policies` folder. For maintanibilty, you can use the [template](eviction_policies/template.py) standard.
