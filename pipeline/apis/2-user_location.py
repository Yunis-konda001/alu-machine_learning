#!/usr/bin/env python3
"""
Script that prints the location of a GitHub user
"""

import sys
import requests
import time


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # If rate limit exceeded
    if response.status_code == 403:
        reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
        current_time = int(time.time())
        minutes = (reset_time - current_time) // 60
        print(f"Reset in {minutes} min")

    # If user not found
    elif response.status_code == 404:
        print("Not found")

    # If user exists
    elif response.status_code == 200:
        data = response.json()
        print(data.get("location"))

    else:
        print("Error")
