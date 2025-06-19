# DevOps-Test-Project

[Evaluation Instructions](EVALUATION.md)

This project demonstrates deploying a Python web application using Docker and Kubernetes, fulfilling the requirements for a DevOps test.

---

## Question 2 Answer

הייתי שומר את זה ב **Docker Hub** כי:

- זה מאפשר לשתף את התמונה בקלות עם אחרים.

**הפקודה לשמירה**:

```bash
docker push your-username/your-image-name
```

---

## Question 4 Answer

כדי לפרוס את האפליקציה ב-EKS הייתי יוצר Deployment עם לפחות שני מופעים באמצעות Kubernetes, וזה ידאג שיהיו תמיד שני מופעים של האפליקציה.  
האפליקציה תאזין לפורט 80 דרך Service מסוג LoadBalancer שימפה את הפורט החיצוני לפורט הפנימי של הקונטיינר.  
את משתנה הסביבה הייתי שומר בתוך Secret של Kubernetes, כדי שהוא יהיה סודי ולא יופיע בקוד.

---

## Overview

The application exposes a `/status` endpoint that:

- Returns a `status` value from an environment variable.
- Includes the current server timestamp.

The application is containerized using Docker and deployed on Kubernetes.

---

## Setup Instructions

### Docker Setup

1. **Build the Docker Image**:

   ```bash
   docker build -t mousat/my-python-app:latest .
   ```

2. **Push the Docker Image**:
   ```bash
   docker push mousat/my-python-app:latest
   ```

### Kubernetes Deployment

1. **Create the ConfigMap**:

   ```bash
   kubectl apply -f configmap.yaml
   ```

2. **Deploy the Application**:

   ```bash
   kubectl apply -f deployment.yaml
   ```

3. **Expose the Service**:

   ```bash
   kubectl apply -f service.yaml
   ```

4. **Access the Application**:
   - Use Minikube to expose the service:
     ```bash
     minikube service python-app-service
     ```
   - Or directly access the `/status` endpoint via the external IP:
     ```plaintext
     http://10.100.206.55:80/status
     ```

---

## Question 2 Answer

הייתי שומר את זה ב **Docker Hub** כי:

- זה מאפשר לשתף את התמונה בקלות עם אחרים.

**הפקודה לשמירה**:

```bash
docker push your-username/your-image-name
```

---

## Files Included

1. **app.py**: Python application exposing the `/status` endpoint.
2. **Dockerfile**: For building the container image.
3. **configmap.yaml**: Stores environment variable `MY_WEB_APP_STATUS`.
4. **deployment.yaml**: Kubernetes Deployment with two replicas.
5. **service.yaml**: Kubernetes Service exposing the app on port 80.

---
