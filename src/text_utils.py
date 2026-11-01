"""Helpers for cleaning up messy text fields."""


def clean_name(raw):
    """Strip, collapse inner whitespace, and title-case a name."""
    # .split() with no argument splits on ANY run of whitespace and
    # drops leading/trailing spaces, so joining with " " leaves single spaces.
    collapsed = " ".join(raw.split())
    return collapsed.title()
