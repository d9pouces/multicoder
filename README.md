Multicoder
==========

Ever asked yourself which encoding returns "Il+n%27y+a+personne+qui+n%27aime+la+souffrance+pour+elle-m%C3%AAme%2C+qui+ne+la+recherche+et+qui+ne+la+veuille+pour+elle-m%C3%AAme%E2%80%A6"?
Multicoder to the rescue!

```bash

>> pip3 install multicoder
>> multicoder -r "Il+n%27y+a+personne+qui+n%27aime+la+souffrance+pour+elle-m%C3%AAme%2C+qui+ne+la+recherche+et+qui+ne+la+veuille+pour+elle-m%C3%AAme%E2%80%A6"
email.header.decode_header : Il+n%27y+a+personne+qui+n%27aime+la+souffrance+pour+elle-m%C3%AAme%2C+qui+ne+la+recherche+et+qui+ne+la+veuille+pour+elle-m%C3%AAme%E2%80%A6
quopri.decodestring : Il+n%27y+a+personne+qui+n%27aime+la+souffrance+pour+elle-m%C3%AAme%2C+qui+ne+la+recherche+et+qui+ne+la+veuille+pour+elle-m%C3%AAme%E2%80%A6
urllib.parse.unquote : Il+n'y+a+personne+qui+n'aime+la+souffrance+pour+elle-même,+qui+ne+la+recherche+et+qui+ne+la+veuille+pour+elle-même…
urllib.parse.unquote_plus : Il n'y a personne qui n'aime la souffrance pour elle-même, qui ne la recherche et qui ne la veuille pour elle-même…
html.unescape : Il+n%27y+a+personne+qui+n%27aime+la+souffrance+pour+elle-m%C3%AAme%2C+qui+ne+la+recherche+et+qui+ne+la+veuille+pour+elle-m%C3%AAme%E2%80%A6
base64.b64encode : (invalid: Incorrect padding )
base64.urlsafe_b64encode : (invalid: Invalid base64-encoded string: number of data characters (129) cannot be 1 more than a multiple of 4 )
```

 