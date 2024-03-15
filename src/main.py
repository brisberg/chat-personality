from dotenv import load_dotenv
from pathlib import Path
import os
from openai import OpenAI
import openai_service.openai_service as openai
import personality
from file_adapter import load_from_file, save_to_file

load_dotenv()

openai.init_client(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

client = openai.get_client()

# Create data directories if they do not exist
file = Path("data/personalities")
file.mkdir(parents=True, exist_ok=True)

pers = personality.Personality()
pers.directory = "abby"
pers.name = "Abby"
pers.clothing = ["Wide Hat"]
pers.physical_attributes = ["tall"]
pers.vocal_attributes = ["sultry"]

save_to_file(pers)
pers = load_from_file(personality.DEFAULT_DIRECTORY + "/abby/personality.pkl")

print(pers)

print('Enter prompt to be sent to ChatGPT. Enter \'exit\' to quit.')
while True:
    prompt = input(">: ")

    if prompt == 'exit':
        exit()

    response = openai.get_completion(prompt)

    print(response['content'])
    print(response['usage'])