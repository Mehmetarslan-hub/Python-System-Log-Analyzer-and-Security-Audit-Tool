# 🛡️ System Log Analyzer and Security Audit Tool

A Python-based CLI tool designed to parse server logs, count system events/errors, and audit potential security risks such as brute-force login attempts.

## 🚀 Features

- **Automated Demo Log Generation:** Automatically creates a sample `server.log` file if no log file exists in the directory.
- **Log Parsing:** Splits log entries into structured components (IP, Timestamp, Log Level, Message).
- **Error Tracking:** Aggregates error types including `ERROR`, `CRITICAL`, `WARNING`, and `FAILED_LOGIN`.
- **Security Audit:** Identifies IP addresses with multiple failed login attempts (Threshold: $\ge 3$).

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts Used:** File I/O, Exception Handling (`try-except`), Dictionaries, Loops & Conditionals.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/Mehmetarslan-hub/Python-System-Log-Analyzer-and-Security-Audit-Tool.git](https://github.com/Mehmetarslan-hub/Python-System-Log-Analyzer-and-Security-Audit-Tool.git)