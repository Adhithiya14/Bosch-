def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char.isalpha() and char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

v, c = count_vowels_consonants("Hello World!")
print(f"Vowels: {v}, Consonants: {c}")