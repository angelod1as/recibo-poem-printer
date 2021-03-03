import os


def flash_path():
    try:
        return os.path.join("/", "media", "pi", "D765-45BB")
    except Exception:
        return False
