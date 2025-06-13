## PLUS W - IT Training
*Date: April 19, 2025*

## Class 13: Launching Linux Servers on AWS

### Acknowledgement
- Supported by **AOTS** and **OEC**
- **Ministry of Economy, Trade and Industry**
- **Overseas Employment Corporation**

## 1. Recap of Last Week
- Control and loop statements
- Linear algebra in NumPy
- Data inspection and requirement analysis
- Machine learning algorithms
- SDLC, Gitflow, Waterfall, Agile methodologies
- Security compliance

## 2. Today’s Focus
- Introduction to AWS and EC2
- Comparison of Linux distributions (Ubuntu, CentOS, Amazon Linux)
- Creating an AWS account and understanding Free Tier
- Launching an EC2 instance
- Managing SSH key pairs for secure access
- Quiz and Q&A session

## 3. AWS & EC2 Overview
- **AWS**: Cloud platform with IaaS, PaaS, SaaS solutions
- **EC2**: Scalable virtual servers for apps
- **Core Services**: EC2, S3, RDS, IAM, Lambda
- **Example**: A startup uses EC2 for app hosting, S3 for storage, RDS for databases

## 4. AWS Global Infrastructure
- **Regions**: Geographical areas (e.g., US-East, Asia-Pacific)
- **Availability Zones**: Isolated data centers in a region
- **Edge Locations**: Content delivery for CloudFront
- **Benefits**: High availability, low latency, disaster recovery
- **Example**: Website hosted in Singapore with two AZs for reliability

## 5. Linux Distributions on AWS
- **Ubuntu**: Developer-friendly, APT package manager
- **Amazon Linux**: AWS-optimized, fast, DNF-based
- **CentOS/Rocky Linux**: Enterprise-grade, stable, YUM/DNF
- **Example**: Ubuntu for quick dev, Amazon Linux for AWS-native apps

## 6. EC2 Pricing Models
- **On-Demand**: Pay-as-you-go, flexible
- **Reserved**: Up to 75% savings for long-term use
- **Spot**: Up to 90% cheaper for flexible workloads
- **Example**: On-Demand for testing, Reserved for production

## 7. Launching an EC2 Instance
- Select AMI (e.g., Ubuntu 22.04, Amazon Linux 2023)
- Choose instance type (e.g., t3.micro - Free Tier)
- Configure storage (e.g., 8GB EBS), tags, security group (SSH port 22)
- Create/download SSH key pair
- Launch and connect via `ssh -i key.pem ubuntu@<public-ip>`

## 8. SSH Key Pairs
- **Purpose**: Secure passwordless EC2 access
- **Creation**: Generate in EC2 Dashboard, download `.pem` file
- **Security**: Run `chmod 400 key.pem` to restrict access
- **Example**: Connect with `ssh -i key.pem ec2-user@<public-ip>`

## 9. AWS Free Tier
- **Benefits**: 750 hrs/month of t3.micro EC2, 5GB S3 storage
- **Best Practices**: Set billing alerts, stop instances, use Cost Explorer
- **Example**: Host a small WordPress site on Free Tier EC2

## 10. Git on EC2
- Install Git: `sudo apt install git` (Ubuntu) or `sudo dnf install git` (Amazon Linux)
- Clone repos: `git clone https://github.com/your-repo.git`
- **Example**: Deploy a Node.js app by cloning its repo on EC2

