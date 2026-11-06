# Week 02 - Weekly Assignment Report

## 1. Student Information
- **Full Name:**  Hoang Thien Nhan
- **Student ID:** 25125031
- **Course:** CSC10014 - Computational Thinking
- **Semester:** Semester 4

---

## 2. AI Usage Declaration

### Summary (In Short)
- **Consultation Topics:** Python syntax fundamentals, debugging runtime errors and edge cases, problem statement clarification, and algorithmic implementation assistance.
- **Tools Used:** Antigravity AI Coding Assistant (Gemini).

---

### Detailed AI Interaction Log

#### Exercise 01 (Python Basics & Divisibility)
- **Prompts:**
  - *"give me a first hello world code in python"*
  - *"code for me inside E01.py, input 3 integer n, m, a"*
  - *"let x = (if a divides n then x = n / a, if not x = n // a + 1), y be the coresspond but with m"*
- **Assistance Received:**
  - Learned Python syntax for multi-variable integer input using `map(int, input().split())`.
  - Implemented conditional branch logic and ceiling division.

---

#### Exercise 02 (Codeforces 2A - Winner)
- **Prompts:**
  - *"Im wanting to have an map that contain integer and the key is string (map[\"abc\"] = 2 for example), help me to implement it down"*
  - *"what is the for syntax in python?"*
  - *"hey fix for me in the line 28"* (Fixing `map(string, int, input().split())` and `n = map(int, input())`)
  - *"how can I get the data (for example course[0].first?)"*
  - *"why when I run, I fail at line 41, the error is TypeError: 'set' object is not subscriptable"*
  - *"Yes I really do Codeforces 2A, why it wrong?"*
- **Assistance Received:**
  - Understood Python dictionaries (`dict`) and variable naming best practices.
  - Learned tuple vs. set syntax: `{s, num}` produces an unsubscriptable set, while `(s, num)` creates a subscriptable pair/tuple.
  - Debugged algorithmic edge cases: accumulating round scores instead of overwriting, tracking running totals per round, and handling potentially negative final scores.

---

#### Exercise 03 (Codeforces 3A - Shortest path of the king)
- **Prompts:**
  - *"This time I will will u the idea and will need u to implemtn for mee: Read & Extract position into (x, y)... min(deltax, deltay) will be the cross... deltax & deltay negative or postive will determine the L/R and U/D"*
- **Assistance Received:**
  - Translated student's mathematical logic (Chebyshev distance / coordinate delta) into clean Python code matching Codeforces directional string requirements.

---

#### Exercise 05 (Codeforces 5A - Chat Server's Outgoing Traffic)
- **Prompts:**
  - *"Im now struggling with maintaining the input(), especially continue to input() when the user still input"*
  - *"what is the syntax for if.. else if in python?"*
  - *"Is it safe to code like I have?"*
  - *"Can I use the try, expect method? I have tried it before but when I ran it (on my terminal), it cause bug when trying to access command[0]"*
  - *"Is if 'not command' true? Since if it is a blank line, it also include the '\n', which mean, the length will be 1"*
- **Assistance Received:**
  - Handled continuous input until EOF using both `try ... except EOFError:` and `sys.stdin`.
  - Explained that `input()` automatically strips trailing newline characters (`\n`), unlike `sys.stdin.readline()`.
  - Added empty string boundary guards to avoid `IndexError: string index out of range` on `command[0]`.
  - Avoided improper use of `.strip()` which could alter valid whitespace inside chat messages.

---

#### Exercise 06 (Codeforces 6B - President's Office)
- **Prompts:**
  - *"what is the syntax of a function in python?"*
- **Assistance Received:**
  - Learned `def` syntax and chained range checking (`0 <= x < n and 0 <= y < m`).

---

#### Exercise 07 (Codeforces 7B - Memory Manager)
- **Prompts:**
  - *"What is identifier? It doesn't have any relationship with the memory block's position? Only count from 1 -> 2 -> 3 ->...?"*
  - *"why I can't access globalIndex inside def alloc()?"*
  - *"help me to complete the code"*
- **Assistance Received:**
  - Clarified the problem specification: identifiers are sequential auto-incrementing IDs independent of memory cell indices.
  - Resolved `UnboundLocalError` by declaring `global globalIndex` and `global mem`.
  - Differentiated between operation count $t$ and memory capacity $m$.
  - Implemented exact contiguous allocation, safe erasure checks, and an $O(m)$ defragmentation compaction.

---

#### Exercise 11 (Contribution Report)
- **Prompts:**
  - *"I would need u to create for me a .md file will content: I haven't contribute anything yet, since this is the first week of the project"*
- **Assistance Received:**
  - Created `E11.md` documenting initial project status.
