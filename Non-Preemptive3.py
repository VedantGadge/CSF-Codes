def calculate_priority_times(arrival_times, burst_times, priorities):
    num_processes = len(burst_times)
    
    # Initialize lists to store times
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    completion_times = [0] * num_processes
    
    # Create a list of process indices and sort based on priority, considering arrival times
    sorted_indices = sorted(range(num_processes), key=lambda i: (arrival_times[i], priorities[i]))
    
    current_time = 0
    for i in range(num_processes):
        index = sorted_indices[i]
        
        # Process only after its arrival time
        if current_time < arrival_times[index]:
            current_time = arrival_times[index]
        
        # Calculate completion, turnaround, and waiting times
        completion_times[index] = current_time + burst_times[index]
        turnaround_times[index] = completion_times[index] - arrival_times[index]
        waiting_times[index] = turnaround_times[index] - burst_times[index]
        
        # Update current time
        current_time = completion_times[index]
    
    return completion_times, turnaround_times, waiting_times


def print_table2(arrival_times, burst_times, priorities):
    print(f"{'Process':<10} {'AT':<10} {'BT':<10} {'Priority':<10}")
    print("-" * 40)
    for i in range(len(burst_times)):
        print(f"Process {i+1:<2} {arrival_times[i]:<10} {burst_times[i]:<10} {priorities[i]:<10}")


def print_table(arrival_times, burst_times, priorities, completion_times, turnaround_times, waiting_times):
    print(f"{'Process':<10} {'AT':<10} {'BT':<10} {'Priority':<10} {'CT':<10} {'TAT':<10} {'WT':<10}")
    print("-" * 70)
    for i in range(len(burst_times)):
        print(f"Process {i+1:<2} {arrival_times[i]:<10} {burst_times[i]:<10} {priorities[i]:<10} "
              f"{completion_times[i]:<10} {turnaround_times[i]:<10} {waiting_times[i]:<10}")


def print_gantt_chart(arrival_times, burst_times, completion_times, priorities):
    num_processes = len(burst_times)
    
    # Create the Gantt chart representation
    gantt_chart = "Gantt Chart:\n"
    gantt_line = ""
    
    # Create a list of process indices sorted by priority
    sorted_indices = sorted(range(num_processes), key=lambda i: (arrival_times[i], priorities[i]))
    current_time = 0
    
    for i in sorted_indices:
        # Update the Gantt chart
        if current_time < arrival_times[i]:
            current_time = arrival_times[i]
        gantt_line += f"{current_time}->P{i+1}->" + str(completion_times[i]) + " "
        current_time = completion_times[i]
    
    print(gantt_chart)
    print(gantt_line)


def main():
    # Input number of processes
    num_processes = int(input("Enter the number of processes: "))
    
    # Input arrival times, burst times, and priorities
    arrival_times = []
    burst_times = []
    priorities = []
    
    print("Enter the arrival times, burst times, and priorities for each process:")
    for i in range(num_processes):
        arrival_time = int(input(f"Enter the Arrival time for process P{i+1}: "))
        burst_time = int(input(f"Enter the Burst time for process P{i+1}: "))
        priority = int(input(f"Enter the Priority for process P{i+1} (lower value = higher priority): "))
        
        arrival_times.append(arrival_time)
        burst_times.append(burst_time)
        priorities.append(priority)
    
    # Calculate times using Priority Scheduling
    completion_times, turnaround_times, waiting_times = calculate_priority_times(arrival_times, burst_times, priorities)
    
    # Calculate average waiting time and average turnaround time
    average_waiting_time = sum(waiting_times) / num_processes
    average_turnaround_time = sum(turnaround_times) / num_processes
    
    # Print the inputs
    print("\nEntered inputs are:")
    print_table2(arrival_times, burst_times, priorities)
    print("\n")
    
    # Print Gantt Chart
    print_gantt_chart(arrival_times, burst_times, completion_times, priorities)
    print("\n")
    
    # Print the results in table format
    print_table(arrival_times, burst_times, priorities, completion_times, turnaround_times, waiting_times)
    
    # Print average waiting time and average turnaround time
    print(f"\nAverage Turnaround Time: {average_turnaround_time:.2f}")
    print(f"Average Waiting Time: {average_waiting_time:.2f}")


if __name__ == "__main__":
    main()