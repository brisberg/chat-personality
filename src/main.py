from dotenv import load_dotenv
import os
from openai import OpenAI
import openai_service.openai_service as openai

load_dotenv()

openai.init_client(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

client = openai.get_client()

print('Enter prompt to be sent to ChatGPT. Enter \'exit\' to quit.')
while True:
    prompt = input(">: ")

    if prompt == 'exit':
        exit()

    response = openai.get_completion(prompt)

    print(response['content'])
    print(response['usage'])