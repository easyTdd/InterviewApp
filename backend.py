from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

prompts = [
    {
        "role": "system", 
        "content": "You are a helpful interview preparation assistant. You are interviewing the user for a .NET Software Developer position. The user is shown a greeting at the beginning of the conversation. Assume you have already said: “Hi, it’s great to meet you. I’m glad you could make it today. Before we begin, how are you feeling?” The first user response will be an answer to this question. In the background, think of the top 10 questions for this interview and ask them one by one. When the user answers, write feedback in italics, then proceed with the next question. After all 10 questions, thank the user and conclude the interview."
    }
];

def get_openai_response(
        history,
        temperature=0.7):
    fullInput = [prompts[-1]] + history

    response = client.responses.create(
        model="gpt-4.1",
        input=fullInput,
        temperature=temperature
    )

    return response.output_text
