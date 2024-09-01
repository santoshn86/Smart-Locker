import requests

# Define the API endpoint
url = "https://aadhaar-number-verification-api-using-pan-number.p.rapidapi.com/api/validation/pan_to_aadhaar"

# Define the payload with your PAN number and consent details
payload = {
    "pan": "BZSPN5764Q",  # Replace with the actual PAN number you want to verify
    "consent": "y",  # 'y' indicates that consent is given
    "consent_text": "I hereby declare my consent agreement for fetching my information via AITAN Labs API"
}

# Define the headers, including your RapidAPI key and host
headers = {
    "x-rapidapi-key": "6a447387dcmsh4886b7e0437817ap1c5d21jsnc02c7876ec99",  # Replace with your actual RapidAPI key
    "x-rapidapi-host": "aadhaar-number-verification-api-using-pan-number.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Send the POST request to the API
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Check if the request was successful

    # Parse the JSON response
    response_data = response.json()

    # Print or process the response as needed
    print("Response from API:", response_data)

except requests.exceptions.RequestException as e:
    print("Error during API request:", e)
