# Define a class to represent a process
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1  # Initially set to -1 to indicate that it hasn't been set yet

# Function to implement SRTF scheduling
def srtf_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    
    while completed != n:
        # Find process with shortest remaining time that has arrived
        min_remaining_time = float('inf')
        shortest = None
        for process in processes:
            if process.arrival_time <= time and process.remaining_time > 0:
                if process.remaining_time < min_remaining_time:
                    min_remaining_time = process.remaining_time
                    shortest = process
        
        if shortest is None:  # No process is ready to run
            time += 1
            continue
        
        # Set the response time for the process if it's the first time it gets the CPU
        if shortest.response_time == -1:
            shortest.response_time = time - shortest.arrival_time
        
        # Execute the process for one unit of time
        shortest.remaining_time -= 1
        time += 1
        
        # If process is completed
        if shortest.remaining_time == 0:
            completed += 1
            shortest.completion_time = time
            shortest.turnaround_time = shortest.completion_time - shortest.arrival_time
            shortest.waiting_time = shortest.turnaround_time - shortest.burst_time
    
    # Calculate average waiting time, response time, and turnaround time
    total_waiting_time = sum([process.waiting_time for process in processes])
    total_response_time = sum([process.response_time for process in processes])
    total_turnaround_time = sum([process.turnaround_time for process in processes])
    
    average_waiting_time = total_waiting_time / n
    average_response_time = total_response_time / n
    average_turnaround_time = total_turnaround_time / n
    
    return average_waiting_time, average_response_time, average_turnaround_time, processes

# Example usage
processes = [
    Process(1, 0, 7),
    Process(2, 1, 5),
    Process(3, 2, 3),
    Process(4, 3, 1),
    Process(5, 4, 2),
    Process(6, 5, 1)
]

average_waiting_time, average_response_time, average_turnaround_time, completed_processes = srtf_scheduling(processes)

for process in completed_processes:
    print(f"Process {process.pid}: Waiting Time = {process.waiting_time}, Turnaround Time = {process.turnaround_time}, Completion Time = {process.completion_time}, Response Time = {process.response_time}")

# Print results
print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
print(f"Average Response Time: {average_response_time:.2f}")
print(f"Average Turnaround Time: {average_turnaround_time:.2f}")
