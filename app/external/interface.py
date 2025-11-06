import requests
from requests import Response


def get_response_from_endpoint(url: str) -> str:
    response: Response = requests.get(url)
    return response.text


if __name__ == "__main__":
    print(get_response_from_endpoint("http://www.example.com"))
