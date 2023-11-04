import requests
import json

# Define the API endpoints
get_api_url = 'https://experimentihat01.aakashgudivada.repl.co/get'
post_api_url = 'https://experimentihat01.aakashgudivada.repl.co/post'

# Function to retrieve data from the get API
def get_data():
    try:
        response = requests.get(get_api_url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error while getting data: {e}")
        return None

# Function to input id, sname, and fname and send them to the post API
def send_data(id, sname, fname):
    try:
        params = {
            'id': id,
            'sname': sname,
            'fname': fname
        }
        response = requests.get(post_api_url, params=params)
        response.raise_for_status()
        print("Data sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error while sending data: {e}")

# Main program
if __name__ == "__main":
    current_list = get_data()
    if current_list:
        print("Retrieved data from the API:")
        print(json.dumps(current_list, indent=2))
        
        id = input("Enter id: ")
        sname = input("Enter sname: ")
        fname = input("Enter fname: ")
        
        send_data(id, sname, fname)
