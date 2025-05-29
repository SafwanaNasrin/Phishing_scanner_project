from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)
LOG_FILE = 'scan_results.txt'
KEYWORD_FILE = 'suspicious_words.txt'

def load_keywords(file_path=KEYWORD_FILE):
    if not os.path.isfile(file_path):
        return ['login', 'verify', 'account', 'paypal', 'secure', 'signin', 'password', 'confirm', 'bank']
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file if line.strip()]

def contains_suspicious_keyword(url, keywords):
    return any(word in url.lower() for word in keywords)

def log_result(url, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} - {url} - {result}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    result = ''
    if request.method == 'POST':
        urls = request.form['urls'].splitlines()
        keywords = load_keywords()
        scanned_results = []
        for url in urls:
            url = url.strip()
            if not url: continue
            is_suspicious = contains_suspicious_keyword(url, keywords)
            verdict = "⚠️ Suspicious" if is_suspicious else "✅ Clean"
            log_result(url, verdict)
            scanned_results.append((url, verdict))
        return render_template('index.html', results=scanned_results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
