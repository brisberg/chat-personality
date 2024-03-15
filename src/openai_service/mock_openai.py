## See https://github.com/openai/openai-python/issues/715#issuecomment-1809203346 for
## examples and source for mocking OpenAI python client

import datetime
import pytest
import openai_service as service
from unittest import mock
from openai import OpenAI

from openai.types.chat import ChatCompletionMessage
from openai.types.chat.chat_completion import ChatCompletion, Choice

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
    service.destroy_client()
    service.init_client("sk-...")
    client = service.get_client()

    client.chat.completions.create = mock.Mock(
        wraps=client.completions.create,
        return_value=create_chat_completion("Foobar")
    )

    return client