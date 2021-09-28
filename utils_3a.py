def preprocess(text: str, characters: str) -> str:
    """
    Takes a string and removes the given characters
    :param text: The string to be processed
    :param characters: The characters to remove
    :return: The string without the given characters
    """

    return ''.join([character for character in text if character not in characters])  # Found how to turn a list back into a string here: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string