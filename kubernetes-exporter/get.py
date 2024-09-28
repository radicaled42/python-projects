import os

# Define the path to the uploaded file
file_path = './kubernetes.logs'

# Open the file and read the contents
with open(file_path, 'r') as file:
    logs = file.readlines()

# Variables to track the current pod and namespace
pod_logs = {}
current_pod = None
current_namespace = None

# Parse the logs
for line in logs:
    if line.startswith("Logs for Pod:"):
        # Extract pod name and namespace
        parts = line.strip().split(" ")
        current_pod = parts[3]  # Extract pod name
        current_namespace = parts[6]  # Extract namespace
        pod_identifier = f"{current_pod}_{current_namespace}"
        # Initialize a new log list for this pod
        if pod_identifier not in pod_logs:
            pod_logs[pod_identifier] = []
    
    # Append the log line to the current pod's log
    if current_pod and current_namespace:
        pod_logs[pod_identifier].append(line)

# Save each pod's logs into separate files
output_dir = './dump-cluster/logs'
os.makedirs(output_dir, exist_ok=True)

for pod, log in pod_logs.items():
    pod_log_file = os.path.join(output_dir, f"{pod}.log")
    with open(pod_log_file, 'w') as pod_file:
        pod_file.writelines(log)

# Return the directory containing the separated logs
output_dir
