from collections import deque

# Define a class to represent a process
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0
        self.response_time = -1  # Initially set to -1 to indicate it hasn't been set yet

# Function to implement Round Robin scheduling
def round_robin_scheduling(processes, time_quantum):
    time = 0
    queue = deque()
    n = len(processes)
    completed = 0

    # Sort processes by arrival time initially
    processes.sort(key=lambda p: p.arrival_time)

    # Add the first process to the queue
    queue.append(processes[0])
    idx = 1

    while completed != n:
        if not queue:
            time = processes[idx].arrival_time
            queue.append(processes[idx])
            idx += 1
        
        current_process = queue.popleft()

        # Set the response time if the process is getting the CPU for the first time
        if current_process.response_time == -1:
            current_process.response_time = time - current_process.arrival_time

        # Calculate time slice for the current process
        if current_process.remaining_time > time_quantum:
            time += time_quantum
            current_process.remaining_time -= time_quantum
        else:
            time += current_process.remaining_time
            current_process.remaining_time = 0
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1

        # Add new processes to the queue
        while idx < n and processes[idx].arrival_time <= time:
            queue.append(processes[idx])
            idx += 1

        # Re-add the current process to the queue if it's not finished
        if current_process.remaining_time > 0:
            queue.append(current_process)

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
    Process(1, 0, 9),
    Process(2, 1, 4),
    Process(3, 2, 9)
]

time_quantum = 3

average_waiting_time, average_turnaround_time, average_response_time, completed_processes = round_robin_scheduling(processes, time_quantum)

for process in completed_processes:
    print(f"Process {process.pid}: Waiting Time = {process.waiting_time} ms, Turnaround Time = {process.turnaround_time} ms, Completion Time = {process.completion_time} ms, Response Time = {process.response_time} ms")

# Print results
print(f"\nAverage Waiting Time: {average_waiting_time:.2f} ms")
print(f"Average Turnaround Time: {average_turnaround_time:.2f} ms")
print(f"Average Response Time: {average_response_time:.2f} ms")
