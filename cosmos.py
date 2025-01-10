import requests
from dotenv import load_dotenv
url = "https://ai.api.nvidia.com/v1/vlm/microsoft/kosmos-2"
import os

api_key = os.getenv('NVIDIA_API_KEY', None)
if not api_key:
    print("Environment variable NVIDIA_API_KEY is not set!")
    raise ValueError("API key is not set!")


payload = {
    "messages": [
        {
            "content": "Where is the coach in this image? <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII==\" />",
            "role": "user"
        }
    ],
    "grounded_response": True,
    "temperature": 0.2,
    "top_p": 0.7,
    "max_tokens": 1024,
    "response_mode": "brief",
    "task": "VQA"
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "accept": "application/json",
}
response = requests.post(url, json=payload, headers=headers)

print(response.text)