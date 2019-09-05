import base64
import email.encoders
import email.header
import functools
import hashlib
import html
import quopri
import shlex
import urllib.parse
from typing import Callable, Optional, Iterable, Union

encoders = {}


class Encoder:
    def __init__(
            self,
            encode_name: str,
            encoder: Callable,
            help_text: Optional[str] = None,
            class_: str = None,
            is_binary: bool = False,
            decode_name: str = None,
            decoder: Optional[Callable] = None
    ):
        self.encode_name = encode_name
        self.decode_name = decode_name or encode_name
        self.encoder = encoder
        self.decoder = decoder
        self.help_text = help_text
        self.class_ = class_
        self.is_binary = is_binary
        encoders[self.encode_name] = self

    def encode(self, message: str) -> str:
        return self.encoder(message)

    def decode(self, message: str) -> str:
        return self.decoder(message)


Encoder("email.header.Header", lambda message: email.header.Header(message).encode(),
        decode_name="email.header.decode_header",
        decoder=lambda header: "".join([x[0].decode(x[1]) if isinstance(x[0], bytes) else x[0] for x in email.header.decode_header(header)])
        )
Encoder(
    "quopri.encodestring",
    lambda message: quopri.encodestring(message).decode("ascii"),
    is_binary=True,
    decode_name="quopri.decodestring",
    decoder=lambda message: quopri.decodestring(message.encode("ascii"))
)
Encoder("urllib.parse.quote", lambda message: urllib.parse.quote(message),
        decode_name="urllib.parse.unquote",
        decoder=lambda message: urllib.parse.unquote(message),
        )
Encoder("urllib.parse.quote_plus", lambda message: urllib.parse.quote_plus(message),
        decode_name="urllib.parse.unquote_plus",
        decoder=lambda message: urllib.parse.unquote_plus(message),
        )
Encoder("html.escape", lambda message: html.escape(message),
        decode_name="html.unescape",
        decoder=lambda message: html.unescape(message)
        )
Encoder("shlex.quote", lambda message: shlex.quote(message),
        )
Encoder(
    "base64.b64encode",
    lambda message: base64.b64encode(message).decode(),
    is_binary=True,
)
Encoder(
    "base64.urlsafe_b64encode",
    lambda message: base64.urlsafe_b64encode(message).decode(),
    is_binary=True,
)
Encoder(
    "base64.b32encode",
    lambda message: base64.b32encode(message).decode(),
    is_binary=True,
)
Encoder(
    "base64.b16encode",
    lambda message: base64.b16encode(message).decode(),
    is_binary=True,
)
Encoder(
    "base64.a85encode",
    lambda message: base64.a85encode(message).decode(),
    is_binary=True,
)
Encoder(
    "base64.b85encode",
    lambda message: base64.b85encode(message).decode(),
    is_binary=True,
)


def get_hashed_value(message: bytes, method: str = "md5") -> str:
    return getattr(hashlib, method)(message).hexdigest()


for m in sorted(hashlib.algorithms_guaranteed):
    if m not in {"shake_128", "shake_256"}:
        Encoder(
            "hashlib.%s" % m, functools.partial(get_hashed_value, method=m), is_binary=True
        )
