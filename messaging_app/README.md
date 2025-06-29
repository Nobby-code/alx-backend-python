Basics of container orchestration with Kubernete
 Novice
 Weight: 1
 Project will start Jun 23, 2025 12:00 AM, must end by Jun 30, 2025 12:00 AM
 Checker was released at Jun 23, 2025 12:00 AM
 Manual QA review was done on Jun 29, 2025 1:24 PM
 An auto review will be launched at the deadline
Overview
Container orchestration refers to the automated management, scaling, and networking of containers. Kubernetes (K8s) is the industry-standard open-source platform for orchestrating containerized applications. It provides developers and DevOps teams with powerful tools to automatically deploy, scale, and manage containers, ensuring high availability and fault tolerance in modern applications.

Kubernetes helps manage clusters of containers running on virtual or physical machines. It abstracts away the infrastructure, allowing teams to focus on application logic rather than server management. By leveraging Kubernetes, development teams can embrace continuous integration/continuous delivery (CI/CD), microservices architecture, and cloud-native principles efficiently.

Objectives
By the end of this, learners should be able to:

Understand the core concepts of Kubernetes and container orchestration.
Deploy and manage containerized applications using Kubernetes.
Explain the relevance of Kubernetes in modern development pipelines.
Recognize key Kubernetes components such as Pods, Nodes, Services, Deployments, and ConfigMaps.
Apply best practices for developing, deploying, and maintaining scalable and reliable systems using Kubernetes.
Learning Outcomes
Learners will:

Grasp the purpose and benefits of container orchestration in software development.
Understand the architecture and ecosystem of Kubernetes.
Learn to write basic Kubernetes configuration files (YAML).
Gain hands-on experience with deploying containers to a Kubernetes cluster.
Explore scaling, self-healing, and rolling update mechanisms in Kubernetes.
Be able to integrate Kubernetes into a CI/CD pipeline for modern DevOps workflows.
Best Practices
Here are key best practices when using Kubernetes in development and production:

Use Declarative Configurations

Define your deployments and services using YAML or Helm charts for version control and reproducibility.
Separate Concerns with Namespaces

Use namespaces to logically divide environments (e.g., dev, staging, production) and manage resources.
Use ConfigMaps and Secrets

Store and manage configuration data and sensitive information securely and independently of your containers.
Health Checks (Liveness & Readiness Probes)

Define clear health checks to allow Kubernetes to detect and replace failing containers automatically.
Resource Requests and Limits

Always define CPU and memory requests and limits to ensure efficient scheduling and prevent resource starvation.
Use Labels and Selectors Strategically

Labels help organize, search, and apply operations across resources.
Monitor and Log Everything

Integrate monitoring tools (Prometheus, Grafana) and logging solutions (ELK, Fluentd) for observability.
Enable Auto-scaling

Use Horizontal Pod Autoscaler (HPA) to adjust to changing loads and optimize resource usage.
Keep Images Lightweight and Secure

Minimize image size, scan for vulnerabilities, and use trusted base images.
Regularly Update and Clean Up

Apply security patches, update dependencies, and clean up unused resources to prevent technical debt.
Relevance in the Development Process
Kubernetes plays a vital role in cloud-native development by supporting microservices, auto-scaling, fault tolerance, and seamless deployments. It empowers teams to:

Deploy applications rapidly and reliably.
Handle dynamic workloads effortlessly.
Implement DevOps and CI/CD practices efficiently.
Reduce downtime and improve system resilience.
Requirements:

Minikube for linux
Tasks
0. Install Kubernetes and Set Up a Local Cluster
mandatory
Objective: Learn how to set up and use Kubernetes locally.

Instructions:

Write a script, kurbeScript that:

Starts a Kubernetes cluster on your machine
verifies that the cluster is running using kubectl cluster-info.
Retrieves the available pods
Ensure minikube is installed

Repo:

GitHub repository: alx-backend-python
Directory: messaging_app
File: messaging_app/kurbeScript
1. Deploy the Django Messaging App on Kubernetes
mandatory
Objective: Deploy your containerized Django app on Kubernetes.

Instructions:

Create a deployment.yaml YAML file for your Django messaging app.

Define the Docker image to be used for the app in the deployment.yaml file.

Expose the Django app via a Service (use a ClusterIP service to keep it internal).

Apply the Deployment using kubectl apply -f deployment.yaml.

Verify that the app is running by checking the pods and logs (kubectl get pods, kubectl logs <pod-name>).

Repo:

GitHub repository: alx-backend-python
Directory: messaging_app
File: messaging_app/deployment.yaml
2. Scale the Django App Using Kubernetes
mandatory
Objective: Learn how to scale applications in Kubernetes.

Instructions:

Write a script kubctl-0x01 if run achieves the following:

Use kubectl scale to increase the number of replicas to 3 of your Django app deployment.
Verify that multiple pods are running by using kubectl get pods.
Perform load testing on your app using wrk to see how the scaled app handles traffic
Monitors Resource Usage using kubectl top
Repo:

GitHub repository: alx-backend-python
Directory: messaging_app
File: messaging_app/kubctl-0x01
3. Set Up Kubernetes Ingress for External Access
mandatory
Objective: Expose your Django app to the internet using an Ingress controller.

Instructions:

Install an Nginx Ingress controller in your cluster .

Create an Ingress resource (ingress.yaml) to route traffic to your Django app’s service.

Configure domain names or paths in the Ingress resource for different services (e.g., /api/ for the Django API).

In commands.txt file write the command you used to apply the Ingress configuration

Repo:

GitHub repository: alx-backend-python
Directory: messaging_app
File: ingress.yaml,commands.txt
4. Implement a Blue-Green Deployment Strategy
mandatory
Objective: Learn how to perform zero-downtime deployments.

Instructions:

Set up a blue-green deployment strategy in Kubernetes where you deploy a new version of the Django app (green_deployment.yaml) alongside the current version: (rename the deployment.yaml file to blue_deployment.yaml). hint

Create Kubernetes Services kubeservice.yaml to switch traffic from the blue version to the green version gradually.

Write a script,kubctl-0x02 with that uses kubectl apply to deploy the blue and green version, and uses kubectl logs to check for errors in the new version

Repo:

GitHub repository: alx-backend-python
Directory: messaging_app
File: green_deployment.yaml,blue_deployment.yaml,kubeservice.yaml,kubctl-0x02
5. Applying rolling updates
mandatory
Objective: Update the application without downtime

Instructions:

Modify the docker image version to 2.0 in the now blue_deployment.yaml

Write a bash script kubctl-0x03 that:

Applies the updated deployment file and triggers a rolling update
Monitors the update progress using kubectl rollout status
Uses curl to test if the app experiences any downtime or disruption by continuously sending requests
Verify the Rolling Update is Complete by checking the current pods
Run your script

Repo:

GitHub repository: alx-backend-python
Directory: messaging_app
File: messaging_app/blue_deployment.yaml, kubctl-0x03
6. Manual Review
mandatory
Score: 100.0% (Checks completed: 100.0%)
Repo:

GitHub repository: alx-backend-python
Directory: messaging_app