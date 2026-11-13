
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://demo6.ki-ansbach.de/hostedmodels/v1",
    api_key=os.getenv("KDT_API_KEY")
)

response = client.chat.completions.create(
    model="deepseek-v4-flash_chat",
    messages=[
        {"role": "user", "content": "Erkläre kurz, was Sycophancy bei KI bedeutet."}
    ],
    temperature=0.2,
    max_tokens=200
)

print(response.choices[0].message.content)
