"""メインスクリプト。"""

def non_typed_func(arg1):
    """Non-typed function.

    Parameters:
        arg1 : str
            argument 1, typed in docstring.
    Returns:
        str
            output string
    """
    print(arg1)
    return "this is manual output."


def main() -> None:
    """Main function."""
    o_ntf = non_typed_func("hello")
    print(o_ntf)
