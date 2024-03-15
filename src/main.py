from dotenv import load_dotenv
from pathlib import Path
import os
from openai import OpenAI
import openai_service.openai_service as openai
import personality
from persistance.file_adapter import FileAdapter
from phrase import PhraseGroup

load_dotenv()

openai.init_client(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

client = openai.get_client()

# Create data directories if they do not exist
file = Path("data/personalities")
file.mkdir(parents=True, exist_ok=True)

file_loader = FileAdapter("data/personalities")

# pers = personality.Personality(
#     directory="abby",
#     name = "Abby",
#     clothing = ["Wide Hat"],
#     physical_attributes = ["tall"],
#     vocal_attributes = ["sultry"]
# )

# file_loader.save_to_file(pers)
pers = file_loader.load_from_file("/abby/personality.pkl")

# greeting = PhraseGroup(pers, ["Give me a short, friendly greeting as if we haven't seen each other since yesterday"])
greeting = file_loader.load_from_file("/abby/greetings.pkl")
print(greeting.get_random_response())
file_loader.save_to_file(greeting)

print('Enter prompt to be sent to ChatGPT. Enter \'exit\' to quit.')
while True:
    prompt = input(">: ")

    if prompt == 'exit':
        exit()

    response = openai.get_completion(prompt)

    print(response['content'])
    print(response['usage'])