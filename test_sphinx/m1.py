"""様々な関数の集まり。"""

def non_typed_func(arg1):
    """
    Non-typed function.

    Parameters
    ----------
    arg1 : str
        Argument 1, typed in docstring.

    Returns
    -------
    str
        Output string.
    """
    print(arg1)
    return "this is output1."


def typed_func(arg2: str) -> str:
    """
    typed function.

    Parameters
    ----------
    arg2 :
        Argument 2, typed by type-hint.

    Returns
    -------
    str
        Output string.
    """
    # NOTE: PR04 | Parameter "arg2" has no type
    print(arg2)
    return "this is output2."


def typed_func_too_simple(arg2: str) -> str:
    """
    too-simple typed function.

    Parameters
    ----------
    arg2
        Argument 2, typed by type-hint.

    Returns
    -------
        Output string.
    """
    # NOTE: RT03 | Return value has no description
    print(arg2)
    return "this is output2."


def typed_func_simple(arg2: str) -> str:
    """
    enough-simple typed function.

    Parameters
    ----------
    arg2
        Argument 2, typed by type-hint.

    Returns
    -------
    :
        Output string.
    """
    print(arg2)
    return "this is output2."


def typed_func_best(arg2: str) -> str:
    """
    best-simple typed function.

    Parameters
    ----------
    arg2 :
        Argument 2, typed by type-hint.

    Returns
    -------
     :
        Output string.
    """
    print(arg2)
    return "this is output2."

def typed_func_best_detail(arg2: str) -> str:
    """
    best-detail typed function.

    This is best-detailed enough-simple docstring.

    Parameters
    ----------
    arg2 :
        Argument 2, typed by type-hint.

    Returns
    -------
    opt2 :
        Output string.
    """
    print(arg2)
    return "this is output2."
