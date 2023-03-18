import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json
from time import sleep

username = input ("Enter your username: ")
password = getpass ("Enter your password: ")

url = "https://10.255.1.101/api/interfaces/physical"
creds = HTTPBasicAuth(username,password)
headers = {"Accept":"application/json"}

# READ API DATA, HANDLE REQUEST TIMEOUT
attempts = 3
timeout = 5
no_of_tries = 0

while (no_of_tries<attempts):
    no_of_tries+=1

    try:
        #READ THE TARGET URL
        response = requests.get(url=url,auth=creds,headers=headers,verify=False, timeout=timeout)

        #IF SUCCESSFUL, Return the response
        if response.ok:
            print("Query executed successfully...")
            print(response)
            break
        
        #IF UNSUCCESSFUL, Handle error code 429 (too many requests)
        # - wait "Retry-After" seconds or 1 sec
        # - retry

        elif response.status_code == 429:
            try:
                retry_after = int(response.headers.get('Retry-After'))
            except:
                retry_after = 1
        
            print(f"Handling error 429, too many requests. Will try aftert {retry_after} seconds.")
            sleep(retry_after)
            continue

        else:
            # IF UNSUCCESSFULL and not 429, then it's somethign unrecoverable
            print("HTTP Error code: " + str(response.status_code))
            print("HTTP Error: \n" + str(response.text))
            
    except:
        print("Timeout error, try again...")
        continue

    #RETURN "NONE" IF UNSUCESSFULL after all attempts
    if (no_of_tries==attempts):
        print("Unable to get any response.")
        print(None)
