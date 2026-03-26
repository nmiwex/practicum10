def check_length(message: str):
    """
    checks that the string length is less than 160
    """
    if len(message) <= 160:
        return message
    return message[:160]
