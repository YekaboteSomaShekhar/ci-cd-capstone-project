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
