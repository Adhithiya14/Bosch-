def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len, default="")

sentence = "The quick brown fox jumps over the lazy dog"
print(longest_word(sentence))