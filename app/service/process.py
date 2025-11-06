from app.external.interface import get_response_from_endpoint


def get_response(url: str) -> str:
    return get_response_from_endpoint(url)


if __name__ == '__main__':
    print(get_response('http://www.example.com'))
