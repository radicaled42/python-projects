# Kubernetes Exporter

The basic idea is to be able to export many types of kubernetes resources at the same time

For example:

`kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{.metadata.namespace}{" "}{.metadata.name}{"\n"}{end}' | xargs -n 2 sh -c 'echo "\nYAML for POD: $2 in Namespace: $1"; kubectl get pod $2 --namespace=$1 -o yaml' sh > kubernetes.logs`

- The script will scan the kubernetes.logs file
- Its going to look for a seprator **Logs for Pod:**
- Its going to create a new log file for each separator it finds

