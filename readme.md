Azure High-Availability Cloud Architecture (CCP Project)
📌 Project Overview
This project demonstrates a robust, cloud-native Hybrid Multi-Tier Application deployed on Microsoft Azure. It is designed to meet strict non-functional requirements for High Availability (99.95% SLA), Scalability, and Fault Tolerance by integrating IaaS, PaaS, and SaaS models.

🏗 Architecture
Frontend (PaaS): Azure App Service (Premium V3) running a Dockerized Flask application. configured with Zone Redundancy and Auto-Scaling.

Backend (IaaS): Azure Virtual Machine (Ubuntu Linux) acting as the persistence layer, utilizing Zone-Redundant Storage (ZRS) for data durability.

Security (SaaS): Identity management implemented via Microsoft Entra ID to enforce secure access control.

🛠 Tech Stack
Cloud Provider: Microsoft Azure

Containerization: Docker & Azure Container Registry (ACR)

Web Framework: Python Flask

Server: Gunicorn / Nginx

Testing: Apache Benchmark (ab) for load testing

🚀 Deployment Steps
1. Backend Setup (IaaS)
Provision the Azure VM and configure Zone-Redundant Storage.

Bash

# SSH into VM
ssh azureuser@<VM-PUBLIC-IP>
# Install dependencies
sudo apt-get update && sudo apt-get install python3-pip
2. Frontend Deployment (PaaS)
Build the Docker image and push to Azure Container Registry.


# Build & Push
docker build -t ccp-app .
docker tag ccp-app <your-registry>.azurecr.io/ccp-app:v1
docker push <your-registry>.azurecr.io/ccp-app:v1
Deploy to Azure App Service and enable "Zone Redundancy" in the Plan settings.

⚡ Load Testing
To validate scalability, we use Apache Benchmark to simulate 50 concurrent users.


# Run 10,000 requests with 50 concurrent users
ab -n 10000 -c 50 https://<YOUR-APP-NAME>.azurewebsites.net/products
📈 Key Results
Throughput: ~150 Requests/Sec

Scaling: Automatically scales from 1 → 2 instances when CPU > 70%.

Availability: Resilient against single-zone datacenter failures
