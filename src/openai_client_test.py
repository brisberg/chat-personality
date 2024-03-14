import pytest
import openai_client as oac

@pytest.fixture(autouse=True)
def cleanup_openai_client():
    oac.client = None
    return

## Tests
def test_init_client_without_api_key():
    with pytest.raises(AssertionError):
        oac.init_client()

def test_get_client_initialized():
    oac.init_client(api_key="sk-12345")

    assert oac.get_client()

def test_get_client_not_initialized():
    with pytest.raises(AssertionError):
        oac.get_client()


