class Greetings:
    @staticmethod
    def greet(input_args):
        result = []
        for arg in input_args:
            result.append(f"Hello, {arg}")
        return result

    @staticmethod
    async def async_greet(input_args) -> list[str]:
        return Greetings().greet(input_args)
