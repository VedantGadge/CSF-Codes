def calculate_sjf_times(arrival_times, burst_times):
    num_processes = len(burst_times)
    
    # Initialize lists to store times
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    completion_times = [0] * num_processes
    start_times = [0] * num_processes
    
    # Create a list of processes with (arrival time, burst time, index)
    processes = sorted([(arrival_times[i], burst_times[i], i) for i in range(num_processes)])
    
    current_time = 0
    for i in range(num_processes):
        arrival_time, burst_time, index = processes[i]
        
        # Start the process only after its arrival time
        if current_time < arrival_time:
            current_time = arrival_time
        
        # Calculate start and completion times
        start_times[index] = current_time
        completion_times[index] = current_time + burst_time
        
        # Calculate turnaround and waiting times
        turnaround_times[index] = completion_times[index] - arrival_times[index]
        waiting_times[index] = turnaround_times[index] - burst_times[index]
        
        # Update current time
        current_time = completion_times[index]
    
    return completion_times, turnaround_times, waiting_times


def print_table2(arrival_times, burst_times):
    print(f"{'Process':<10} {'AT':<10} {'BT':<10}")
    print("-" * 30)
    for i in range(len(burst_times)):
        print(f"Process {i+1:<2} {arrival_times[i]:<10} {burst_times[i]:<10}")


def print_table(arrival_times, burst_times, completion_times, turnaround_times, waiting_times):
    print(f"{'Process':<10} {'AT':<10} {'BT':<10} {'CT':<10} {'TAT':<10} {'WT':<10}")
    print("-" * 60)
    for i in range(len(burst_times)):
        print(f"Process {i+1:<2} {arrival_times[i]:<10} {burst_times[i]:<10} {completion_times[i]:<10} "
              f"{turnaround_times[i]:<10} {waiting_times[i]:<10}")


def print_gantt_chart(arrival_times, burst_times, completion_times):
    num_processes = len(burst_times)
    
    # Create the Gantt chart representation
    gantt_chart = "Gantt Chart:\n"
    gantt_line = ""
    current_time = 0
    
    for i in range(num_processes):
        gantt_line += f"{current_time}->P{i+1}->" + str(completion_times[i]) + " "
        current_time = completion_times[i]
    
    print(gantt_chart)
    print(gantt_line)


def main():
    # Input number of processes
    num_processes = int(input("Enter the number of processes: "))
    
    # Initialize arrival times and burst times lists
    arrival_times = []
    burst_times = []
    
    # Input arrival and burst times
    print("Enter the arrival and burst times for each process:")
    for i in range(num_processes):
        arrival_time = int(input(f"Enter the Arrival time for Process P{i+1}: "))
        burst_time = int(input(f"Enter the Burst time for Process P{i+1}: "))
        
        arrival_times.append(arrival_time)
        burst_times.append(burst_time)
    
    # Calculate times using SJF
    completion_times, turnaround_times, waiting_times = calculate_sjf_times(arrival_times, burst_times)
    
    # Calculate average waiting time and average turnaround time
    average_waiting_time = sum(waiting_times) / num_processes
    average_turnaround_time = sum(turnaround_times) / num_processes
    
    # Print the inputs
    print("\nEntered inputs are:")
    print_table2(arrival_times, burst_times)
    print("\n")
    
    # Print Gantt Chart
    print_gantt_chart(arrival_times, burst_times, completion_times)
    print("\n")
    
    # Print the results in table format
    print_table(arrival_times, burst_times, completion_times, turnaround_times, waiting_times)
    
    # Print average waiting time and average turnaround time
    print(f"\nAverage Turnaround Time: {average_turnaround_time:.2f}")
    print(f"Average Waiting Time: {average_waiting_time:.2f}")


if __name__ == "__main__":
    main()