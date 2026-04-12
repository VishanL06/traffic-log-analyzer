# AI-Powered Firewall Log Analyzer

A full-stack web application that analyzes firewall traffic logs and generates insights using Python, Flask, pandas, and OpenAI.

## Overview

This project allows users to upload firewall traffic logs (CSV format) and receive:

* Key traffic statistics (top IPs, actions, etc.)
* Security-relevant metrics (e.g., denied traffic)
* AI-generated analysis highlighting suspicious activity and patterns

The goal is to combine traditional data processing with AI-driven interpretation to simulate a lightweight security analysis tool.

---

## Features

### File Upload

* Upload CSV traffic logs through a web interface
* Handles real-world firewall log formats (e.g., Palo Alto)

### Data Analysis (pandas)

* Top actions (allow, deny, etc.)
* Top source IP addresses
* Top destination IP addresses
* Denied traffic count

### AI Analysis

* Uses OpenAI API to analyze structured traffic summaries
* Generates insights such as:

  * suspicious activity
  * unusual traffic patterns
  * potential investigation points

### Frontend (Flask + Bootstrap)

* Responsive UI using Bootstrap
* Dashboard-style layout
* Structured display of metrics and AI output

---

## Tech Stack

* Backend: Python, Flask
* Data Processing: pandas
* Frontend: HTML, Bootstrap
* AI Integration: OpenAI API
* Version Control: Git, GitHub

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/traffic-log-analyzer.git
cd traffic-log-analyzer
```

---

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set your OpenAI API key

```bash
export OPENAI_API_KEY="your_api_key_here"
```

(Optional: add this to ~/.zshrc for persistence)

---

### 5. Run the app

```bash
python3 app.py
```

Then open:

http://127.0.0.1:5000

---

## Project Structure

```
traffic-log-analyzer/
│
├── app.py
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── css/
├── uploads/
├── requirements.txt
└── README.md
```

---

## Example Use Case

1. Upload a firewall traffic CSV
2. View:

   * top source IPs
   * most common actions
   * denied traffic count
3. Receive an AI-generated summary such as:
   "High concentration of denied traffic from a single IP may indicate scanning or brute-force behavior."

---

## Notes

* Column names are normalized to lowercase to handle inconsistent CSV formatting
* AI analysis is based on summarized data rather than full logs for efficiency
* Ensure your CSV contains relevant fields such as:

  * action
  * source address
  * destination address

---

## Future Improvements

* User-driven queries (ask questions about logs)
* Anomaly detection (e.g., spikes in traffic)
* Visualization (charts for traffic patterns)
* Improved classification of denied traffic types
* File history and session tracking

---

## Why This Project Matters

This project demonstrates:

* real-world data handling
* full-stack development (Flask + frontend)
* integration of AI into a practical workflow
* ability to extract and interpret meaningful insights from raw logs

---

## License

This project is for educational and personal portfolio use.
