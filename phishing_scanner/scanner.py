import os
import sys
import logging
import time
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama (for colored terminal output)
init(autoreset=True)

# Configure logging
LOG_FILE = "phishing_scanner.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_keywords(file_path='suspicious_words.txt'):
    """
    Loads phishing keywords from a file and returns a list of lowercase words.
    """
    if not os.path.isfile(file_path):
        logging.warning(f"Keyword file '{file_path}' not found. Using default keywords.")
        return [
            'login', 'verify', 'account', 'paypal', 'secure', 'signin', 'password', 'confirm', 'bank', 'webscr',
            'update', 'security', 'alert', 'ebay', 'appleid', 'microsoft', 'amazon', 'google', 'icloud',
            'verifyaccount', 'reset', 'challenge', 'urgent', 'click', 'confirmyouraccount', 'billing',
            'support', 'service', 'administrator', 'notification', 'payment', 'suspend', 'suspended',
            'locked', 'unlock', 'identity', 'access', 'webscr', 'signin', 'confirm', 'security-alert',
            'validate', 'validateaccount', 'account-update', 'confirm-email', 'banking', 'transaction',
            'security-check', 'helpdesk', 'phish', 'fraud', 'compromised', 'account-verification', 'secure-login'
        ]

    try:
        with open(file_path, 'r') as file:
            keywords = [line.strip().lower() for line in file if line.strip()]
            logging.info(f"Loaded {len(keywords)} keywords from '{file_path}'")
            return keywords
    except Exception as e:
        logging.error(f"Error reading keyword file: {e}")
        print(Fore.RED + f"[ERROR] Failed to load keywords: {e}")
        sys.exit(1)

def get_user_input():
    """
    Prompt user to enter URL or exit command.
    """
    return input(Fore.YELLOW + "Enter a URL to scan (or type 'exit' to quit): ").strip()

def validate_url(url):
    """
    Validate if URL starts with http:// or https://
    """
    if not url:
        print(Fore.RED + "URL cannot be empty. Please try again.")
        return False
    if not (url.startswith("http://") or url.startswith("https://")):
        print(Fore.RED + "Please enter a valid URL starting with http:// or https://")
        return False
    return True

def contains_suspicious_keyword(url, keywords):
    """
    Check if any keyword is present in the URL.
    """
    url_lower = url.lower()
    return any(word in url_lower for word in keywords)

def save_scan_result(url, result, filename='scan_results.txt'):
    """
    Save the scan result with timestamp.
    """
    try:
        with open(filename, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {url} - {result}\n")
    except Exception as e:
        logging.error(f"Failed to save scan result: {e}")

def show_loading_animation(duration=2):
    """
    Simulate a loading animation for given duration in seconds.
    """
    print(Fore.CYAN + "Scanning URL", end="", flush=True)
    for _ in range(duration * 3):  # 3 dots per second
        print(Fore.CYAN + ".", end="", flush=True)
        time.sleep(0.33)
    print()  # New line after loading

def process_url_scan(url, keywords):
    """
    Process scanning URL with loading animation and return result message.
    """
    show_loading_animation()
    if contains_suspicious_keyword(url, keywords):
        result = Fore.RED + Style.BRIGHT + "⚠️ Suspicious keyword detected in URL!"
        print(result)
        logging.warning(f"Suspicious URL detected: {url}")
    else:
        result = Fore.GREEN + "✅ No suspicious keywords found."
        print(result)
        logging.info(f"Clean URL scanned: {url}")
    save_scan_result(url, result.strip('\033[0m'))  # Save clean text only

def main():
    print(Fore.CYAN + Style.BRIGHT + "=== Phishing URL Keyword Scanner ===\n")
    keywords = load_keywords()

    while True:
        user_input = get_user_input()
        if user_input.lower() == 'exit':
            print(Fore.CYAN + "Exiting the scanner. Goodbye!")
            break

        if not validate_url(user_input):
            continue

        try:
            process_url_scan(user_input, keywords)
        except Exception as e:
            logging.error(f"Error scanning URL '{user_input}': {e}")
            print(Fore.RED + f"[ERROR] Scanning failed: {e}")

        print()  # Blank line for readability

if __name__ == "__main__":
    main()
