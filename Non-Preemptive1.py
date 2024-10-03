def calculate_times(burst_times, arrival_times):
    num_processes = len(burst_times)
    
    # Initialize lists to store times
    waiting_times = [0] * num_processes
    finish_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    
    # Variables to keep track of time
    current_time = 0
    
    # Calculate Finish Times, Waiting Times, and Turnaround Times
    for i in range(num_processes):
        # The process starts execution at max(current_time, arrival_times[i])
        start_time = max(current_time, arrival_times[i])
        finish_times[i] = start_time + burst_times[i]
        turnaround_times[i] = finish_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]
        
        # Update current time
        current_time = finish_times[i]
    
    return finish_times, turnaround_times, waiting_times

def print_table2(arrival_times, burst_times):
    print(f"{'Process':<10} {'AT':<10} {'BT':<10}")
    print("-" * 30)
    for i in range(len(burst_times)):
        print(f"Process {i+1:<2} {arrival_times[i]:<10} {burst_times[i]:<10}")

def print_table(arrival_times, burst_times, finish_times, turnaround_times, waiting_times):
    print(f"{'Process':<10} {'AT':<10} {'BT':<10} {'FT':<10} {'TAT':<10} {'WT':<10}")
    print("-" * 60)
    for i in range(len(burst_times)):
        print(f"Process {i+1:<2} {arrival_times[i]:<10} {burst_times[i]:<10} {finish_times[i]:<10} "
              f"{turnaround_times[i]:<10} {waiting_times[i]:<10}")

def print_gantt_chart(arrival_times, burst_times, finish_times):
    num_processes = len(burst_times)
    gantt_chart = ""
    current_time = 0
    
    # Build the Gantt chart representation
    gantt_chart += "0"
    for i in range(num_processes):
        start_time = max(current_time, arrival_times[i])
        gantt_chart += " -> P" + str(i + 1)
        gantt_chart += " -> " + str(finish_times[i])
        current_time = finish_times[i]
    
    print("Gantt Chart:")
    print(gantt_chart)

# Input number of processes
num_processes = int(input("Enter the number of processes: "))

# Input arrival times
arrival_times = []
print("Enter the arrival times for each process:")
for i in range(num_processes):
    arrival_time = int(input(f"Enter the Arrival time for process P{i+1}: "))
    arrival_times.append(arrival_time)

# Input burst times
burst_times = []
print("Enter the burst times for each process:")
for i in range(num_processes):
    burst_time = int(input(f"Enter the Burst time for Process P{i+1}: "))
    burst_times.append(burst_time)

# Calculate times
finish_times, turnaround_times, waiting_times = calculate_times(burst_times, arrival_times)

# Print Inputs
print("\n")
print_table2(arrival_times, burst_times)

# Print Gantt Chart
print("\n")
print_gantt_chart(arrival_times, burst_times, finish_times)
print("\n")

# Calculate average waiting time
average_waiting_time = sum(waiting_times) / num_processes
# Calculate average turnaround time
average_turnaround_time = sum(turnaround_times) / num_processes

# Print the results in table format
print_table(arrival_times, burst_times, finish_times, turnaround_times, waiting_times)

# Print average times
print(f"\nAverage Turnaround Time: {average_turnaround_time:.2f}")
print(f"Average Waiting Time: {average_waiting_time:.2f}")