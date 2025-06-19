import requests
import time

# A list of websites you want to monitor
# We include a good one and a bad one for this test
WEBSITES_TO_CHECK = [
    "https://google.com",
    "https://amazon.com",
    "http://this-is-a-fake-domain-that-will-fail.com",
    "https://slack.com",
    "https://code.akumotechnology.com"
]

def check_website_status(urls):  # Loops through a list of URLs and checks the status of each one.
    print("--- Starting Website Health Check ---")
    
    for url in urls:
        try:
            response = requests.get(url, timeout=5)   # The 'timeout=5' means we will only wait 5 seconds for a response
            if response.status_code == 200:           # The HTTP status code '200' means "OK" or "Success"
                print(f"SUCCESS: {url} is online and responding correctly.")
            else:                                       # Any other status code (like 404 Not Found, 500 Server Error) is a problem
                print(f" ALERT: {url} is online but returned a status code of {response.status_code}.")

        except requests.ConnectionError:                 # This 'except' block runs if the script can't connect to the server at all
            print(f"CRITICAL: {url} is OFFLINE. Connection failed.")
        except Exception as e:                           # Catch any other unexpected errors
            print(f"An unknown error occurred with {url}: {e}")

    print("Health Check Complete")


if __name__ == "__main__": # This is important for when I want to import this file's functions into a different script. # Standard entry point for direct execution. The code inside this 'if' block will only run when this script is executed directly.It will NOT run if this script is imported as a module into another file.
    check_website_status(WEBSITES_TO_CHECK)

     
