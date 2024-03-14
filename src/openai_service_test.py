import datetime
import pytest
from unittest import mock
from openai import OpenAI

from openai.types.chat import ChatCompletionMessage
from openai.types.chat.chat_completion import ChatCompletion, Choice

## See https://github.com/openai/openai-python/issues/715#issuecomment-1809203346 for
## examples and source for mocking OpenAI python client

def create_chat_completion(content: str, model = "gpt-3.5-turbo", role: str = "assistant") -> ChatCompletion:
    return ChatCompletion(
        id="foo",
        model=model,
        object="chat.completion",
        choices=[
            Choice(
                finish_reason="stop",
                index=0,
                message=ChatCompletionMessage(
                    content=content,
                    role=role,
                ),
            )
        ],
        created=int(datetime.datetime.now().timestamp()),
    )


@pytest.fixture
def mock_openai():
    client = OpenAI(api_key="sk-...")

    client.chat.completions.create = mock.Mock(
        wraps=client.completions.create,
        return_value=create_chat_completion("Foobar")
    )

    return client

def test_chat_completion(mock_openai):
    EXPECTED_RESPONSE = "The mock is working! ;)"
    EXPECTED_MODEL = "gpt-3.5-turbo"
    client = mock_openai
    client.chat.completions.create.return_value = create_chat_completion(EXPECTED_RESPONSE, EXPECTED_MODEL)

    r = client.chat.completions.create(
        messages=[{"role": "user", "content": "Do you know any jokes?"}],
        model="gpt-3.5-turbo",
    )
    response = r.choices[0].message.content
    assert response == EXPECTED_RESPONSE
    assert r.model == EXPECTED_MODEL
