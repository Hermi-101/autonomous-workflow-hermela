# Autonomous Workflow Discovery & Meta-Agent System

## 1. Problem Overview

The objective of this project is to build an autonomous system capable of discovering user workflows from desktop activity logs and automatically generating automation agents that can execute those workflows.

The system analyzes raw user interaction data including application events and screenshots to identify repeated sequences of actions. These sequences are interpreted as workflows which can later be automated.

The project is divided into two major components:

1. Workflow Extraction System
2. Meta-Agent System for Automation Generation

The dataset contains activity logs for three employees over four days. 

 ## 2. Dataset Description

The dataset is stored in a SQLite database and contains two main tables.

### events table

This table records atomic user actions such as:

- Click
- Type
- Scroll
- Copy
- Paste
- Application Switch

Important columns include:

- timestamp
- app_name
- window_title
- event
- url
- clipboard_content
- id_employee

### captures table

This table contains screenshots captured during user activity.

Important columns include:

- event_id
- timestamp
- image_path
- id_employee

### Join Strategy

The workflow extraction process uses the `captures` table as the anchor because only events associated with screenshots provide visual evidence.

The tables are joined using:

captures.event_id = events.id

## 3. System Architecture

The system consists of four main components.
1. **Workflow Extraction Engine**

   Extracts sequences of user actions from raw logs.

2. **Workflow Pattern Analyzer**

   Identifies repeating workflows and calculates repetition statistics.

3. **Meta-Agent Builder**

   Automatically generates automation scripts based on extracted workflows.

4. **Generated Agents**

   Python scripts capable of reproducing the user workflow autonomously.


## 4. Workflow Extraction Methodology

Workflow Schema: Workflows are exported as a JSON array where each object contains metadata (employee_id, persistence scores) and a list of steps. Each step includes app_name, event, url, and a reference to the image_path for visual verification.

The workflow extraction process consists of several steps.

### Step 1: Data Loading

The SQLite database is loaded using Python's sqlite3 module.

### Step 2: Table Join

The captures table is joined with the events table to ensure all analyzed actions have visual context.

### Step 3: Employee Separation

Data is processed independently for each employee to prevent workflow contamination across users.

Employees:

- EMP-0025
- EMP-0028
- EMP-0053

### Step 4: Event Sorting

Events are sorted by timestamp to reconstruct the order of user interactions.

### Step 5: Sequence Detection

User interactions are grouped into workflows based on temporal proximity.

If the time difference between actions is small, they are considered part of the same workflow.

### Step 6: Workflow Representation

Each workflow is represented as an ordered sequence of actions including:

- application name
- event type
- URL
- screenshot reference

This representation allows workflows to later be converted into automation scripts.

## 5. Workflow Pattern Detection

Once workflows are extracted, the system identifies repeated patterns.

Each workflow is converted into a canonical representation based on its sequence of actions.

Patterns are compared across time to determine repetition statistics.

### Metrics Computed

**Daily Count**

Number of times a workflow occurs on each day.

**2-Day Persistence**

Whether the workflow appears on at least two different days.

**3-Day Persistence**

Whether the workflow appears on three different days.

**4-Day Persistence**

Whether the workflow appears across the full four-day period.

These metrics help identify high-value automation opportunities.


## 6. Meta-Agent Architecture

The Meta-Agent system is an "Agent Builder" responsible for generating standalone automation scripts dynamically without manual coding.

### Input
The Meta-Agent parses the `workflow.json` generated in Task 1, specifically prioritizing "High-Value" workflows (those with 2-day or 4-day persistence).

### Implementation Logic: The Factory Pattern
The system employs a code-generation factory:
1. **Parsing:** The builder extracts the sequence of apps, URLs, and events.
2. **Injection:** Data is injected into a specialized Python template (`templates.py`).
3. **Serialization:** The resulting string is saved as a new, executable `.py` script in the `generated_agents/` directory.

### Mapping Strategy

| Workflow Action | Automation Logic | Python Implementation |
|----------------|------------------|----------------------|
| URL/Navigate   | Browser Launch   | `webbrowser.open()`  |
| Click          | Visual Target    | `pyautogui.click()`  |
| Type           | String Injection | `pyautogui.write()`  |
| App Switch     | Focus Change     | `time.sleep()` / OS focus |

The result is a suite of **Autonomous Generated Agents** that can be run independently to reproduce the discovered user behavior.
