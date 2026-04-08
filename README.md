---
title: OpenEnv Customer Ops
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# 🚀 OpenEnv Customer Operations Environment

## 📌 Overview

This project implements a **real-world OpenEnv environment** simulating customer support operations.
An AI agent interacts with the environment using the standard:

- `step()`
- `reset()`
- `state()`

The goal is to optimize customer satisfaction, prioritization, and resolution efficiency.

---

## 🎯 Problem Statement

Design a realistic environment where an AI agent handles customer requests, prioritizes tasks, and maximizes operational efficiency using reinforcement learning principles.

---

## 🧠 Environment Design

### 🔹 State Space

The state includes:

- Pending customer requests
- Priority levels
- Time delays
- Resolution status

---

### 🔹 Action Space

The agent can:

- Assign priority
- Resolve tickets
- Escalate issues

---

### 🔹 Reward Function

Reward is based on:

- ✔ Correct prioritization
- ✔ Faster resolution
- ✔ Customer satisfaction

Partial rewards are given for intermediate progress.

---

## 🧪 Tasks Implemented

### 🟢 Easy Task

- Basic ticket resolution
- Fixed priorities

### 🟡 Medium Task

- Multiple tickets with dynamic priorities

### 🔴 Hard Task

- Complex scenario with:
  - Escalations
  - Time constraints
  - Conflicting priorities

---

## 🤖 Agent & Evaluation

- Baseline inference script: `inference.py`
- Produces reproducible results
- Reward range: **0.0 to 1.0 per step**

---

## 🏗️ Project Structure

```
.
├── env.py
├── tasks.py
├── graders.py
├── inference.py
├── openenv.yaml
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 Local Run

```bash
pip install -r requirements.txt
python inference.py
```

---

### 🐳 Docker

```bash
docker build -t customer-ops-env .
docker run -it customer-ops-env
```

---

## 🌐 Hugging Face Deployment

This project is deployed using **Hugging Face Spaces (Docker)** for reproducibility.

---

## 📊 Key Features

- ✔ Fully compliant OpenEnv API
- ✔ Real-world simulation (non-toy problem)
- ✔ Multi-level tasks (easy → hard)
- ✔ Meaningful reward shaping
- ✔ Reproducible evaluation
- ✔ Dockerized environment

---

## 🚀 Future Improvements

- Advanced RL agents
- Real-world datasets integration
- Multi-agent collaboration
- Performance visualization

---

## 👩‍💻 Author

Hema (Computer Science Engineering Student)

---

## 🏆 Goal

To build a scalable, realistic environment for training intelligent agents in customer operations.
