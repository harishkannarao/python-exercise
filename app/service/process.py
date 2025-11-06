from app.external import interface


def get_response(url: str) -> str:
    return interface.get_response_from_endpoint(url)


if __name__ == "__main__":
    print(get_response("http://www.example.com"))
