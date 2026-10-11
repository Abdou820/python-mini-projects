# Python Foundations & Utility Toolkit 

A curated portfolio of core Python scripts and command-line tools built from scratch. This repository documents my first year of programming, focusing on core logic, data structures, file handling, local security principles, and terminal user interfaces (TUI).

---

## Skills & Concepts Learned
Building these projects helped me transition from basic theoretical syntax to solving practical problems. Key technical concepts applied across this repository include:
- **Control Flow & Logic:** Conditional branching (`if-elif-else`), `while` loops, and input validation loops.
- **Data Structures:** Lists manipulation (`append`, `pop`, indexing) and dictionary-based state tracking.
- **File I/O:** Reading, writing, and parsing text files (`open`, `read`, `readlines`, exception handling with `FileNotFoundError`).
- **Security Basics:** Cryptographic pseudo-randomness (`secrets` module), Caesar cipher mathematical implementation, and password complexity scoring heuristics.
- **System Interaction:** Executing shell commands and parsing output streams via the `subprocess` module.
- **User Experience (UX):** Designing clean text-based terminal interfaces with custom ASCII formatting and error feedback.

---

## Project Structure & Details

### 1. Interactive Calculator (`Calculator.py`)
* **Description:** A continuous arithmetic calculator handling standard mathematical operations with robust input handling.
* **Key Implementation Details:** Includes explicit error catching to prevent runtime crashes (such as division by zero checks) and a loop structure allowing multiple calculations in a single session[cite: 20].

### 2. Number Guessing Game (`Number Guessing Game.py`)
* **Description:** A terminal game where the user guesses a randomly generated secret number within a set range[cite: 23].
* **Key Implementation Details:** Utilizes the `random` module alongside attempt-counting logic and dynamic feedback hints ("Too low!" / "Too high!")[cite: 23].

### 3. Countdown Timer (`Countdown Timer.py`)
* **Description:** A time-tracking utility that takes minutes and seconds from the user and counts down second-by-second[cite: 21].
* **Key Implementation Details:** Uses integer division and modulo operations (`//` and `%`) to format total seconds into a readable clock view, paired with the `time.sleep(1)` function[cite: 21].

### 4. To-Do List Manager (`To Do List.py`)
* **Description:** A local task management assistant to organize daily to-dos directly from the command line[cite: 27].
* **Key Implementation Details:** Implements dynamic list manipulation (`append`, index tracking, and `pop` deletion) with safety checks for empty lists and invalid index inputs[cite: 27].

### 5. Secure Password Manager (`Password Manager.py`)
* **Description:** A local credential management tool that stores site names, usernames, and passwords securely in a flat-file structure (`passwords.txt`)[cite: 25].
* **Key Implementation Details:** Utilizes file writing (`'a'` mode) and line-by-line string parsing (`split(' | ')`), combined with `try-except` blocks to handle missing storage files gracefully[cite: 25].

### 6. Secure Password Generator (`Password Generator.py`)
* **Description:** A tool designed to generate strong, randomized cryptographic passwords based on user-defined character pools[cite: 24].
* **Key Implementation Details:** Leverages Python’s secure `secrets` module instead of standard pseudo-random generators, enforcing inclusion rules across uppercase letters, lowercase letters, numbers, and punctuation symbols[cite: 24].

### 7. Password Strength Checker (`Password Strength Checker.py`)
* **Description:** An analysis tool that evaluates a given password against multiple security criteria and outputs a score out of 6[cite: 26].
* **Key Implementation Details:** Employs boolean tracking flags (`has_upper`, `has_lower`, etc.) and character iteration to generate precise, actionable tips for improving password safety[cite: 26].

### 8. WiFi Password Viewer (`WiFi Password Viewer.py`)
* **Description:** A system utility script that retrieves saved wireless network profiles and their plain-text keys on a local machine[cite: 28].
* **Key Implementation Details:** Interacts directly with the operating system via `subprocess.check_output('netsh wlan ...')`, parsing multi-line command output strings to extract network credentials[cite: 28].

### 9. Interactive Learning Bot (`Bot.py`)
* **Description:** A lightweight rule-based terminal chatbot capable of remembering new conversational pairs dynamically[cite: 19].
* **Key Implementation Details:** Combines a dictionary-based memory model with persistent file writing (`bot_memory.txt`), allowing the bot to learn new responses interactively from user inputs[cite: 19].

---

## Purpose
This collection represents my foundational journey into computer science—moving from simple procedural scripts to building functional tools that emphasize logic, security, and clean manual implementation.
