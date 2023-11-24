def is_palindrome(phrase):
    reverse_phrase = phrase[::-1]
    joined_phrase = ''.join(phrase.split())
    joined_reverse_phrase = ''.join(reverse_phrase.split())
    if joined_reverse_phrase.lower() == joined_phrase.lower():
        return True
    else:
        return False
    



"""Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
