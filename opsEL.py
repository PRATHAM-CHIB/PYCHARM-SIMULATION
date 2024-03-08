import matplotlib.pyplot as plt

# Function for First Fit Allocation (Modified)
def first_fit(memory_blocks, program_sizes):
    allocation_sequence = []
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Define colors for programs
    for idx, size in enumerate(program_sizes):
        allocated_block = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size:
                memory_blocks[i] -= size
                allocated_block = i
                break
        allocation_sequence.append((allocated_block, colors[idx]))
    return allocation_sequence

# Function for Worst Fit Allocation (Modified)
def worst_fit(memory_blocks, program_sizes):
    allocation_sequence = []
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Define colors for programs
    for idx, size in enumerate(program_sizes):
        max_block_index = -1
        max_block_size = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size and memory_blocks[i] > max_block_size:
                max_block_index = i
                max_block_size = memory_blocks[i]
        if max_block_index != -1:
            memory_blocks[max_block_index] -= size
        allocation_sequence.append((max_block_index, colors[idx]))
    return allocation_sequence

# Function for Best Fit Allocation (Modified)
def best_fit(memory_blocks, program_sizes):
    allocation_sequence = []
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Define colors for programs
    for idx, size in enumerate(program_sizes):
        best_fit_index = -1
        min_remaining_space = float('inf')
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size and memory_blocks[i] - size < min_remaining_space:
                best_fit_index = i
                min_remaining_space = memory_blocks[i] - size
        if best_fit_index != -1:
            memory_blocks[best_fit_index] -= size
        allocation_sequence.append((best_fit_index, colors[idx]))
    return allocation_sequence

# User input for free segments and programs
memory_blocks = []
num_segments = int(input("Enter the number of free memory segments: "))
for i in range(num_segments):
    size = int(input(f"Enter the size of free segment {i+1}: "))
    memory_blocks.append(size)

num_programs = int(input("Enter the number of programs: "))
program_sizes = []
for i in range(num_programs):
    size = int(input(f"Enter the size of program {i+1}: "))
    program_sizes.append(size)

# Visualization of memory allocation using different algorithms for all programs in the same free memory segment
allocation_methods = [first_fit, worst_fit, best_fit]
method_names = ['First Fit', 'Worst Fit', 'Best Fit']

for method, name in zip(allocation_methods, method_names):
    memory_blocks_copy = memory_blocks.copy()
    allocation_sequence = method(memory_blocks_copy, program_sizes)

    plt.figure()
    plt.title(f'{name} Allocation for All Programs')
    plt.bar(range(len(memory_blocks)), memory_blocks, color='skyblue', label='Free Memory')
    for block_index, color in allocation_sequence:
        if block_index != -1:
            plt.bar(block_index, program_sizes[allocation_sequence.index((block_index, color))], color=color, label=f'Program {allocation_sequence.index((block_index, color))} Allocated')
    plt.xlabel('Memory Block')
    plt.ylabel('Memory Size')
    plt.legend()
    plt.show()
import matplotlib.pyplot as plt

# Function for First Fit Allocation (Modified)
def first_fit(memory_blocks, program_sizes):
    allocation_sequence = []
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Define colors for programs
    for idx, size in enumerate(program_sizes):
        allocated_block = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size:
                memory_blocks[i] -= size
                allocated_block = i
                break
        allocation_sequence.append((allocated_block, colors[idx]))
    return allocation_sequence

# Function for Worst Fit Allocation (Modified)
def worst_fit(memory_blocks, program_sizes):
    allocation_sequence = []
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Define colors for programs
    for idx, size in enumerate(program_sizes):
        max_block_index = -1
        max_block_size = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size and memory_blocks[i] > max_block_size:
                max_block_index = i
                max_block_size = memory_blocks[i]
        if max_block_index != -1:
            memory_blocks[max_block_index] -= size
        allocation_sequence.append((max_block_index, colors[idx]))
    return allocation_sequence

# Function for Best Fit Allocation (Modified)
def best_fit(memory_blocks, program_sizes):
    allocation_sequence = []
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Define colors for programs
    for idx, size in enumerate(program_sizes):
        best_fit_index = -1
        min_remaining_space = float('inf')
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size and memory_blocks[i] - size < min_remaining_space:
                best_fit_index = i
                min_remaining_space = memory_blocks[i] - size
        if best_fit_index != -1:
            memory_blocks[best_fit_index] -= size
        allocation_sequence.append((best_fit_index, colors[idx]))
    return allocation_sequence

# User input for free segments and programs
memory_blocks = []
num_segments = int(input("Enter the number of free memory segments: "))
for i in range(num_segments):
    size = int(input(f"Enter the size of free segment {i+1}: "))
    memory_blocks.append(size)

num_programs = int(input("Enter the number of programs: "))
program_sizes = []
for i in range(num_programs):
    size = int(input(f"Enter the size of program {i+1}: "))
    program_sizes.append(size)

# Visualization of memory allocation using different algorithms for all programs in the same free memory segment
allocation_methods = [first_fit, worst_fit, best_fit]
method_names = ['First Fit', 'Worst Fit', 'Best Fit']

for method, name in zip(allocation_methods, method_names):
    memory_blocks_copy = memory_blocks.copy()
    allocation_sequence = method(memory_blocks_copy, program_sizes)

    plt.figure()
    plt.title(f'{name} Allocation for All Programs')
    plt.bar(range(len(memory_blocks)), memory_blocks, color='skyblue', label='Free Memory')
    for block_index, color in allocation_sequence:
        if block_index != -1:
            plt.bar(block_index, program_sizes[allocation_sequence.index((block_index, color))], color=color, label=f'Program {allocation_sequence.index((block_index, color))} Allocated')
    plt.xlabel('Memory Block')
    plt.ylabel('Memory Size')
    plt.legend()
    plt.show()
