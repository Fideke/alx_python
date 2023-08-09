#!/usr/bin/env python3
"""
a python scripts that fetches https://alu-intranet.hbtn.io/status
"""


import requests



def fetch_hbtn_status():
    """
     you must use the package requests
     allowed to import requests only
    """

    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    context_type = type(response.text)
    content = response.text

    print("Body response")
    print(f"\t-type: {context_type}")
    print(f"\t-content: {content}")

if __name__ == "__main__":
    fetch_hbtn_status()
