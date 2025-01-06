import re
import requests

def crawl_directories(url):
   
    try:
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()  

        
        html_content = response.text
        link_pattern = r'href=["\'](.*?)["\']'
        links = re.findall(link_pattern, html_content)

        
        absolute_links = [
            link if link.startswith(('http://', 'https://')) else f"{url.rstrip('/')}/{link.lstrip('/')}"
            for link in links
        ]

        return f"Successfully crawled {url} with {len(absolute_links)} links found:\n" + "\n".join(absolute_links)

    except requests.exceptions.RequestException as e:
        return f"Failed to crawl {url}. Error: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python crawl_script_no_bs4.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]
    print(crawl_directories(target_url))
