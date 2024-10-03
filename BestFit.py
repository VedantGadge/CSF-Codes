b_size = {}
p_size = {}
allocation = {}

nb = int(input("Enter the number of Blocks: "))
np = int(input("Enter the number of Processes: "))

# Input memory block sizes
for i in range(nb):
    a = int(input(f"Enter size of memory block {i + 1}: "))
    b_size[i] = a

# Input process sizes
for i in range(np):
    b = int(input(f"Enter size of process {i + 1}: "))
    p_size[i] = b

# Best Fit memory allocation
for process_id, process_size in p_size.items():
    best_fit_block = None
    min_fragment = float('inf')
    
    # Finding the best fitting block
    for block_id, block_size in b_size.items():
        if process_size <= block_size and (block_size - process_size) < min_fragment:
            min_fragment = block_size - process_size
            best_fit_block = block_id
    
    # Allocate the block if found
    if best_fit_block is not None:
        b_size[best_fit_block] -= process_size
        allocation[process_id] = best_fit_block
    else:
        allocation[process_id] = None

# Output the allocation results
print("\nBest Fit Allocation:")
for process_id in p_size:
    if allocation[process_id] is not None:
        print(f"Process {process_id + 1} of size {p_size[process_id]} allocated to Block {allocation[process_id] + 1}")
    else:
        print(f"Process {process_id + 1} of size {p_size[process_id]} could not be allocated.")

# Output the remaining fragments in blocks
print("\nFragmentation in Memory Blocks:")
for block_id in b_size:
    print(f"Fragment of Block {block_id + 1}: {b_size[block_id]}")