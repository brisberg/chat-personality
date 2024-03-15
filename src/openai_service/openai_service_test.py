import pytest
from mock_openai import create_chat_completion, mock_openai
import openai_service as service

@pytest.fixture(autouse=True)
def cleanup_openai_client():
    yield 
    service.destroy_client()
    return

## Tests
def test_init_client_without_api_key():
    with pytest.raises(AssertionError):
        service.init_client()

def test_get_client_initialized():
    service.init_client(api_key="sk-12345")

    assert service.get_client()

def test_get_client_not_initialized():
    with pytest.raises(AssertionError):
        service.get_client()

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
