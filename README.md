# AI-Powered Firewall Log Analyzer

A full-stack web application that analyzes firewall traffic logs and generates insights using Python, Flask, pandas, and a locally hosted LLM powered by Ollama.

## Overview

This project allows users to upload firewall traffic logs (CSV format) and receive:

* Key traffic statistics (top IPs, actions, etc.)
* AI-generated security analysis
* Actionable insights into potentially suspicious network behavior

The goal is to combine traditional data processing with AI-driven interpretation to simulate a lightweight security analysis tool.

Unlike cloud-based AI solutions, this project performs inference using a locally hosted LLM, keeping firewall data private while eliminating dependency on external AI services.

---

## Features

### File Upload

* Upload firewall traffic logs through a web interface
* Supports CSV exports from firewall platforms such as Palo Alto Panorama

### Data Analysis (pandas)

* Top actions (allow, deny, etc.)
* Top source IP addresses
* Top destination IP addresses
* Denied traffic count

### Local AI Analysis

* Runs entirely on a locally hosted LLM through Ollama
* No OpenAI API required
* No recurring API costs
* Firewall logs remain on your local network
* Generates insights such as:

  * Overall traffic summary
  * Potentially suspicious activity
  * Investigation recommendations

### Frontend (Flask + Bootstrap)

* Responsive UI using Bootstrap
* Dashboard-style layout
* Structured display of metrics and AI output

---

## Tech Stack

* Backend: Python, Flask
* Data Processing: pandas
* Frontend: HTML, Bootstrap
* AI Integration: Ollama + Qwen 3 (or any compatible local model)
* Environment Management: python-dotenv
* Version Control: Git, GitHub

---

## Setup Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/traffic-log-analyzer.git
cd traffic-log-analyzer
```

### 2. Create a virtual environment

``` bash
python3 -m venv .venv
```

Activate it:

**macOS/Linux**

``` bash
source .venv/bin/activate
```

**Windows**

``` powershell
.venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

Then pull a supported model:

``` bash
ollama pull qwen3:8b
```

Ensure the Ollama server is running before launching the application.

### 5. Configure environment variables

Create a `.env` file in the project root:

``` env
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=qwen3:8b
```

If the AI server is running on another machine, replace `localhost` with
that machine's local IP.

Example:

``` env
OLLAMA_URL=http://192.168.1.xxx:11434/api/generate
OLLAMA_MODEL=qwen3:8b
```

### 6. Run the application

``` bash
python app.py
```

Open your browser:

``` text
http://127.0.0.1:5000
```

---

## Project Structure

``` text
traffic-log-analyzer/
│
├── app.py
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── css/
├── uploads/
├── .env.example
├── requirements.txt
└── README.md
```

---

## Example Workflow

1.  Upload a firewall traffic log (CSV).
2.  The application processes the data using pandas.
3.  Key traffic statistics are extracted.
4.  A structured prompt is generated and sent to the local LLM through
    Ollama.
5.  The AI returns a concise security analysis highlighting suspicious
    activity and recommended investigation points.

---

## Why Local AI?

-   Firewall logs never leave your environment
-   No dependence on cloud AI availability
-   No API usage costs
-   Faster inference on GPU-equipped systems
-   Ability to switch models without modifying application logic

---

## Future Improvements

-   User authentication
-   Scan history per user
-   Export reports (PDF)
-   Interactive AI chat about uploaded logs
-   Threat severity scoring
-   Traffic visualizations
-   Support for additional firewall vendors

---

## Why This Project Matters

This project demonstrates:

-   Full-stack web development with Flask
-   Cybersecurity log analysis
-   Data processing with pandas
-   Local LLM integration through Ollama
-   REST API communication
-   Environment configuration and dependency management
-   Practical application of AI to network security workflows

---

## License

This project is for educational and personal portfolio use.
