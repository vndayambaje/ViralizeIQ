#!/bin/bash

# Authenticate with AWS
aws configure

# Build Docker image
docker build -t trendiq .

# Push Docker image to AWS ECR
aws ecr create-repository --repository-name trendiq
docker tag trendiq:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/trendiq:latest
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/trendiq:latest

# Deploy on ECS or EC2
aws ecs create-cluster --cluster-name trendiq-cluster
aws ecs create-service --service-name trendiq-service --cluster trendiq-cluster --task <task_arn>
