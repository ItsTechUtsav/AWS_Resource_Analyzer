# 💰 AWS Cost Optimization Tool

A Python-based AWS cost optimization tool that scans AWS resources, identifies commonly unused resources, generates an HTML report, and automatically emails the report using GitHub Actions.

---

# 📌 Problem Statement

During development and testing, AWS resources are often created temporarily and then forgotten. These unused resources continue to generate charges even though they are no longer serving any purpose.

Some common examples include:

- Unattached EBS Volumes
- Unused Elastic IP Addresses
- Old EBS Snapshots
- Running EC2 instances that developers forget to review

Manually checking every AWS service regularly is repetitive and time-consuming, especially as cloud infrastructure grows.

---

# ✅ Solution

This project automates the process of identifying commonly unused AWS resources using **Python** and **Boto3**.

The tool scans multiple AWS services, prepares a consolidated HTML report, and sends it automatically via email using GitHub Actions.

This helps reduce manual effort and provides quick visibility into potential cloud cost savings.

---

# 🚀 Features

- Scan EC2 Instances
- Detect Unattached EBS Volumes
- Detect Unused Elastic IP Addresses
- Detect Old EBS Snapshots
- Calculate Estimated Monthly Savings
- Generate HTML Report
- Send Report via Email
- Automated execution using GitHub Actions
- Secure credentials using GitHub Secrets

---

# 🏗️ Project Architecture

```
                  AWS Account

      EC2    EBS    Elastic IP    Snapshots
         │      │         │            │
         └────────────┬───────────────┘
                      │
                Python + Boto3
                      │
             Resource Analysis
                      │
             HTML Report Generator
                      │
         ┌────────────┴────────────┐
         │                         │
    Email Report            GitHub Artifact
```

---

# ⚙️ Project Workflow

```
GitHub Actions

        │

        ▼

Run Python Script

        │

        ▼

Scan AWS Resources

        │

        ▼

Generate HTML Report

        │

        ▼

Send Email

        │

        ▼

Upload Report as GitHub Artifact
```

---

# 🛠️ Tech Stack

- Python
- AWS
- Boto3
- AWS CLI
- IAM
- GitHub Actions
- HTML
- SMTP (Gmail)
- GitHub Secrets

---

# 📂 Project Structure

```
aws-cost-optimizer/
│
├── detectors/
│   ├── ec2.py
│   ├── ebs.py
│   ├── eip.py
│   └── snapshots.py
│
├── reports/
│   ├── html_report.py
│   └── report.html
│
├── mail/
│   ├── email_sender.py
│   └── __init__.py
│
├── .github/
│   └── workflows/
│       └── daily-report.yml
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Resources Checked

| AWS Resource | Purpose |
|-------------|---------|
| EC2 | Display running instances |
| EBS Volume | Detect unattached volumes |
| Elastic IP | Detect unused public IPs |
| EBS Snapshot | Detect snapshots older than 90 days |

---


# 📧 Email Automation

After generating the HTML report, the tool automatically sends the report as an email attachment.

The email contains:

- Summary of the scan
- HTML report attachment
- Estimated monthly savings

---

# 🤖 GitHub Actions

The project can be executed manually or on a scheduled basis using GitHub Actions.

Workflow includes:

- Checkout Repository
- Setup Python
- Install Dependencies
- Configure AWS Credentials
- Run Python Script
- Generate HTML Report
- Send Email
- Upload HTML Report as Artifact

---

# 🔐 Security

Sensitive information is **not stored in the source code**.

The project uses:

- GitHub Secrets
- Environment Variables

for:

- AWS Access Key
- AWS Secret Key
- Email
- App Password

---

# 📸 Screenshots


---

# 🔮 Future Enhancements

- CloudWatch CPU Utilization based Idle EC2 Detection
- AWS Cost Explorer Integration
- Underutilized RDS Detection
- Idle Load Balancer Detection
- Slack Notifications
- Docker Support
- AWS Lambda Deployment
- Multi-Account Scanning

---

# 🙋 Why I Built This Project

I wanted to build something beyond basic CRUD applications and work on a project that solves a practical cloud engineering problem.

This project helped me understand how to interact with AWS services using Boto3, automate repetitive cloud tasks, and build a simple reporting pipeline using GitHub Actions and email automation.
