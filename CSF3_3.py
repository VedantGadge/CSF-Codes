class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = -1  # Initially set to -1 to indicate it hasn't been set yet

# Function to implement Pre-emptive Priority Scheduling
def preemptive_priority_scheduling(processes):
    time = 0
    n = len(processes)
    completed = 0
    current_process = None
    
    while completed != n:
        # Find process with highest priority that has arrived and has remaining time
        highest_priority = float('inf')
        next_process = None
        
        for process in processes:
            if (process.arrival_time <= time and process.remaining_time > 0 and process.priority < highest_priority):
                highest_priority = process.priority
                next_process = process
        
        if next_process is None:  # No process is ready to run
            time += 1
            continue
        
        if current_process != next_process:
            current_process = next_process
        
        # Set the response time if the process is getting the CPU for the first time
        if current_process.response_time == -1:
            current_process.response_time = time - current_process.arrival_time
        
        # Execute the process for one unit of time
        current_process.remaining_time -= 1
        time += 1
        
        # If process is completed
        if current_process.remaining_time == 0:
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1
    
    # Calculate average waiting time, turnaround time, and response time
    total_waiting_time = sum([p.waiting_time for p in processes])
    total_turnaround_time = sum([p.turnaround_time for p in processes])
    total_response_time = sum([p.response_time for p in processes])
    
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    average_response_time = total_response_time / n
    
    return average_waiting_time, average_turnaround_time, average_response_time, processes

# Example usage
processes = [
    Process(1, 0, 9, 2),
    Process(2, 1, 4, 1),
    Process(3, 2, 9, 3)
]

average_waiting_time, average_turnaround_time, average_response_time, completed_processes = preemptive_priority_scheduling(processes)

for process in completed_processes:
    print(f"Process {process.pid}: Waiting Time = {process.waiting_time} ms, Turnaround Time = {process.turnaround_time} ms, Completion Time = {process.completion_time} ms, Response Time = {process.response_time} ms")

# Print results
print(f"\nAverage Waiting Time: {average_waiting_time:.2f} ms")
print(f"Average Turnaround Time: {average_turnaround_time:.2f} ms")
print(f"Average Response Time: {average_response_time:.2f} ms")
