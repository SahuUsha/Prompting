from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()  # Loads environment variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Correct way in Python

result = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "what is 2+3"
        }
    ]
)

print(result.choices[0].message.content)  # 'choices' not 'choice'


# 1. Zero shot prompting 
# 2 . few shot prompting --> we give example in system prompt