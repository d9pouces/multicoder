import argparse
from typing import Tuple, Iterable

from multicoder.encoders import encoders

__author__ = "flanker"

__all__ = ["main"]


def decode_text(message) -> Iterable[Tuple[str, str]]:
    for encoder in encoders.values():
        if encoder.decoder is None:
            continue
        try:

            decoded_message = encoder.decode(message)
            if encoder.is_binary:
                decoded_message = decoded_message.decode()
        except Exception as e:
            decoded_message = "(invalid: %s )" % e
        yield encoder.decode_name, decoded_message


def encode_text(message) -> Iterable[Tuple[str, str]]:
    for encoder in encoders.values():
        try:
            if encoder.is_binary:
                message = message.encode()
            encoded_message = encoder.encode(message)
        except Exception as e:
            encoded_message = "(invalid: %s )" % e
        yield encoder.encode_name, encoded_message


def main(args=None):
    parser = argparse.ArgumentParser(description="Display standard encodings")
    parser.add_argument(
        "-g", "--guess", help="guess which encoding provides this result", default=None
    )
    parser.add_argument(
        "-r", "--reverse", help="try to decode the provided text", default=False,
        action="store_true"
    )
    parser.add_argument("text", help="text to encode in different ways")
    args = parser.parse_args(args)

    src_text = args.text
    dst_text = args.guess
    reverse = args.reverse
    if reverse:
        for name, msg in decode_text(src_text):
            print("%s : %s" % (name, msg))
    elif dst_text:
        for name, msg in encode_text(src_text):
            if msg == dst_text:
                print("%s : %s" % (name, msg))
    else:
        for name, msg in encode_text(src_text):
            print("%s : %s" % (name, msg))


if __name__ == "__main__":
    main()
