"""メインスクリプト."""


from .m1 import non_typed_func, typed_func, typed_func_best, typed_func_simple, typed_func_too_simple 

def main() -> None:
    """Main function."""
    o_ntf = non_typed_func("hello")
    print(o_ntf)

    o_tf = typed_func("world")
    print(o_tf)

    o_tfs = typed_func_simple("hello:world")
    print(o_tfs)

    o_tft = typed_func_too_simple("hello:world:too")
    print(o_tft)

    o_tfb = typed_func_best("hello:world:best")
    print(o_tfb)

    print("end.")


if __name__ == "__main__":
    main()