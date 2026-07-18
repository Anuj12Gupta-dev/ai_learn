import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

apikey = os.getenv("GROQ_API_KEY")

if not apikey:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=apikey)

model = "llama-3.3-70b-versatile"

class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object",
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

text="Hello My name is Pratyush. Yesterday I broke up with my girlfriend sheetal I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 82134"
role="user"

prompt = f""" This is a customer ticket . Please extract personal information from this . {text} """


message_system = {
    "role": "system",
    "content": system_prompt
}

message_user = {
    "role": role,
    "content": prompt
}

messages = [message_system, message_user]

response = client.chat.completions.create(model=model, messages=messages , response_format=response_format)

answer = response.choices[0].message.content

print(answer)

# isko padhte kaise hai
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)


# inko pass kr sakte hai aage!
print(ticket.name)
print(ticket.email)
print(ticket.issue)