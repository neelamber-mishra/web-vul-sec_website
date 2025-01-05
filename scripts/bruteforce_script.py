def brute_force(url, username):
    return f"Attempted brute force on {url} with username {username}"

if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    username = sys.argv[2]
    print(brute_force(url, username))
