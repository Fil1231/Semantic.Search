import sys
import json
import os
from bs4 import BeautifulSoup

def extract_article_body(file_path):
    """
    Extracts the value of the 'articleBody' field from a given HTML file using BeautifulSoup.
    Returns the article body as a string, or None if not found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        soup = BeautifulSoup(content, 'html.parser')

        # Try to find JSON-LD script with articleBody
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(script.string)
                return(data.get('articleBody', 'No articleBody found'))
            except Exception:
                continue
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return None


def list_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def main():
    directory = "www.actualno.com"
    html_files = list_html_files(directory)

    for html_file in html_files:
       article_body = extract_article_body(html_file)
       print(article_body)

if __name__ == "__main__":
    main()
