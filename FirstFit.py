b_size = {}
p_size = {}
allocation = {}

nb = int(input("Enter the number of Blocks: "))
np = int(input("Enter the number of Processes: "))

for i in range(nb):
    a = int(input(f"Enter size of memory block {i + 1}: "))
    b_size[i] = a

for i in range(np):
    b = int(input(f"Enter size of process {i + 1}: "))
    p_size[i] = b

for process_id, process_size in p_size.items():
    allocated = False
    for block_id, block_size in b_size.items():
        if process_size <= block_size:
            b_size[block_id] -= process_size
            allocation[process_id] = block_id
            allocated = True
            break
    if not allocated:
        allocation[process_id] = None

print("\nFirst Fit Allocation:")
for process_id in p_size:
    if allocation[process_id] is not None:
        print(f"Process {process_id + 1} of size {p_size[process_id]} allocated to Block {allocation[process_id] + 1}")
    else:
        print(f"Process {process_id + 1} of size {p_size[process_id]} could not be allocated.")

print("\nFragmentation in Memory Blocks:")
for block_id in b_size:
    print(f"Fragment of Block {block_id + 1}: {b_size[block_id]}")