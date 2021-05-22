# Filters 



If use minikube rather than AWS (via Kops) or 
another Cloud drive kubernetes, you will likely need to 
change from LoadBalancer to NodePort configuration in the
service descriptions, and you will need to use a different
URL to communicate with Prometheus.

The following will switch LoadBalancer for NodePort
in the service manifest 'type' field:

    grep Load *yml | cut -d: -f1 | xargs sed -i '' -e  s/LoadBalancer/NodePort/

Note that when port "9090" is referenced, or the discovery 
of the service is defined, that this information will
be different.  In the minikube case, the prometheus UI will
be on the minikube IP, which can be discovered as:

    minikube ip

and on the statically defined (nodePort in the .yml definitions)
as 30990.  The following command should generate an HTTP:// URL 
for use in a browser:

    echo "http://$(minikube ip):30990/"


yaml 10-18


# We find an interesting cAdvisor provided metric
container_cpu_user_seconds_total

# We do a little filtering to remove some obvious non-pod data
container_cpu_user_seconds_total{pod_name!=""}

# Then we change the filter to tune in to a single pod
container_cpu_user_seconds_total{pod_name="prometheus-prometheus-1"}

yaml 19-22

# Then we change the filter to tune in to a single pod
container_cpu_user_seconds_total{pod_name="prometheus-prometheus-1"}

# We can then switch from a point data to a data range
container_cpu_user_seconds_total{pod_name="prometheus-prometheus-1"}[5m]

# And now we can start to manipulate the data, first let's look at rate of change
rate(container_cpu_user_seconds_total{pod_name="prometheus-prometheus-1"}[5m])

# And then let's see about the pod metric rather than the individual containers
sum(rate(container_cpu_user_seconds_total{pod_name="prometheus-prometheus-1"}[5m]))


# First we find a time series set that we can work with
# With the example app running, we can look at requests in action
demo_api_http_requests_in_progress

# So how do we get a summary of these vectors?  We could sum them up:
sum(demo_api_http_requests_in_progress)

# But that might be double counting (as this app talks to itself)
# How do we go about filtering on instance data?
sum(demo_api_http_requests_in_progress) without (instance)

sum(demo_api_http_requests_in_progress) without (pod)

# We can also look at unique requests, by removing overlapping requests
demo_api_http_requests_in_progress{instance=~"100.96.3.*:8080"} unless demo_api_http_requests_in_progress{instance=~"100.96.4.*:8080"} unless demo_api_http_requests_in_progress{instance=~"100.96.5.*:8080"}


# We start with a large swath of metrics
http_requests_total

# We might know of a specific type of request, e.g. code 200 requests
http_requests_total{code="200"}

# Then we further refine it by looking at only the top requestors
topk(3,http_requests_total{code="200"})

