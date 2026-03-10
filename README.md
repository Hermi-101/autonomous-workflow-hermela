# Autonomous Workflow Discovery & Meta-Agent

This project implements an end-to-end autonomous pipeline designed to analyze raw desktop activity data, identify high-value repetitive workflows, and dynamically generate functional automation agents to execute those tasks without human intervention.


##  Overview

The system is divided into two primary components:
1.  **Workflow Discovery Engine (Task 1):** Analyzes SQLite logs and screenshots to identify sequences of user actions. It calculates "persistence" across a 4-day window to identify high-value automation candidates.
2.  **Meta-Agent Builder (Task 2):** A factory-pattern system that reads extracted workflows and autonomously generates standalone Python automation scripts (Agents) using `pyautogui` and `webbrowser`.



##  System Architecture

### 1. Workflow Extraction & Discovery
- **Data Anchoring:** Per the project requirements, all events are joined with the `captures` table to ensure visual evidence for every extracted step.
- **Pattern Matching:** Uses a sliding-window algorithm (n=5) to identify coherent sequences of applications, window titles, and events.
- **Persistence Logic:** Categorizes workflows based on their repetition over time:
    - **Daily Count:** Frequency of occurrence per day.
    - **Multi-Day Persistence:** Identifying patterns that appear across 2, 3, and 4-day horizons.

### 2. The Meta-Agent (Agent Builder)
- **Zero-Code Automation:** Rather than manual scripting, the Meta-Agent parses the JSON "DNA" of a discovered workflow.
- **Dynamic Construction:** The builder injects workflow steps into a pre-defined template to instantiate a functional `.py` agent for each specific task.
- **Execution Capability:** Generated agents are equipped to handle navigation, simulated clicks, and data entry.


##  Project Structure
```text
├── ci/                     # GitHub Actions CI/CD configuration
├── data/                   # Source SQLite database (test_data.db)
├── extractor/              # Task 1: Workflow Discovery logic
│   ├── extract_workflow.py # Main discovery script
│   └── utills.py           # Database and OCR utilities
├── generated_agents/       # Output folder for Meta-Agent generated scripts
├── meta_agent/             # Task 2: The Agent Builder System
│   ├── build_agent.py      # Meta-Agent execution script
│   └── templates.py        # Logic blueprints for generated agents
├── notebooks/              # Exploratory Data Analysis (EDA)
├── system_designs.md       # Detailed architectural design document
├── workflow.json           # Intermediate discovery output (Task 1 -> Task 2)
└── requirements.txt        # Project dependencies
```

##  Installation & Setup Guide

Follow these steps to set up the environment and run the Autonomous Pipeline.

### 1. System Requirements
- **Python 3.10 or higher**
- **Tesseract OCR Engine:** This is required for the system to read text from screenshots.
  - **Windows:** Download and install from [UB Mannheim's Tesseract Page](https://github.com/UB-Mannheim/tesseract/wiki). 
  - *Note: After installation, ensure `tesseract.exe` is in your PATH or update the path in `extractor/utills.py`.*

### 2. Clone the Repository
Open your terminal (Git Bash recommended) and run:
```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd autonomous-workflow-hermela  
```
### 3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
```

### 4.Install dependencies:
```bash
pip install -r requirements.txt
```

## Execution Guide
## 1. Discover Workflows
Run the extraction engine to process the SQLite data and identify repetitive patterns.
```bash
cd extractor
python extract_workflow.py
```
This generates workflow.json in the root directory.

## 2. Generate Meta-Agents
Run the Meta-Agent builder to construct autonomous robots based on the discovered workflows.
```bash
cd ../meta_agent
python build_agent.py
```
Check the /generated_agents/ folder for the resulting automation scripts.


 ## Submission Information
Developer: Hermela Angaw

