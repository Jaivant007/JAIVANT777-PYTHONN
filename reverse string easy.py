def reverse_string(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

word = input("String: ")
reversed_word = reverse_string(word)
print(f"Reverse String: {reversed_word}")
