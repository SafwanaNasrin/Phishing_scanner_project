# interactive_url_creator.py

def create_urls_file_interactively(filename="urls_to_scan.txt"):
    print("🔵 Enter URLs one by one. Type 'done' to finish.\n")

    urls = []
    while True:
        url = input("Enter URL: ").strip()
        if url.lower() == 'done':
            break
        if url:  # Ensure it's not empty
            urls.append(url)

    if not urls:
        print("⚠️ No URLs were entered. File not created.")
        return

    try:
        with open(filename, 'w') as file:
            for url in urls:
                file.write(url + '\n')
        print(f"\n✅ Saved {len(urls)} URLs to '{filename}'")
    except Exception as e:
        print(f"❌ Failed to write to '{filename}': {e}")

if __name__ == "__main__":
    create_urls_file_interactively()
