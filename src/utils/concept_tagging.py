import requests

API_URL = "http://localhost:5000/tag"

def get_tags(text):
    """
    Sends a request to the Concept Tagging API and returns the tags.
    Args:
        text (str): Input text to be tagged.
    Returns:
        list: Extracted tags from the text.
    """
    response = requests.post(API_URL, json={"text": text})
    if response.status_code == 200:
        return response.json().get("tags", [])
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
