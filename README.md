# DevOps / Cloud Engineer Portfolio Project

This project demonstrates a production-style DevOps workflow using **Docker**, **GitHub Actions**, and **Microsoft Azure App Service**.  
The goal is to showcase real-world CI/CD practices, cloud deployment, and infrastructure awareness.

---

## 🚀 Live Application

- **Web App:**  
  https://devops-lab-gha-b6cxc7ccdhgnc5fk.centralus-01.azurewebsites.net

- **Health Check:**  
  `/health`

- **About Endpoint:**  
  `/about`

---

## 🏗 Architecture Overview

**Tech Stack:**
- Python (Flask)
- Docker
- GitHub Actions (CI/CD)
- Azure App Service (Linux, Free Tier)
- Azure Managed Identity

**High-Level Flow:**
1. Developer pushes code to GitHub
2. GitHub Actions pipeline is triggered
3. Application is built and packaged
4. Deployment is automatically pushed to Azure App Service
5. Health endpoint validates successful deployment

---

## 🔄 CI/CD Pipeline

The CI/CD pipeline is implemented using **GitHub Actions**.

### Pipeline Capabilities:
- Triggered on every push to the `main` branch
- Builds the Python application
- Packages the app using Docker
- Deploys automatically to Azure App Service
- Uses Azure authentication for secure deployment

This simulates a real production deployment workflow used by modern DevOps teams.

---

## 🧪 Application Endpoints

| Endpoint | Description |
|--------|------------|
| `/` | Portfolio homepage |
| `/health` | Health check endpoint used for monitoring |
| `/about` | Application metadata and tech stack |

---

## 📦 Containerization

The application is containerized using Docker to ensure:
- Environment consistency
- Cloud portability
- Scalable deployment

The Docker image is built during the CI pipeline and deployed directly to Azure.

---

## 🛠 Skills Demonstrated

- CI/CD pipeline design and troubleshooting
- Docker containerization
- Azure App Service deployment (Linux)
- GitHub Actions workflows
- Production health checks
- Cloud-native application architecture

---

## 👤 Author

**Darrell Goodwin**  
DevOps / Cloud Engineer  

**Tech Focus:**  
Azure · Docker · GitHub Actions · Python · Linux
