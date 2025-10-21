from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "user", "content": "tell me about easyTdd"}
    ],
    temperature=0.7
)

print(response.output_text)