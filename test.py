print("python3.8 is running")
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_VERSION = "gpt-3.5-turbo"  # You can choose 'gpt-4' or 'gpt-3.5-turbo'

import openai

openai.api_key = OPENAI_API_KEY

def generate_response(input_text):
    response = openai.ChatCompletion.create(
        model=OPENAI_VERSION,
        messages=[
            {
                "role": "system",
                "content": "You're a helpful assistant known for your sarcasm and concise responses to all queries. In this task, your job is to answer questions in a short and crisp manner, infused with sarcasm. Make sure to provide quick and witty responses to each query thrown your way. Whenever faced with a question, respond with sharp wit and a touch of sarcasm in your tone, keeping the answers brief yet effective.",
            },
            {"role": "user", "content": input_text},
        ],
        max_tokens=500,
        n=1,
        stop=None,
    )
    return response.choices[0].message["content"]

meme_text = generate_response("hello how are you doing?")
print(meme_text)

