import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.organization = os.getenv('OPENAI_ORGANIZATION')
openai.api_key = os.getenv('OPENAI_API_KEY')



completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a professional Flutter engineer."},
    {"role": "user", "content": "Is the traditional MVVM architecture the appropriate architecture for creating small mobile applications, or is another architecture more suitable?"},
  ],
  temperature=0,
)

print(completion.choices[0]["message"]["content"].strip())