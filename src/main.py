from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return {'content': response.choices[0].message.content, 'usage': response.usage}

print('Enter prompt to be sent to ChatGPT. Enter \'exit\' to quit.')
while True:
    prompt = input(">: ")

    if prompt == 'exit':
        exit()

    response = get_completion(prompt)

    print(response['content'])
    print(response['usage'])