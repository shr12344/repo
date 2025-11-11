#10. Paging Simulation (Basic)

import math
def paging_simulator(process_size, page_size):
    num_pages = math.ceil(process_size / page_size)
    page_table = {f"Page {i}": f"Frame {i}" for i in range(num_pages)}
    return page_table

table = paging_simulator(1024, 256)

for k, v in table.items():
    print(f"{k} → {v}")
