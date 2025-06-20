# 🛡️ Phishing URL Keyword Scanner

> 🚨 A beginner-friendly cybersecurity tool that scans URLs for phishing-related keywords using Python!  
> 📌 Helps detect suspicious links based on common phishing tactics.

---

## ✨ Overview

The **Phishing URL Keyword Scanner** is a command-line tool that checks whether a given URL contains suspicious keywords often used in phishing attacks. It’s designed for **cybersecurity learners, ethical hackers, and awareness training projects**.

---

## 🔍 Features

✅ Scan any URL and detect phishing keywords  
⚠️ Alert users when suspicious terms are found  
📂 Save results in `scan_results.txt` with timestamps  
🧠 Load keywords from `suspicious_words.txt` (fully editable)  
🎨 User-friendly colored output via `colorama`  
🪵 Built-in error logging (`phishing_scanner.log`)

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:**  
  - `colorama` – for colorful terminal output  
  - `logging` – for detailed logs  
  - Standard libraries (`os`, `time`, `sys`, `datetime`, etc.)

---

## 📦 Project Structure

phishing_scanner/
├── scanner.py # Main scanning script
├── suspicious_words.txt # List of phishing keywords
├── scan_results.txt # Output results (auto-created)
├── phishing_scanner.log # Logs all scan activities
└── README.md # Project documentation


---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone 
cd phishing_scanner
pip install colorama
