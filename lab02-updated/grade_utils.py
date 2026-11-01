"""Helpers for converting GPAs (out of 5.00) into letter grades."""


def letter_grade(gpa):
    """Return the letter grade (A-F) for a GPA on the 5.00 scale."""
    # Check from the highest threshold down; the first match wins,
    # so each elif only runs when every condition above it was False.
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
