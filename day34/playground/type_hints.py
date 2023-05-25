def police_check(age: int) -> bool:
    '''Check driving eligibility of potential driver

    Args:
        age (int): Users age

    Returns:
        _type_: Boolean
    '''
    if age < 18:
        result = True
    else:
        result = False
    return result  # Change to non bool results in IDE error due to type hint


can_drive = police_check(age="twelve")  # IDE shows error due to type hint
