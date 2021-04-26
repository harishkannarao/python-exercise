class Greetings:

    @staticmethod
    def greet(input_args):
        result = []
        for arg in input_args:
            result.append(f"Hello, {arg}")
        return result
