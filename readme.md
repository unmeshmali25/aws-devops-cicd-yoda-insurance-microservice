# Yoda Insurance Policy Service

A Spring Boot microservice for managing insurance policies at Yoda Insurance.

## Overview

This microservice is part of the Yoda Insurance platform, handling policy-related operations. It's built with Spring Boot and deployed on AWS EKS using a CI/CD pipeline with AWS CodeBuild.

## Technologies

- Java 17
- Spring Boot 3.4.0
- Spring Data JPA
- Docker
- Kubernetes (AWS EKS)
- AWS CodeBuild
- AWS ECR

## Prerequisites

- Java 17 or higher
- Maven
- Docker
- AWS CLI
- kubectl

## Local Development

1. Clone the repository:
`git clone <repository-url>`
`cd yoda-insurance-ms`

2. Build the project
`./mvnw clean package`

3. Run locally: 
`./mvnw spring-boot:run`
The application will start on `http://localhost:8080`


## Docker Build

Build the Docker image locally:
`docker build -t yoda-insurance-policy-service .`
`docker run -p 8080:8080 yoda-insurance-policy-service`


## Deployment

The service is automatically deployed to AWS EKS through AWS CodeBuild pipeline. The pipeline:

1. Builds the Java application
2. Creates a Docker image
3. Pushes to Amazon ECR
4. Deploys to EKS cluster

### Kubernetes Resources

The service uses the following Kubernetes configurations:

- Deployment: 2 replicas with resource limits
- Service: LoadBalancer type exposing port 80
- ConfigMap: AWS authentication for EKS

## API Endpoints

- `GET /hello` - Test endpoint returning a greeting message

## Configuration

The application can be configured through:

- `application.properties` - Application configuration
- Environment variables:
  - `AWS_DEFAULT_REGION`
  - `AWS_ACCOUNT_ID`
  - `IMAGE_REPO_NAME`
  - `IMAGE_TAG`
  - `EKS_CLUSTER_NAME`

## Project Structure
yoda-insurance-ms/
├── src/
│ ├── main/
│ │ ├── java/
│ │ └── resources/
│ └── test/
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── aws-auth-configmap.yaml
├── Dockerfile
├── buildspec.yml
└── pom.xml


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
