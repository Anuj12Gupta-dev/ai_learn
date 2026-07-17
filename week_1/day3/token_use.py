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

prompt1 = "Hi!!"
prompt2 = "Explain about time travel "
prompt3 = "Write in brief on machine learning in 1000 words"

prompts = [ prompt1,prompt2,prompt3]

for prompt in prompts :
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages , max_tokens=50)

    usage = response.usage
    print(f"Prompt: {prompt} --> Your Tokens  : {usage.prompt_tokens} , Completion Tokens : {usage.completion_tokens} , Total Tokens : {usage.total_tokens} Finish Reason : {response.choices[0].finish_reason}  ")

    # print(response.choices[0].message.content)




