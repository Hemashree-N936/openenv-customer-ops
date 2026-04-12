# OpenEnv-TaskSuite

## Overview

OpenEnv-TaskSuite is a multi-task environment built using the OpenEnv specification.  
It simulates real-world tasks that AI agents commonly perform, including:

- Email Triage
- Data Cleaning
- Meeting Scheduling

The environment is designed for evaluating agent capabilities using a standardized interface (`step`, `reset`, `state`) with deterministic grading and reward functions.

---

## Motivation

Modern AI agents must operate in real-world environments rather than synthetic benchmarks.  
This project provides a lightweight, reproducible environment to evaluate agent decision-making across multiple practical tasks.

---

## Tasks

### 1. Email Triage (Easy)

- Objective: Classify emails correctly
- Action: `classify`
- Grader: Ratio of correct classifications

---

### 2. Data Cleaning (Medium)

- Objective: Clean dataset entries
- Action: `clean`
- Grader: Ratio of correct cleaning actions

---

### 3. Meeting Scheduling (Hard)

- Objective: Schedule meetings without conflicts
- Action: `schedule`
- Grader: Ratio of valid scheduling actions

---

## Action Space

```json
{
  "action_type": "string",
  "params": {}
}
```
