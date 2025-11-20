import requests
import json

API_KEY = "3baf3939c6a5405eba2dc9b2d330fab4"
MODEL = "gemini-2.0-flash-lite"  
ENDPOINT = "https://aoai-farm.bosch-temp.com/api/openai/deployments/google-gemini-2-0-flash-lite/chat/completions"

conversation = [] 

def chat_with_gemini(user_input):
    conversation.append({"role": "user", "parts": [{"text": user_input}]})

    data = {
        "contents": conversation  # Send entire history, not just last message
    }

    try:
        response = requests.post(ENDPOINT, json=data, timeout=10)
        response.raise_for_status()
        result = response.json()

        if "candidates" in result and result["candidates"]:
            reply = result["candidates"][0]["content"]["parts"][0]["text"]

            # Add Gemini's reply to history for continuity
            conversation.append({"role": "model", "parts": [{"text": reply}]})
            return reply
        else:
            return "No response from Gemini."

    except requests.exceptions.Timeout:
        return "Error: Request timed out."
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except KeyError:
        return "Unexpected response format from API."
while(1):
    statement = input("How can I help you ? If you wanna quit click 'Q' : ")
    if(statement == "q" or statement == "Q"):
        break
    else:
        print(chat_with_gemini(statement))
