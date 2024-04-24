def convert_to_letter_grade(score: float) -> str:
    """Convert a numerical grade to its letter grade representation.

    Args:
        score: the numerical score to convert to a number.

    Returns:
        The uppercase letter representation of the input score.
    
    Raises:
        TypeError: if score is not int or float (numerical).
        ValueError: if score is not valid (not between 0 or 100).
    
    """
    if not type(score) is int and not type(score) is float:
        raise TypeError("Score must be a numeric value.")

    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
