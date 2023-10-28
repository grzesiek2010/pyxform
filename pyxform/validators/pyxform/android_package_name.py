import re
from typing import Optional


def validate_android_package_name(name: str) -> Optional[str]:
    prefix = "Parameter 'app' has an invalid Android package name - "

    if not name.strip():
        return f"{prefix}package name is missing."

    if "." not in name:
        return f"{prefix}the package name must have at least one '.' separator."

    if name[-1] == ".":
        return f"{prefix}the package name cannot end in a '.' separator."

    segments = name.split(".")
    if any(segment == "" for segment in segments):
        return f"{prefix}package segments must be of non-zero length."

    if any(segment.startswith("_") for segment in segments):
        return f"{prefix}the character '_' cannot be the first character in a package name segment."

    if any(segment[0].isdigit() for segment in segments):
        return f"{prefix}a digit cannot be the first character in a package name segment."

    pattern = re.compile(r"[^a-zA-Z0-9._]")
    for segment in segments:
        if pattern.search(segment):
            return f"{prefix}the package name contains not allowed characters."

    return None