from base64 import b64encode, b64decode


def btoa(value: str) -> str:
    # btoa source: https://github.com/WebKit/WebKit/blob/fcd2b898ec08eb8b922ff1a60adda7436a9e71de/Source/JavaScriptCore/jsc.cpp#L1419
    binary = value.encode("latin-1")
    return b64encode(binary).decode()


def atob(value: str) -> str:
    binary = b64decode(value.encode())
    return binary.decode("latin-1")
