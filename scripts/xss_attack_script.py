import requests

def xss_attack(url, payload):
   
    try:
        response = requests.get(f"{url}?input={payload}", timeout=10)
        response.raise_for_status() 
        if payload in response.text:
            return f"XSS vulnerability detected on {url} with payload: {payload}"
        else:
            return f"No XSS vulnerability detected on {url} with payload: {payload}"
    except requests.exceptions.RequestException as e:
        return f"Failed to test {url}. Error: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python xss_attack_script.py <url> <payload>")
        sys.exit(1)

    target_url = sys.argv[1]
    attack_payload = sys.argv[2]
    print(xss_attack(target_url, attack_payload))
