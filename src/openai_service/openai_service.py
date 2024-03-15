# Light weight wrapper on the OpenAI client to simplify generating and
# interacting with the client. Makes testing easier for other modules

from openai import OpenAI

# Global singleton holding the active API Client
client = None

def init_client(api_key: str=None):
    global client
    assert(api_key != None), "OpenAI Client must be provided an api key on initialization."

    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )

    return client

def destroy_client():
    global client
    client = None

def get_client():
    global client
    assert(client != None), "OpenAI Client must be initialized before use. Call InitClient() first."

    return client

def get_completion(prompt: str, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = get_client().chat.completions.create(
        model=model,
        messages=messages
    )

    return {"content": response.choices[0].message.content, "usage": response.usage}

def get_specific_completion(messages, model="gpt-3.5-turbo"):
    response = get_client().chat.completions.create(
        model=model,
        messages=messages
    )

    return {"content": response.choices[0].message.content, "usage": response.usage}