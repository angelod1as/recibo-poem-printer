import os


def flash_path():
    try:
        # flash = os.path.join("/", "media", "pi", "D765-45BB")
        flash = os.path.join("/", "home", "pi", "poem-printer", "files")
        return flash
    except Exception:
        return False
