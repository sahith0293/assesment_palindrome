def palindrome_strings(strings):
    palindrome_count = 0
    non_palindrome_count = 0
    
    palindrome_strings = []
    non_palindrome_strings = []
    
    for string in strings:
        if string == string[::-1]:  # check if the string is a palindrome
            palindrome_count += 1
            palindrome_strings.append(string)
        else:
            non_palindrome_count += 1
            non_palindrome_strings.append(string)
    
    print("Count of Palindrome Strings:", palindrome_count)
    for palindrome_string in palindrome_strings:
        print("Palindrome string:", palindrome_string)
    
    print("Count of Non - Palindrome Strings:", non_palindrome_count)
    for non_palindrome_string in non_palindrome_strings:
        print("Non - Palindrome string:", non_palindrome_string)

strings = ["MOM", "DAD", "HOUSE", "AEROPLANE", "PET"]
palindrome_strings(strings)
