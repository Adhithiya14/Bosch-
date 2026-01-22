def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.split()).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_strings = ['A man a plan a canal Panama', 'Hello', 'Racecar', '12321', 'Not a palindrome']
    for string in test_strings:
        if is_palindrome(string):
            print(f'"{string}" is a palindrome.')
        else:
            print(f'"{string}" is not a palindrome.')