from typing import Coroutine

from app.external import interface


def get_response(url: str) -> str:
    return interface.get_response_from_endpoint(url)


async def async_get_response(url: str) -> Coroutine[None, None, str]:
    return interface.async_get_response_from_endpoint(url)


if __name__ == "__main__":
    print(get_response("http://www.example.com"))
