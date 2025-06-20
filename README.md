# DevOps Final Test – Flask App on Kubernetes

## 👨‍💻 Student Name: Mahmoud Firon  
## 📆 Date: June 2024

---

## ✅ Step Summary

| Step | Description |
|------|-------------|
| 1    | Simple Flask app (`app.py`) on port **8017** ✅ |
| 2    | GitHub Actions workflow to build & push Docker image to Docker Hub ✅ |
| 3    | Docker image: `mahmoudfiron/devops-final-app:latest` ✅ |
| 4    | Kubernetes `deployment.yaml` with **2 replicas** ✅ |
| 5    | Service type **LoadBalancer** with target port 8017 ✅ |
| 6    | ConfigMap (`configmap.yaml`) with variable `MY_WEB_APP_STATUS="Running in Kubernetes"` ✅ |
| 7    | Liveness and readiness probes on `/status` ✅ |
| 8    | Manual pod deletion tested: new pod auto recreated ✅ |

---

## 📦 DockerHub Link

🔗 https://hub.docker.com/r/mahmoudfiron/devops-final-app

---

## 📂 Kubernetes Commands Used

```bash
# Apply everything
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# View app
minikube service python-app-service

# Delete one pod to test resilience
kubectl delete pod <pod-name>
