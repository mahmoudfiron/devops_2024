
# Evaluation Instructions

This document explains how to evaluate the **DevOps-Test-Project**, from setting up the environment to verifying the application's functionality.

---

## 1. Prerequisites

Ensure the following tools are installed:
1. **Docker**: For building and running containerized applications.
2. **Kubernetes**: For deploying the application (e.g., Minikube or a cloud Kubernetes cluster).
3. **kubectl**: To interact with the Kubernetes cluster.

---

## 2. Docker Setup

1. Pull the pre-built Docker image:
   ```bash
   docker pull mousat/my-python-app:latest
   ```

2. Verify the image:
   ```bash
   docker images
   ```

3. Run the container locally (optional):
   ```bash
   docker run -p 8017:8017 -e MY_WEB_APP_STATUS="Running in Docker" mousat/my-python-app:latest
   ```
   - Access the application locally:
     ```plaintext
     http://localhost:8017/status
     ```

---

## 3. Kubernetes Deployment

1. Start a Kubernetes cluster (e.g., using Minikube):
   ```bash
   minikube start
   ```

2. Clone the project repository:
   ```bash
   git clone https://github.com/<your-username>/DevOps-Test-Project.git
   cd DevOps-Test-Project
   ```

3. Apply Kubernetes configurations:
   ```bash
   kubectl apply -f configmap.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

4. Verify the pods are running:
   ```bash
   kubectl get pods
   ```
   - Expected output:
     ```
     NAME                                     READY   STATUS    RESTARTS   AGE
     python-app-deployment-xxxxx             1/1     Running   0          <time>
     ```

5. Verify the service is running:
   ```bash
   kubectl get service python-app-service
   ```
   - Note the `EXTERNAL-IP` or use Minikube's tunnel if it's `<pending>`:
     ```bash
     minikube tunnel
     ```

6. Access the application:
   - Use the external IP or Minikube tunnel:
     ```plaintext
     http://<external-ip-or-localhost>:80/status
     ```

---

## 4. Expected Output

The `/status` endpoint should return:
```json
{
  "status": "Running in Kubernetes",
  "time": "<current-time>"
}
```

---

## 5. Cleanup

To clean up the resources:
1. Delete the deployment and service:
   ```bash
   kubectl delete -f configmap.yaml
   kubectl delete -f deployment.yaml
   kubectl delete -f service.yaml
   ```

2. Stop Minikube:
   ```bash
   minikube stop
   ```

---

### Tips for Evaluators
- Verify the use of ConfigMap for the `MY_WEB_APP_STATUS` variable.
- Confirm the `/status` endpoint works as expected.
- Check that the service is exposed on **port 80** externally.

