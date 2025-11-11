#9. Garbage Collection Visualization

import gc
import sys

a = [1] * (10**6)
print("Memory used:", sys.getsizeof(a), "bytes")

del a

gc.collect()
print("Garbage collected")
