#Memory Management in OS
#7. Simulate Memory Allocation (Static&Dynamic)

memory = [None] * 100

def allocate(process_id, size):
    for i in range(len(memory) - size + 1):
        if all(block is None for block in memory[i:i+size]):
            for j in range(i, i+size):
                memory[j] = process_id
        return f"Allocated {size} blocks to {process_id} at {i}"
    return "Insufficient memory"

def deallocate(process_id):
    count = memory.count(process_id)
    for i in range(len(memory)):
        if memory[i] == process_id:
            memory[i] = None
        return f"Deallocated {count} blocks from {process_id}"
    

print(allocate("P1", 10))
print(allocate("P2", 20))
print(deallocate("P1"))
