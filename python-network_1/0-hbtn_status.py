"""
a python scripts that fetches https://alu-intranet.hbtn.io/status
"""
import requests

def fetch_hbtn_io_status():
    """
     you must use the package requests
     allowed to import requests only
    """

    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    data = response.json()

    print("Body response")
    print("\t-type:", type(data))
    print("\t-content:", data)
if __name__ == "__main__":
    fetch_hbtn_io_status()