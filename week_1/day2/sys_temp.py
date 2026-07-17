import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

apikey = os.getenv("GROQ_API_KEY")

if not apikey:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=apikey)

model = "llama-3.3-70b-versatile"

role="user"

prompt = "Suggest a name for my food company. "

message_system = {
    "role": "system",
    "content": "You are brand manager who suggest name for my food company name should be in one word  suggest only one same the best one  "
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages , temperature=2)

print(response.choices[0].message.content)