# Scalable Web Application Using NLB and Auto Scaling

## Project Overview

This project demonstrates the deployment of a scalable web application on Amazon Web Services (AWS) using Amazon EC2, Auto Scaling, Target Groups, and a Network Load Balancer (NLB).

A Flask-based web application was deployed on Ubuntu EC2 instances. An Auto Scaling Group was configured to maintain multiple EC2 instances across different Availability Zones. A Network Load Balancer was configured to distribute TCP traffic to the application instances.

---

## Objective

The main objective of this project is to demonstrate how a web application can be made scalable and highly available using AWS Auto Scaling and Network Load Balancing.

The project focuses on:

- Deploying a Flask application on EC2.
- Creating a reusable EC2 Launch Template.
- Creating an Auto Scaling Group.
- Running multiple EC2 instances.
- Creating a Target Group.
- Configuring a Network Load Balancer.
- Performing health checks.
- Understanding scalable and highly available cloud architecture.

---

## AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon EC2 | Hosts the Flask web application |
| Auto Scaling Group | Maintains and manages multiple EC2 instances |
| Launch Template | Stores the configuration used to launch EC2 instances |
| Target Group | Registers EC2 instances as load balancing targets |
| Network Load Balancer | Designed to distribute TCP traffic |
| Security Groups | Controls network traffic to EC2 instances |
| Amazon VPC | Provides the networking environment |

---

## Architecture

```text
                    Internet
                       |
                       |
             Network Load Balancer
                    TCP : 80
                       |
                       v
                Target Group
                       |
              +--------+--------+
              |                 |
              v                 v
        EC2 Instance 1    EC2 Instance 2
        ap-south-1a       ap-south-1b
              |                 |
              +--------+--------+
                       |
                 Flask Application
                       |
                    Auto Scaling