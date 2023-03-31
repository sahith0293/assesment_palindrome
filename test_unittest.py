from palindrom import palindrome_strings


def test_palindrome_strings():
    strings = ["MOM", "DAD", "HOUSE", "AEROPLANE", "PET"]
    expected_output = "Count of Palindrome Strings: 2\nPalindrome string: MOM\nPalindrome string: DAD\nCount of Non - Palindrome Strings: 3\nNon - Palindrome string: HOUSE\nNon - Palindrome string: AEROPLANE\nNon - Palindrome string: PET\n"
    
    # Redirect stdout to a buffer
    from io import StringIO
    import sys
    buffer = StringIO()
    sys.stdout = buffer
    
    # Call the function
    palindrome_strings(strings)
    
    # Get the printed output
    output = buffer.getvalue()
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    # Compare the output with the expected output
    assert output == expected_output, f"Output was {output}, but expected {expected_output}"
