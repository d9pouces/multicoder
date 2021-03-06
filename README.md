Multicoder
==========

Ever asked yourself which encoding returns "Test%20with%20special%20chars%3A%20%24%20%C3%A9%C3%A8%20%26%20.%3B/%3D"?
Multicoder to the rescue!

Multicoder will encode, or decode, the given text using the standard encodings.

```bash
$ pip3 install multicoder
$ multicoder -r Test%20with%20special%20chars%3A%20%24%20%C3%A9%C3%A8%20%26%20.%3B/%3D
email.header.decode_header : Test%20with%20special%20chars%3A%20%24%20%C3%A9%C3%A8%20%26%20.%3B/%3D
quopri.decodestring : Test%20with%20special%20chars%3A%20%24%20%C3%A9%C3%A8%20%26%20.%3B/%3D
urllib.parse.unquote : Test with special chars: $ éè & .;/=
urllib.parse.unquote_plus : Test with special chars: $ éè & .;/=
html.unescape : Test%20with%20special%20chars%3A%20%24%20%C3%A9%C3%A8%20%26%20.%3B/%3D
base64.b64encode : (invalid: Invalid base64-encoded string: number of data characters (53) cannot be 1 more than a multiple of 4 )
base64.urlsafe_b64encode : (invalid: Invalid base64-encoded string: number of data characters (53) cannot be 1 more than a multiple of 4 )
```

You can encode or decode the provided text (of course, some methods can only encode since they are actually hash methods, not encoding ones…):
```bash
$ multicoder "Test with special chars: \$ éè & .;/="
email.header.Header : =?utf-8?b?VGVzdCB3aXRoIHNwZWNpYWwgY2hhcnM6ICQgw6nDqCAmIC47Lz0=?=
quopri.encodestring : Test with special chars: $ =C3=A9=C3=A8 & .;/=3D
urllib.parse.quote : Test%20with%20special%20chars%3A%20%24%20%C3%A9%C3%A8%20%26%20.%3B/%3D
urllib.parse.quote_plus : Test+with+special+chars%3A+%24+%C3%A9%C3%A8+%26+.%3B%2F%3D
html.escape : Test with special chars: $ éè &amp; .;/=
shlex.quote : 'Test with special chars: $ éè & .;/='
base64.b64encode : VGVzdCB3aXRoIHNwZWNpYWwgY2hhcnM6ICQgw6nDqCAmIC47Lz0=
base64.urlsafe_b64encode : VGVzdCB3aXRoIHNwZWNpYWwgY2hhcnM6ICQgw6nDqCAmIC47Lz0=
base64.b32encode : KRSXG5BAO5UXI2BAONYGKY3JMFWCAY3IMFZHGORAEQQMHKODVAQCMIBOHMXT2===
base64.b16encode : 546573742077697468207370656369616C2063686172733A202420C3A9C3A82026202E3B2F3D
base64.a85encode : <+U,m+EqOABHVA8ARfF_C`m5$@<-EM+=&)IWPbYW-6Op&00K
base64.b85encode : RAqB?Aa`kWXdrWNWn*b!Y#?K3VRCaiAS58esl%usCLk_5FFg
hashlib.blake2b : 191d8425db0082f6c2c014602f7d9876281c17373939a3661fca520d47c43ba5b941856674e15487aa251b77efaf3dbb9470b90d88e85b3d12660c2c45abaf91
hashlib.blake2s : eb5fcb76ab5b1e71f698133f5d634c6892eb27ea562d02f2f650e0826a2c9dbc
hashlib.md5 : 3283fc37323faaf908e77aa1fdab8e57
hashlib.sha1 : 439a025a45e73fce2786a549e7ddf89e4b91c438
hashlib.sha224 : 34c446d4f0a74ba9126a52193dc31ca8e0e0a2b396cd37509811f291
hashlib.sha256 : 42a905181300cd433e9985dec166e33cdc21edc6bcd699e48315cef41d00a9a8
hashlib.sha384 : bd6ab20dbf0c28cdb759ef24d404035de561cad4a0a6864e82db3f5047e183da8f33820887dbe8a7e3b867f4175600c1
hashlib.sha3_224 : e3232527279f04255a037840580917c4cebe7179457bb514fd7fc920
hashlib.sha3_256 : ce1efa90097c42405a0859ed8c58660814d920b0e4063a862c97852bc164c91c
hashlib.sha3_384 : 0b6e96e03855a57b01c4da29793ca3790b024a860ca3c858092ea361be9872d72001b1c7878cf7bea13a4aae5c3a0dc2
hashlib.sha3_512 : bc72fb7932dd319d4b5622d91e921b44e2a0ad3ab21205c6c7dd8558dadd491b0e7abfdf9b5c345c6120e8686c26aab71df5520b30839bd1907ae305d2060fba
hashlib.sha512 : 8a5785883b4acc2bd17ca91511d598bad9784f22bf4a8f420df779a8beae43cdee3e2053d47e40b89b29ce4804c6043ad36c75e8f2c3496c0473cb97c0e60ea6
```

If you known both clear and encoded text, you can display valid encodings:
```bash
$ multicoder "Test with special chars: \$ éè & .;/=" -o 3283fc37323faaf908e77aa1fdab8e57
hashlib.md5 : 3283fc37323faaf908e77aa1fdab8e57
```

Probably not the script of the decade but it can help.