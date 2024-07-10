def greet(name: str) -> str:
    """
    Return a greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
