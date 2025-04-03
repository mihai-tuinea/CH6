import codecs
import base64
import re


def isB64Encoded(string):
    # added '=' in the regex to account for padding
    b64Pattern = re.compile('^[A-Za-z0-9+/=]*$')
    return len(string) % 4 == 0 and bool(b64Pattern.match(string))


with open("CH6.txt", "r") as file:
    ascii_codes = file.read().strip().split()
    # convert ascii to characters
    asciiResult = ''.join(chr(int(code)) for code in ascii_codes)
    # print(asciiResult)
    """
    the result is "\"uXXXX"\"uXXXX"\"uXXXX etc.. so we decode using unicode escape
    """

    unicodeResult = codecs.decode(asciiResult, 'unicode_escape')
    # print(unicodeResult)
    # print(isB64Encoded(unicodeResult))
    """
    unicodeResult matches the base64 pattern, so we decode it using b64
    """

    b64Result = base64.b64decode(unicodeResult)
    # print(b64Result)
    # print(isB64Encoded(b64Result.decode('utf-8')))
    """
    converted b64result into a string by decoding bytes to string
    this printed true thus confirming the string is still encoded in base64
    """

    b64ResultTWO = base64.b64decode(b64Result)
    # print(b64ResultTWO)
    """
    the resulting string started with x89PNG and contained several human-readable snippets
    such as: <xmp:CreatorTool>Snip My on macOS</xmp:CreatorTool>
    this means that the string is no longer encrypted and we can obtain the image
    """

    with open("decoded_image.png", "wb") as img_file:
        img_file.write(b64ResultTWO)


