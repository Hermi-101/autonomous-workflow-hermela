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

captures.event_id = events.

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

The Meta-Agent system is responsible for generating automation agents automatically.

### Input

The Meta-Agent receives the extracted workflows from Task 1.

### Agent Generation Process

For each workflow:

1. The workflow structure is read.
2. Each action is mapped to an automation instruction.
3. A Python script is generated using PyAutoGUI.


Example mapping:

| Workflow Action | Automation Command |
|----------------|-------------------|
| Click | pyautogui.click() |
| Type | pyautogui.write() |
| Copy | pyautogui.hotkey('ctrl','c') |
| Paste | pyautogui.hotkey('ctrl','v') |

The result is a standalone Python automation agent.
