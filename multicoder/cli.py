import argparse
from typing import Tuple, Iterable

from multicoder.encoders import encoders

__author__ = "flanker"

__all__ = ["main"]


def encode_text(message) -> Iterable[Tuple[str, str]]:
    for encoder in encoders.values():
        if encoder.is_binary:
            encoded_message = encoder.encode(message.encode())
        else:
            encoded_message = encoder.encode(message)
        yield encoder.name, encoded_message


def main(args=None):
    parser = argparse.ArgumentParser(description="Display standard encodings")
    parser.add_argument(
        "-g", "--guess", help="guess which encoding provides this result", default=None
    )
    parser.add_argument("text", help="text to encode in different ways")
    args = parser.parse_args(args)

    src_text = args.text
    dst_text = args.guess
    if dst_text:
        for name, msg in encode_text(src_text):
            if msg == dst_text:
                print("%s : %s" % (name, msg))
    else:
        for name, msg in encode_text(src_text):
            print("%s : %s" % (name, msg))



if __name__ == "__main__":
    main()
