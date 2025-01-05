import requests
from bs4 import BeautifulSoup

def crawl_directories(url):
    """
    Crawls the given URL and extracts links for further exploration.
    
    Args:
        url (str): The target URL to crawl.
    
    Returns:
        str: Summary of the crawling results.
    """
    try:
        # Send GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links on the page
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        absolute_links = [link if link.startswith('http') else f"{url.rstrip('/')}/{link.lstrip('/')}" for link in links]

        return f"Successfully crawled {url} with {len(absolute_links)} links found:\n" + "\n".join(absolute_links)

    except requests.exceptions.RequestException as e:
        return f"Failed to crawl {url}. Error: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python crawl_script.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]
    print(crawl_directories(target_url))
