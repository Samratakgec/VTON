import requests

# Replace with your actual API key and external user ID
api_key = 'YvZEWVKQvQj5YJD2mUYhcYMxzT6EjiAQ'
external_user_id = 'abcde'

# Step 1: Create Chat Session
create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
create_session_headers = {
    'apikey': api_key
}
create_session_body = {
    "pluginIds": ['plugin-1712327325'],
    "externalUserId": external_user_id
}

# Make the POST request to create a chat session
create_session_response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)

# Check if the request was successful
if create_session_response.status_code == 200:
    # Extract the session ID from the response
    session_id = create_session_response.json().get('data', {}).get('id')
    
    if session_id:
        # Step 2: Submit Query
        submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
        submit_query_headers = {
            'apikey': api_key
        }
        submit_query_body = {
            "endpointId": "predefined-openai-gpt4o",
            "query": "Does the image have a person in it?",
            "pluginIds": ["plugin-1712327325"],
            "responseMode": "sync"
        }

        # Make the POST request to submit the query
        submit_query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)

        # Check if the request was successful
        if submit_query_response.status_code == 200:
            # Print the response from the query submission
            print(submit_query_response.json())
        else:
            print(f"Failed to submit query: {submit_query_response.status_code} - {submit_query_response.text}")
    else:
        print("Failed to extract session ID from the response.")
else:
    print(f"Failed to create chat session: {create_session_response.status_code} - {create_session_response.text}")
