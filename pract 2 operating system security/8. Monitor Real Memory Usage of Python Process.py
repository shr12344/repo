#8. Monitor Real Memory Usage of Python Process

import os, psutil

process = psutil.Process(os.getpid())

print(f" Current Memory Usage: {process.memory_info().rss / 1024**2:.2f} MB")
