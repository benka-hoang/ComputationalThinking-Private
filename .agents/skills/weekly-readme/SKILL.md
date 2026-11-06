---
name: weekly-readme
description: >-
  Generates a weekly assignment README.md report summarizing student details, 
  exercises completed, and AI usage declarations with detailed prompt logs. 
  Use when the user asks to create, update, or generate a weekly README report.
---

# Weekly Assignment README & AI Usage Generator

This skill guides the agent in creating a structured `README.md` for weekly assignments in courses like CSC10014 (Computational Thinking), featuring a formal AI Usage Declaration.

---

## Workflow Steps

### Step 1: Identify the Target Week
- Check the current workspace structure (e.g., `Week01`, `Week02`, `Week03`).
- Determine which week the user is working on or ask the user if ambiguous.

---

### Step 2: Handle the "In Short" AI Usage Section
Ask the user which mode they prefer for the **Summary (In Short)** section, or present the choices:
- **Choice A: Let the user fill**
  Insert a clear placeholder:
  ```markdown
  ### Summary (In Short)
  [USER TO FILL: Summarize in 1-2 sentences how you utilized AI tools this week]
  ```
- **Choice B: Let the Agent think & fill**
  Analyze the current conversation / task history and write a concise, professional summary covering:
  - Topics consulted (syntax, algorithmic thinking, debugging, problem clarification).
  - Tools utilized (e.g., Antigravity AI Coding Assistant).

---

### Step 3: Compile the Detailed AI Interaction Log
Extract all exercises worked on during the week by reviewing the chat transcript and directory files:
For each exercise (e.g., `Exercise 01`, `Exercise 02`, `Exercise 03`, ...):
1. **Prompts:** Quote or closely summarize the key prompts the user asked.
2. **Assistance Received:** Summarize key concepts taught, syntax explained, runtime errors debugged, or edge cases identified.

---

### Step 4: Generate the `README.md` File
Write the completed template into the target week folder (e.g., `WeekXX/README.md`) using the following structure:

```markdown
# [Week Title] - Weekly Assignment Report

## 1. Student Information
- **Full Name:** [FILL IN YOUR FULL NAME]
- **Student ID:** [FILL IN YOUR STUDENT ID]
- **Course:** CSC10014 - Computational Thinking
- **Semester:** Semester 4

---

## 2. AI Usage Declaration

### Summary (In Short)
<!-- Insert Choice A placeholder or Choice B agent-generated summary here -->

---

### Detailed AI Interaction Log

#### Exercise 01 ([Topic/Problem Title])
- **Prompts:**
  - *"[User Prompt 1]"*
  - *"[User Prompt 2]"*
- **Assistance Received:**
  - [Key concept/fix 1]
  - [Key concept/fix 2]

<!-- Repeat for each exercise -->
```

---

### Step 5: Verification
- Verify the file is created at the correct path (e.g. `<target_week>/README.md`).
- Inform the user and remind them to fill in their Name, Student ID, or any pending placeholders.
