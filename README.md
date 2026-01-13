# ci-cd-capstone-project

This project demonstrates a production-style CI/CD pipeline built around a 2-tier web application using Docker, Docker Compose, GitHub Actions and PostgreSQL. The pipeline automates build → test → scan → push → deploy to a staging environment with security and best practices.

## Project Structure

```
ci-cd-docker-project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_health.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── nginx.conf
│   └── Dockerfile
│
├── docker-compose.yml
├── docker-compose.staging.yml
├── .env
├── .env.staging
│
├── scripts/
│   ├── deploy-staging.sh
│   └── verify.sh
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
└── README.md

```

## GitHub Actions Architecture

<img width="1055" height="595" alt="Screenshot 2026-01-12 172709" src="https://github.com/user-attachments/assets/40214411-9dc6-4a3b-81cd-81776647197d" />

## GitHub Actions Workflow

<img width="1157" height="474" alt="Screenshot 2026-01-12 203415" src="https://github.com/user-attachments/assets/bdf381a4-fe43-40f5-b234-c8b702e9bba4" />

## Technology Stack

| Category              | Tools                                 |
| --------------------- | ------------------------------------- |
| Frontend              | Nginx + static HTML/CSS/JS (or React) |
| Backend               | Flask (Python) / Express.js (Node.js) |
| Database              | PostgreSQL                            |
| Container Runtime     | Docker                                |
| Orchestration (Local) | Docker Compose                        |
| CI/CD                 | GitHub Actions / Jenkins              |
| Security Scanning     | Trivy                                 |
| Registry              | Docker Hub (or ECR/GCR)               |
| Target Environment    | Staging                               |
| Deployment            | Shell scripts                         |

## Environment Configuration

Environment variables stored via `.env.staging` such as:

```
DB_HOST=db
DB_USER=staging_user
DB_PASSWORD=staging_pass
DB_NAME=staging_db
FLASK_ENV=staging
```

## CI/CD Pipeline Stages

1. Checkout source code
2. Build Docker images
3. Run unit tests (inside containers)
4. Scan images using Trivy
5. Tag & push images to registry
6. Deploy to staging environment
7. Health checks & verification

### Outputs

**Frontend check:** http://localhost:8080
<img width="1074" height="689" alt="Screenshot 2026-01-12 133745" src="https://github.com/user-attachments/assets/4cded7e9-459f-4cc6-b7fc-0e26986cd78d" />

**Backened health check:** http://localhost:5000/health
<img width="816" height="337" alt="Screenshot 2026-01-12 133457" src="https://github.com/user-attachments/assets/f0ead034-34c9-47cd-a0ca-6fa6c73a0b38" />

<img width="922" height="313" alt="Screenshot 2026-01-12 134248" src="https://github.com/user-attachments/assets/765fb41a-b9b1-46b4-9f47-752f900e8fbb" />

<img width="948" height="403" alt="Screenshot 2026-01-12 140952" src="https://github.com/user-attachments/assets/31e2e2d3-f104-4328-8836-61321827af3f" />

<img width="1867" height="921" alt="Screenshot 2026-01-12 205245" src="https://github.com/user-attachments/assets/189d1739-2718-4120-9b0e-cde598e3f2be" />



