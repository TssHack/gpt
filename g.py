import requests
import json

def send_request(prompt):
    url = "https://api.binjie.fun/api/generateStream"
    headers = {
        "authority": "api.binjie.fun",
        "method": "POST",
        "path": "/api/generateStream",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://chat18.aichatos.xyz",
        "referer": "https://chat18.aichatos.xyz/",
        "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "userId": "#/chat/1711529530173",
        "network": True,
        "system": "",
        "withoutContext": False,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=True)
        response.raise_for_status()  # Check the status code (raises an error for 4xx or 5xx responses)

        if response.status_code == 200:
            try:
                # Check if the content type is JSON and parse it if so
                if 'application/json' in response.headers.get('Content-Type', ''):
                    result = response.json()  # Parse the response as JSON
                    print(result["text"].encode('latin1').decode('utf-8'))  
                else:
                    # If the response is not JSON, print it as raw text
                    print("Response received: ", response.content.decode('utf-8'))
            except json.JSONDecodeError:
                print("Error decoding JSON response")
                print(f"Raw response from server: {response.text}")  # Print raw response if JSON parsing fails
        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")

# Continuous loop to receive input from the user and send requests
while True:
    try:
        prompt = input("Please enter your question or request: ")
        if prompt.lower() == 'exit':
            print("Exiting the program...")
            break
        send_request(prompt)
    except UnicodeDecodeError:
        print("Error reading input. Please use Latin characters.")
