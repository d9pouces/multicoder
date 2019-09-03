import argparse

__author__ = "flanker"

__all__ = ["main"]


def main(args=None):
    """Main function

    Returns:
      * :class:`int`: 0 in case of success, != 0 if something went wrong

    """
    parser = argparse.ArgumentParser(description="Display standard encodings")
    parser.add_argument(
        "--hash", action="store_true", help="display common hashes", default=False
    )
    parser.add_argument(
        "-g", "--guess", help="guess which encoding provides this result", default=None
    )
    parser.add_argument("text", help="text to encode in different ways")
    args = parser.parse_args(args)
    return_code = 0  # 0 = success, != 0 = error
    # complete this function
    return return_code


if __name__ == "__main__":
    main()
