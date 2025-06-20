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
git clone https://github.com/SafwanaNasrin/Phishing_scanner_project.git
cd phishing_scanner
pip install colorama

▶️ Run the Tool

python scanner.py

📸 Sample Output

=== Phishing URL Keyword Scanner ===

Enter a URL to scan (or type 'exit' to quit): https://paypal-login-update.com
Scanning URL...
⚠️ Suspicious keyword detected in URL!

✏️ How It Works

    User inputs a URL

    Script checks if it contains any phishing keywords from the list

    Shows scan result and saves it to a file

    Provides helpful colored feedback to the user

    Logs all activity for later review

🧠 Customization

You can edit suspicious_words.txt to add/remove keywords based on new threats or trends.

Example:

login
account
secure
verify
paypal
bank
reset
fraud

🧑‍💻 Author

Safwana Nasrin
B.Sc. Computer Science | Cybersecurity Enthusiast
🔗 LinkedIn (Replace with your actual LinkedIn)
📫 Open to collaboration & internships in Cybersecurity
📜 License

This project is licensed under the MIT License – free to use, modify, and distribute.
🙌 Contributions

Pull requests are welcome!
If you have keyword lists, ideas, or want to add new scanning features, feel free to contribute!
🔖 Tags

#PhishingScanner #Python #CyberSecurityProject #OpenSource #CLIApp #InfoSec

    🔐 Stay alert. Think before you click.


---

✅ Let me know if you want:
- A version of this in PDF for your resume
- Demo video script
- A badge-style GitHub banner

I can also help you **add shields.io badges**, **GitHub Topics**, or a **LinkedIn post** with this project!


