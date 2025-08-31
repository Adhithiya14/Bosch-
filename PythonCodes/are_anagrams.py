def are_anagrams(str1, str2):
    str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    str2 = ''.join(char.lower() for char in str2 if char.isalnum())
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))