import base64
import email.encoders
import email.header
import hashlib
import html
import quopri
import shlex
import urllib.parse
from typing import Callable, Optional, Iterable

encoders = {}


class Encoder:
    def __init__(
        self,
        name: str,
        encoder: Callable,
        help_text: Optional[str] = None,
        class_: str = None,
        is_binary: bool = False,
    ):
        self.name = name
        self.encoder = encoder
        self.help_text = help_text
        self.class_ = class_
        self.is_binary = is_binary
        encoders[self.name] = self

    def encode(self, message: str) -> Iterable[str]:
        if self.is_binary:
            encoded_message = message.encode()
            yield self.encoder(encoded_message)
        else:
            yield self.encoder(message)


Encoder("email.header.Header", lambda message: email.header.Header(message).encode())
Encoder(
    "quopri.encodestring",
    lambda message: quopri.encodestring(message).decode(),
    is_binary=True,
)
Encoder("urllib.parse.quote", lambda message: urllib.parse.quote(message))
Encoder("urllib.parse.quote_plus", lambda message: urllib.parse.quote_plus(message))
Encoder("html.escape", lambda message: html.escape(message))
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
Encoder("shlex.quote", lambda message: shlex.quote(message))
for m in sorted(hashlib.algorithms_guaranteed):
    Encoder(
        "hashlib.%s" % m, lambda message: getattr(hashlib, m)(message), is_binary=True
    )
